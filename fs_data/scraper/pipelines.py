import logging, requests
from django.db.utils import IntegrityError
from scrapy.exceptions import DropItem
from dynamic_scraper.models import SchedulerRuntime

class DjangoWriterPipeline(object):
    
    def prepare_currency_convs(self, item, spider):
        if spider.ref_object.nc_symbol != ''::
            symbol = spider.ref_object.nc_symbol
            if not hasattr(spider, 'nc_conv_rate'):
                if hasattr(spider, 'nc_conv_rate_api_request_failed'):
                    raise DropItem("First fixer.io API request already failed, will no try again, \
                        please restart scraping process with manual conv rate addition.")
                
                r = requests.get('http://api.fixer.io/latest?symbols={symbol}'.format(symbol=symbol))
                if r.status_code == 200:
                    r_json = r.json()
                    conv_date = r_json['date']
                    
                    if symbol in r_json['rates']:
                        conv_rate = r_json['rates'][symbol]
                        logging.info(str(type(conv_rate)))
                        spider.nc_conv_rate = conv_rate
                        spider.nc_conv_date = conv_date
                        item['nc_conv_rate'] = round(conv_rate, 4)  
                        item['nc_conv_date'] = conv_date
                        spider.log("Currency conv rate for {symbol} read from fixer.io API ({rate}, {date}).".format(
                            symbol=symbol, rate=conv_rate, date=conv_date), logging.INFO)
                    else:
                        spider.nc_conv_rate_api_request_failed = True
                        raise DropItem("No corresponding currency rate for {symbol} found \
                            on requesting fixer.io API, enter manually.".format(
                            symbol))
                else:
                    spider.nc_conv_rate_api_request_failed = True
                    raise DropItem("Currency conv rate could not be read from fixer.io API.")
            else:
                item['nc_conv_rate'] = spider.nc_conv_rate
                item['nc_conv_date'] = spider.nc_conv_date
                spider.log("Using cached {symbol} currency conversion rate from fixer.io API.".format(
                    symbol=symbol))
            
            item['amount_nc'] = round(float(item['amount_nc']))
            item['amount_euro'] = round(float(item['amount_nc']) / float(item['nc_conv_rate']), 2)
            item['sub_payments_euro'] = str(item['nc_conv_rate']) + 'CONV' + str(item['sub_payments_nc'])
        else:
            item['amount_euro'] = round(float(item['amount_euro']))
        
        return item
    
    
    def process_item(self, item, spider):
        item = self.prepare_currency_convs(item, spider)
        item['year'] = int(item['year'])
        
        if spider.conf['DO_ACTION']:
            try:
                #item['country'] = spider.ref_object
                item.save()
                
                spider.action_successful = True
                spider.log("Item saved.", logging.INFO)

            except IntegrityError, e:
                spider.log(str(e), logging.ERROR)
                spider.log(str(item._errors), logging.ERROR)
                raise DropItem("Missing attribute.")
        else:
            if not item.is_valid():
                spider.log(str(item._errors), logging.ERROR)
                raise DropItem("Missing attribute.")

        return item
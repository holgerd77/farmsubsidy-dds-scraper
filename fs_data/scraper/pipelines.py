from django.db.utils import IntegrityError
from scrapy import log
from scrapy.exceptions import DropItem
from dynamic_scraper.models import SchedulerRuntime

class DjangoWriterPipeline(object):

    def process_item(self, item, spider):
        if spider.conf['DO_ACTION']:
            try:
                #item['country'] = spider.ref_object
                item.save()
                
                spider.action_successful = True
                spider.log("Item saved.", log.INFO)

            except IntegrityError, e:
                spider.log(str(e), log.ERROR)
                spider.log(str(item._errors), log.ERROR)
                raise DropItem("Missing attribute.")
        else:
            if not item.is_valid():
                spider.log(str(item._errors), log.ERROR)
                raise DropItem("Missing attribute.")

        return item
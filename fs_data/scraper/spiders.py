from dynamic_scraper.spiders.django_spider import DjangoSpider
from fs_data.models import Agency, Payment, PaymentItem


class PaymentSpider(DjangoSpider):

    name = 'payment_spider'

    def __init__(self, *args, **kwargs):
        self._set_ref_object(Agency, **kwargs)
        self.scraper = self.ref_object.scraper
        self.scrape_url = self.ref_object.scrape_url
        self.scraped_obj_class = Payment
        self.scraped_obj_item_class = PaymentItem
        super(PaymentSpider, self).__init__(self, *args, **kwargs)
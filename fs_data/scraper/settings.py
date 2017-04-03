import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "openfarmsubsidies.settings") #Changed in DDS v.0.3

BOT_NAME = 'farmsubsidy_org'

SPIDER_MODULES = ['dynamic_scraper.spiders', 'fs_data.scraper',]
USER_AGENT = '%s/%s' % (BOT_NAME, '1.0')

DOWNLOAD_DELAY = 0.25
DOWNLOAD_TIMEOUT = 30

#Scrapy 0.20+
ITEM_PIPELINES = {
    'dynamic_scraper.pipelines.ValidationPipeline': 400,
    'fs_data.scraper.pipelines.DjangoWriterPipeline': 800,
}

FEED_EXPORTERS = {
    'ujsonlines': 'fs_data.scraper.exporter.UnicodeJsonLinesItemExporter',
}
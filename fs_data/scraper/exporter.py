import json
from scrapy.contrib.exporter import BaseItemExporter


class UnicodeJsonLinesItemExporter(BaseItemExporter):
    '''
    Solution from:
    https://groups.google.com/forum/#!msg/scrapy-users/rJcfSFVZ3O4/HcG-ai2aqRsJ, 2016-01-26
    Not used, raises UnicodeDecodeError, but points in the right (?) direction
    '''    
    def __init__(self, file, **kwargs):
        self._configure(kwargs)
        self.file = file
        self.encoder = json.JSONEncoder(ensure_ascii=False, **kwargs)

    def export_item(self, item):
        itemdict = dict(self._get_serialized_fields(item))
        self.file.write(self.encoder.encode(itemdict) + '\n')
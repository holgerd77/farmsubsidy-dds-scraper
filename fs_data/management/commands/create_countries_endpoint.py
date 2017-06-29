import json
from collections import OrderedDict
from django.core.management.base import BaseCommand, CommandError
from fs_data.models import Country

class Command(BaseCommand):
    help = 'Creates the JSON output for the countries endpoint of the API'

    def add_arguments(self, parser):
        pass
        #parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        countries = Country.objects.exclude(scraper__status='I')
        countries_dict = OrderedDict()
        
        for c in countries:
            c_dict = OrderedDict()
            c_dict.update({ 'name': c.name})
            c_dict.update({ 'agency_name': c.agency_name})
            c_dict.update({ 'info_url': c.info_url})
            c_dict.update({ 'data_url': c.data_url})
            c_dict.update({ 'language_code': c.language_code})
            c_dict.update({ 'nc_symbol': c.nc_symbol})
            c_dict.update({ 'nc_sign': c.nc_sign})
            
            countries_dict.update({ c.country_code: c_dict })
        
        self.stdout.write(json.dumps(countries_dict, indent=4))
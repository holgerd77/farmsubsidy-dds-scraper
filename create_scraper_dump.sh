#!/bin/bash

if [ "$#" -ne 1 ]; then
  echo "Usage: ./create_scraper_dump.sh DDS_VERSION(e.g. 090)" >&2
  exit 1
fi

directory=scraper_dumps/
file_name=farmsubsidy_scraper_dump_$(date +'%Y-%m-%d')_dds_v$1.json
printf "File      : ${file_name}\nDirectory : ${directory}\n\n"

python manage.py dumpdata --indent 4 dynamic_scraper fs_data > ${directory}${file_name}

printf "Scraper dump successfully written.\n" 
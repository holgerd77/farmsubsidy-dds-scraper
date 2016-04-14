#!/bin/bash
#Shorthand for scraping command

if [ "$#" -ne 5 ]; then
  echo "Usage: ./scrape.sh FILENAME LOGLEVEL ID MAX_ITEMS_READ MAX_PAGES_READ" >&2
  echo "Example: ./scrape.sh test.json DEBUG GB 8 2" >&2
  exit 1
fi

scrapy crawl --output=$1 --output-format=ujsonlines payment_spider -L $2 -a id=$3 -a max_items_read=$4 -a max_pages_read=$5

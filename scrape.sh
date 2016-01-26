#!/bin/bash
#Shorthand for scraping command

if [ "$#" -ne 5 ]; then
  echo "Usage: ./scrape.sh FILENAME LOGLEVEL ID MAX_PAGES_READ MAX_ITEMS_READ" >&2
  echo "Example: ./scrape.sh test.json DEBUG GB 2 8" >&2
  exit 1
fi

scrapy crawl --output=$1 --output-format=jsonlines payment_spider -L $2 -a id=$3 -a max_pages_read=$4 -a max_items_read=$5
#!/bin/bash
#Shorthand for scraping command

if [ "$#" -lt 3 ]; then
  echo "Usage: ./scrape.sh FILENAME LOGLEVEL ID [MAX_ITEMS_READ MAX_PAGES_READ]" >&2
  echo "Example: ./scrape.sh test.json DEBUG GB 8 2" >&2
  exit 1
fi

if [ -f $1 ]; then
  echo "File exists, deleting to avoid side effects..."
  rm $1
fi

CMD="scrapy crawl --output=$1 --output-format=ujsonlines payment_spider -L $2 -a id=$3"
if [ ! -z "$4" ]; then
  CMD="$CMD -a max_items_read=$4"
fi
if [ ! -z "$5" ]; then
  CMD="$CMD -a max_pages_read=$5"
fi
echo $CMD
$CMD

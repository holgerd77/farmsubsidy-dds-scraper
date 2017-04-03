#!/bin/bash
#/home/ubuntu/scripts/gunicorn-scraper.sh
set -e
source ~/.bashrc
source ~/venv-scraper/bin/activate
cd /home/ubuntu/openfarmsubsidies-scraper/
# exec is important, otherwise supervisor is not able to stop/restart the process, see:
# https://github.com/benoitc/gunicorn/issues/199
exec gunicorn --workers=5 --bind=127.0.0.1:8000 openfarmsubsidies.wsgi:application
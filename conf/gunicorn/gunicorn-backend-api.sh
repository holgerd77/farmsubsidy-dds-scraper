#!/bin/bash
#/home/ubuntu/scripts/gunicorn-scraper.sh
set -e
source ~/.bashrc
source ~/venv-backend-api/bin/activate
cd /home/ubuntu/openfarmsubsidies-backend-api/
# exec is important, otherwise supervisor is not able to stop/restart the process, see:
# https://github.com/benoitc/gunicorn/issues/199
exec gunicorn -w 4 -b 127.0.0.1:8010 app:app

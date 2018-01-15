#!/bin/bash

source /home/alu5604/.virtualenvs/vm/bin/activate
uwsgi --ini /home/alu5604/webapps/vm/uwsgi.ini

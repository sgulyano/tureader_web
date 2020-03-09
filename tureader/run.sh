#!/bin/sh

cd tureader

python manage.py makemigrations readerapp --no-input
python manage.py migrate --no-input

#python manage.py load res/readerlist.csv 
python manage.py collectstatic --no-input --clear

#rm -rf /code/tureader/res

cd ..

exec "$@"
python manage.py makemigrations readerapp
python manage.py migrate
python manage.py load res/readerlist.csv 
python manage.py createsuperuser
python manage.py collectstatic

# TU Reader Web

เว็บไซต์สำหรับสืบค้นข้อมูลรายชื่อผู้ทรงคุณวุฒิสำหรับการขอเลื่อนตำแหน่งทางวิชาการ จัดทำให้แก่ฝ่ายงานพิจารณาตำแหน่ง

----
## Architecture
This website is implemented using Django 1.11 (for the compatibility with Oracle 10g using as the backend database) deployed using Gunicorn and Nginx and wrapped using Docker (see this tutorial: https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/)

![Reader Database UML](https://github.com/sgulyano/tureader_web/blob/django1.11/reader_uml.png)
The database schema is given in the above diagram. The main entity is the Reader. A Reader may have at most one affiliation (University entity) and may be the reader in one or many fields according to MUA (AcademicField entity).

----
## Setup
1. Install Docker
2. Edit the `.env` file to configure the website
3. To start the web service, 
    ```
    docker-compose up --build -d
    ```
4. To create super user,
    ```
    docker-compose exec web base -c "cd /code/tureader && python manage.py createsuperuser"
    ```
5. To import data,
    ```
    docker-compose exec web base -c "cd /code/tureader && python manage.py load res/readerlist.csv"
    ```
6. Don't forget to remove auxiliary files in `res` folder and `db.sqlite3` for testing


To stop the web service,
```
docker-compose down -v
```

---
Edited by Aj. Yo, Best, France, Pokpak, and Jay 
FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD python manage.py migrate \
    && python manage.py loaddata users/fixtures/users.json \
    && python manage.py loaddata site_blog/fixtures/post_category.json \
    && python manage.py loaddata site_blog/fixtures/posts.json \
    && python manage.py loaddata site_blog/fixtures/comments.json \
    && python manage.py makemigrations \
    && python manage.py migrate \
    && python manage.py runserver 0.0.0.0:8000
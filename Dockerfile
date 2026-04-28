FROM python:3.12

# python 한테 byte code 쓰지 말라고
ENV PYTHONDONTWRITEBYTECODE=1
# python unbuffered
ENV PYTHONUNBUFFERED=1

# 작업 디렉토리 맞추기
WORKDIR /code

COPY requirements.txt .
RUN pip install --no-cahe-dir -r requirements.txt

# 프로젝트 넣는다
COPY . .

RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "django_docker.wsgi:application", "--config", "gunicorn.conf.py"]
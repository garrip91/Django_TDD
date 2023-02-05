FROM python:3.10.6

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN wget https://raw.githubusercontent.com/vishnubob/wait-for-it/\81b1373f17855a4dc21156cfe1694c31d7d1792e/wait-for-it.sh \
    && chmod +x wait-for-it.sh

COPY requirements.txt /app/

RUN pip install -r ./requirements.txt

COPY src /app/
COPY docker /docker

FROM python:3.11-alpine

ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

RUN mkdir /var/log/gunicorn

# WORKDIR ./

ENV TZ=Europe/Kyiv
RUN set -ex \
    && apk add --no-cache --virtual .build-deps py3-cryptography py3-mysqlclient mariadb-dev build-base freetype-dev tzdata \
    && python -m venv venv \
    && /venv/bin/pip install --upgrade pip

ADD ./requirements.txt /opt/requirements.txt

RUN /venv/bin/pip install --no-cache-dir -r /opt/requirements.txt

RUN runDeps="$(scanelf --needed --nobanner --recursive /env \
        | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
        | sort -u \
        | xargs -r apk info --installed \
        | sort -u)" \
    && apk add --virtual rundeps $runDeps \
    && apk del .build-deps

# ADD ./src /app
RUN python manage.py collectstatic --no-input
RUN python manage.py migrate

EXPOSE 5000

CMD ["/venv/bin/gunicorn", "--bind", ":5000", "core.wsgi:application", "--workers", "3", "--access-logfile", "/var/log/gunicorn/prod_access.log", "--error-logfile", "/var/log/gunicorn/prod_error.log", "--log-level=debug"]


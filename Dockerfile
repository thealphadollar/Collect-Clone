FROM python:3.7-alpine3.9

MAINTAINER thealphadollar "shivam.cs.iit.kgp@gmail.com"

COPY ./ /collect-clone
WORKDIR /collect-clone

# workaround for making pylink work on alpine
RUN apk add --no-cache --update python3 gcc build-base
RUN python3 -m ensurepip
RUN pip3 install --upgrade pip

# installing pipenv and dependencies
RUN pip install pipenv
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
RUN pipenv install --dev --system --deploy

EXPOSE 8000
ENTRYPOINT [ "gunicorn" ]
CMD [ "collect-demo.wsgi:app", "--bind=0.0.0.0:8000", "--reload" ]
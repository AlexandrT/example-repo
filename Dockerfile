ARG NEXUS_HOST=nexus.comp-dev.ru
ARG PIP_TRUSTED_HOST=${NEXUS_HOST}
ARG PIP_INDEX_URL=http://${PIP_TRUSTED_HOST}/repository/pypi/simple

FROM $NEXUS_HOST/python:alpine as base
ARG PIP_TRUSTED_HOST
ARG PIP_INDEX_URL

ENV PIP_TRUSTED_HOST=${PIP_TRUSTED_HOST} PIP_INDEX_URL=${PIP_INDEX_URL}

RUN \
  apk update -q \
  && apk add -q \
  chromium \
  chromium-chromedriver

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["pytest", "tests/", "--driver", "Chrome", "--reruns", "3"]

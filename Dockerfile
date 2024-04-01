FROM python:3.11

ENV PYTHONBUFFERED 1

RUN pip install --upgrade pip
RUN pip install poetry
WORKDIR /bebl
COPY . .
RUN poetry install --without dev
RUN chmod +x /bebl/entrypoint.sh

ENTRYPOINT [ "/bebl/entrypoint.sh"]
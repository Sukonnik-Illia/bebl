FROM python:3.11

ENV PYTHONBUFFERED 1

RUN pip install --upgrade pip
RUN pip install poetry
WORKDIR /bebl
COPY . .
RUN poetry install --without dev

# it's not production ready code so we can use flask's development server
ENTRYPOINT [ "poetry",  "run", "flask", "--app", "bebl.main:create_app", "run", "--host", "0.0.0.0"]
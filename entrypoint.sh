#!/bin/bash

poetry run flask db upgrade head
poetry run flask run --host=0.0.0.0
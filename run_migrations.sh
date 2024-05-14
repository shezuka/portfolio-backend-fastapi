#!/bin/sh

poetry shell
cd portfolio_backend_fastapi
poetry run alembic upgrade head
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

WORKDIR /app/

EXPOSE 8000

# copy contents of project into docker
COPY . .

ENV POETRY_HOME="/opt/poetry"

# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python - && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

RUN ls

# install dependencies
RUN poetry install
ENV PYTHONPATH=/app
RUN pytest

CMD uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
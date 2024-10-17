# BUILDER
FROM python:3.12.6-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

RUN apt update && \
  apt install -y --no-install-recommends gcc

WORKDIR /src

COPY requirements.txt ./

COPY ./src ./src

COPY ./run_server.py ./

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 8000

# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE=1
# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1

CMD ["python", "run_server.py"]
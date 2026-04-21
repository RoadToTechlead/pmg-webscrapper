FROM mcr.microsoft.com/playwright/python:v1.49.1-noble

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DATA_PATH=/mnt/data

ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN playwright install chromium --with-deps

COPY src/ ./src/
COPY .env .

CMD ["python", "src/main.py"]
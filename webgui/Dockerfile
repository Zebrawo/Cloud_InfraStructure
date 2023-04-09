FROM alpine:latest

RUN apk add --update py3-pip python3-dev gcc libc-dev libffi-dev

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY templates/ templates/
COPY main.py .
COPY dnszone.py .
COPY mongo_functions.py .
COPY config.py .

CMD ["python", "main.py"]

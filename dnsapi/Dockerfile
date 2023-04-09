FROM alpine:latest

RUN apk add --update py3-pip python3-dev gcc libc-dev libffi-dev

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY dns_api.py .
COPY dnszone.py .

CMD ["python", "dns_api.py"]

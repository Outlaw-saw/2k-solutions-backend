FROM python:3.12-slim

WORKDIR /app/backend

RUN apt-get update && apt-get install -y --no-install-recommends libpq-dev && rm -rf /var/lib/apt/lists/*

RUN ln -s /usr/local/bin/python3 /usr/local/bin/python

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN chmod +x entrypoint.sh

EXPOSE 5000

CMD ["./entrypoint.sh"]

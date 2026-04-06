FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p data outputs/reports

ENV PYTHONUNBUFFERED=1

EXPOSE 8501

CMD ["python", "main.py", "dashboard"]

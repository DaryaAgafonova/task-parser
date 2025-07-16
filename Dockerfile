FROM python:3.11
WORKDIR /code
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY wait-for-it.sh .
RUN chmod +x wait-for-it.sh
COPY . .
CMD ["python", "-m", "app.scheduler"]

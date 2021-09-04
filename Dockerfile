FROM python:3.8
RUN pip install --no-cache-dir "uvicorn[standard]" fastapi
RUN pip install redis
RUN pip install psycopg2
RUN pip install requests
COPY ./app /app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "9898"]

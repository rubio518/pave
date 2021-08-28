FROM python:3.8
RUN pip install --no-cache-dir "uvicorn[standard]" fastapi
WORKDIR /opt
COPY app.py /opt/app.py
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "9898"]

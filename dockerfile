FROM tiangolo/uvicorn-gunicorn-fastapi

EXPOSE 80

RUN pip install pandas

COPY ./app /app

FROM tiangolo/uvicorn-gunicorn-fastapi

EXPOSE 80



COPY ./app /app


RUN pip3 install pandas


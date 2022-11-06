FROM tiangolo/uvicorn-gunicorn-fastapi

RUN pip install pandas

ENV PIP_ROOT_USER_ACTION=ignore

EXPOSE 80

COPY ./app /app
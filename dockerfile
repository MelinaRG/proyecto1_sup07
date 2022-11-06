FROM tiangolo/uvicorn-gunicorn-fastapi

ENV PIP_ROOT_USER_ACTION=ignore

RUN pip install pandas



EXPOSE 80

COPY ./app /app
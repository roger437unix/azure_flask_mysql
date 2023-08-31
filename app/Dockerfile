FROM python:3.10-rc-slim-bullseye

WORKDIR /app
COPY . .
RUN apt update
RUN apt install gcc libmariadb-dev-compat libmariadb-dev -y
RUN pip3 install -r requirements.txt
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]

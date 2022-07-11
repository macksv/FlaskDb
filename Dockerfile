FROM fnndsc/ubuntu-python3:latest

ADD . /code
WORKDIR /code

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "app.py"]

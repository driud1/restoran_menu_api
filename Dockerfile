FROM python:3.9.10-slim

WORKDIR /app

RUN apt-get update

COPY . /app

RUN pip install -r requirements.txt

# create venv

#RUN  uvicorn main:app --host 0.0.0.0 --port 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

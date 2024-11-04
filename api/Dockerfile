FROM python:3

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY *.py .
RUN chmod a+x linkextractor.py

ENTRYPOINT ["./main.py"]
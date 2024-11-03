FROM python:3

RUN pip install beautifulsoup4
RUN pip install requests
RUN pip install Flask

WORKDIR /app
COPY *.py .
RUN chmod a+x linkextractor.py

ENTRYPOINT ["./main.py"]
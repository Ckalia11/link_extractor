# Aim

A project that scrapes links from webpages

# How to Run

- Clone this repository
- Download Docker and ensure it's running
- Run `docker-compose up -d --build` from the root of the directory
- Visit `http://www.localhost:80` and enter a webpage link

# Notes

- Responses are cached using redis. You can check if a url hit the cache by checking the `api/logs` folder which will get created

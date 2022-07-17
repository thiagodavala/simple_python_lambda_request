import json
import logging
import requests

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    url = "https://jsonplaceholder.typicode.com/posts"
    body = {
                "login" : "teste",
                "password" : ""
           }
    response = requests.post(url, data=body)
    logger.info(response.status_code)
    logger.info(response.json())

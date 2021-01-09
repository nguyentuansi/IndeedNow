import logging
import sys
import http.client
import json


def setup_custom_logger(name):
    formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')
    handler = logging.FileHandler('log.txt', mode='a')
    handler.setFormatter(formatter)
    screen_handler = logging.StreamHandler(stream=sys.stdout)
    screen_handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    logger.addHandler(screen_handler)
    return logger


logger = setup_custom_logger('mysite')
logger.info('File updated!')

conn = http.client.HTTPSConnection("newscatcher.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "17b22fda86msh2dc480f3f737cdap16a605jsn15b1d0d7f2f7",
    'x-rapidapi-host': "newscatcher.p.rapidapi.com"
}

conn.request(
    "GET", "/v1/latest_headlines?topic=tech&lang=en&media=True", headers=headers)

res = conn.getresponse()

data = json.loads(res.read().decode("utf-8"))


original_stdout = sys.stdout  # Save a reference to the original standard output

with open('log.txt', 'a') as f:
    sys.stdout = f  # Change the standard output to the file we created.
    print("******************************************")
    for article in data['articles']:
        print(article["title"])
        print(article["summary"])
        print(article["link"])
        print("---------------------")
    print("******************************************")
    sys.stdout = original_stdout  # Reset the standard output to its original value

with open('README.md', 'a') as f:
    sys.stdout = f  # Change the standard output to the file we created.
    for article in data['articles']:
        print('-[{}] {}'.format(article["link"], article["title"]))
    sys.stdout = original_stdout  # Reset the standard output to its original value
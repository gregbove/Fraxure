# contains functions for interacting with tagtog API
# originally came from https://docs.tagtog.net/API_documents_v1

import requests
import os

import constants


def get_auth():
    return requests.auth.HTTPBasicAuth(
        username=os.environ["TAGTOG_USERNAME"], password=os.environ["TAGTOG_PASSWORD"]
    )


def send_plain_txt(txt: str):
    params = {
        "owner": constants.PROJECT_OWNER,
        "project": constants.TAGTOG_PROJECT_NAME,
        "format": "formatted",
        "output": "ann.json",
    }
    payload = {"text": txt}
    response = requests.post(
        constants.tagtogAPIUrl, params=params, auth=get_auth(), data=payload
    )

    print(response.text)


def import_web_page(url):
    params = {
        "owner": constants.PROJECT_OWNER,
        "project": constants.TAGTOG_PROJECT_NAME,
        "output": "weburl",
        "url": url,
    }
    response = requests.post(constants.TAGTOG_URL, params=params, auth=get_auth())
    print(response.text)


def import_file_url():
    params = {
        "owner": "yourUsername",
        "project": "yourProjectName",
        "output": "null",
        "url": "https://raw.githubusercontent.com/oxford-cs-deepnlp-2017/lectures/master/README.md",
    }
    response = requests.post(constants.TAGTOG_URL, params=params, auth=get_auth())
    print(response.text)


def import_plain_txt():
    params = {
        "owner": "yourUsername",
        "project": "yourProjectName",
        "output": "ann.json",
    }
    # you can append more files to the list in case you want to upload multiple files
    files = [("files", open("files/text.txt"))]
    response = requests.post(
        constants.TAGTOG_URL, params=params, auth=get_auth(), files=files
    )
    print(response.text)


def import_pdf():
    params = {
        "owner": "yourUsername",
        "project": "yourProjectName",
        "output": "ann.json",
    }
    # you can append more files to the list in case you want to upload multiple files
    files = [("files", open("files/document.pdf", "rb"))]
    response = requests.post(
        constants.TAGTOG_URL, params=params, auth=get_auth(), files=files
    )
    print(response.text)


def import_markdown_file():
    params = {"owner": "yourUsername", "project": "yourProjectName", "output": "null"}
    files = [("files", open("files/readme.md"))]
    response = requests.post(
        constants.TAGTOG_URL, params=params, auth=get_auth(), files=files
    )
    print(response.text)


def import_file_list():
    params = {"owner": "yourUsername", "project": "yourProjectName", "output": "null"}
    files = [
        ("files", open("files/item1.txt")),
        ("files", open("files/item2.txt")),
        ("files", open("files/item3.txt")),
    ]
    response = requests.post(
        constants.TAGTOG_URL, params=params, auth=get_auth(), files=files
    )
    print(response.text)

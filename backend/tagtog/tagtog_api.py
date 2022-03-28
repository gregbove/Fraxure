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
    auth = get_auth()
    params = {
        "owner": constants.PROJECT_OWNER,
        "project": constants.TAGTOG_PROJECT_NAME,
        "format": "formatted",
        "output": "ann.json",
    }
    payload = {"text": txt}
    response = requests.post(
        constants.tagtogAPIUrl, params=params, auth=auth, data=payload
    )

    print(response.text)


def import_web_page():
    auth = get_auth()
    params = {
        "owner": constants.PROJECT_OWNER,
        "project": constants.TAGTOG_PROJECT_NAME,
        "output": "weburl",
        "url": "https://en.wikipedia.org/wiki/Autonomous_cruise_control_system",
    }
    response = requests.post(constants.TAGTOG_API_URL, params=params, auth=auth)
    print(response.text)


def import_file_url(url: str):
    auth = get_auth()
    params = {
        "owner": constants.PROJECT_OWNER,
        "project": constants.PROJECT_NAME,
        "output": "null",
        "url": url,
    }
    response = requests.post(tagtogAPIUrl, params=params, auth=auth)
    print(response.text)


def import_plain_txt():
    auth = get_auth()
    params = {
        "owner": constants.PROJECT_OWNER,
        "project": constants.PROJECT_NAME,
        "output": "ann.json",
    }
    # you can append more files to the list in case you want to upload multiple files
    files = [("files", open("files/text.txt"))]
    response = requests.post(tagtogAPIUrl, params=params, auth=auth, files=files)
    print(response.text)


def import_pdf():
    auth = get_auth()
    params = {
        "owner": constants.PROJECT_OWNER,
        "project": constants.PROJECT_NAME,
        "output": "ann.json",
    }
    # you can append more files to the list in case you want to upload multiple files
    files = [("files", open("files/document.pdf", "rb"))]
    response = requests.post(
        constants.TAGTOG_API_URL, params=params, auth=auth, files=files
    )
    print(response.text)


def import_markdown_file(path: str):
    auth = get_auth()
    params = {
        "owner": constants.PROJECT_OWNER,
        "project": constants.PROJECT_NAME,
        "output": "null",
    }
    files = [("files", open("files/readme.md"))]
    response = requests.post(
        constants.TAGTOG_API_URL, params=params, auth=auth, files=files
    )
    print(response.text)


def import_file_list():
    auth = get_auth()
    params = {"owner": "yourUsername", "project": "yourProjectName", "output": "null"}
    files = [
        ("files", open("files/item1.txt")),
        ("files", open("files/item2.txt")),
        ("files", open("files/item3.txt")),
    ]
    response = requests.post(
        constants.TAGTOG_API_URL, params=params, auth=auth, files=files
    )
    print(response.text)

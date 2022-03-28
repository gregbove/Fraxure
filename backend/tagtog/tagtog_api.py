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
<<<<<<< HEAD
    auth = get_auth()
=======
>>>>>>> 711118700001ca79b48df7f9503c364bb9b47a4b
    params = {
        "owner": constants.PROJECT_OWNER,
        "project": constants.TAGTOG_PROJECT_NAME,
        "format": "formatted",
        "output": "ann.json",
    }
    payload = {"text": txt}
    response = requests.post(
<<<<<<< HEAD
        constants.tagtogAPIUrl, params=params, auth=auth, data=payload
=======
        constants.tagtogAPIUrl, params=params, auth=get_auth(), data=payload
>>>>>>> 711118700001ca79b48df7f9503c364bb9b47a4b
    )

    print(response.text)


<<<<<<< HEAD
def import_web_page():
    auth = get_auth()
=======
def import_web_page(url):
>>>>>>> 711118700001ca79b48df7f9503c364bb9b47a4b
    params = {
        "owner": constants.PROJECT_OWNER,
        "project": constants.TAGTOG_PROJECT_NAME,
        "output": "weburl",
<<<<<<< HEAD
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
=======
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
>>>>>>> 711118700001ca79b48df7f9503c364bb9b47a4b
    print(response.text)


def import_plain_txt():
<<<<<<< HEAD
    auth = get_auth()
    params = {
        "owner": constants.PROJECT_OWNER,
        "project": constants.PROJECT_NAME,
=======
    params = {
        "owner": "yourUsername",
        "project": "yourProjectName",
>>>>>>> 711118700001ca79b48df7f9503c364bb9b47a4b
        "output": "ann.json",
    }
    # you can append more files to the list in case you want to upload multiple files
    files = [("files", open("files/text.txt"))]
<<<<<<< HEAD
    response = requests.post(tagtogAPIUrl, params=params, auth=auth, files=files)
=======
    response = requests.post(
        constants.TAGTOG_URL, params=params, auth=get_auth(), files=files
    )
>>>>>>> 711118700001ca79b48df7f9503c364bb9b47a4b
    print(response.text)


def import_pdf():
<<<<<<< HEAD
    auth = get_auth()
    params = {
        "owner": constants.PROJECT_OWNER,
        "project": constants.PROJECT_NAME,
=======
    params = {
        "owner": "yourUsername",
        "project": "yourProjectName",
>>>>>>> 711118700001ca79b48df7f9503c364bb9b47a4b
        "output": "ann.json",
    }
    # you can append more files to the list in case you want to upload multiple files
    files = [("files", open("files/document.pdf", "rb"))]
    response = requests.post(
<<<<<<< HEAD
        constants.TAGTOG_API_URL, params=params, auth=auth, files=files
=======
        constants.TAGTOG_URL, params=params, auth=get_auth(), files=files
>>>>>>> 711118700001ca79b48df7f9503c364bb9b47a4b
    )
    print(response.text)


<<<<<<< HEAD
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
=======
def import_markdown_file():
    params = {"owner": "yourUsername", "project": "yourProjectName", "output": "null"}
    files = [("files", open("files/readme.md"))]
    response = requests.post(
        constants.TAGTOG_URL, params=params, auth=get_auth(), files=files
>>>>>>> 711118700001ca79b48df7f9503c364bb9b47a4b
    )
    print(response.text)


def import_file_list():
<<<<<<< HEAD
    auth = get_auth()
=======
>>>>>>> 711118700001ca79b48df7f9503c364bb9b47a4b
    params = {"owner": "yourUsername", "project": "yourProjectName", "output": "null"}
    files = [
        ("files", open("files/item1.txt")),
        ("files", open("files/item2.txt")),
        ("files", open("files/item3.txt")),
    ]
    response = requests.post(
<<<<<<< HEAD
        constants.TAGTOG_API_URL, params=params, auth=auth, files=files
=======
        constants.TAGTOG_URL, params=params, auth=get_auth(), files=files
>>>>>>> 711118700001ca79b48df7f9503c364bb9b47a4b
    )
    print(response.text)

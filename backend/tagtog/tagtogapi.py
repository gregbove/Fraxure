#Class for interacting with TagTog API
from pydoc import plain
import requests

class TagTogAPI:
    def __init__(self, user, passw):
        self.username = user
        self.password = passw
        self.tagtogAPIUrl = "https://www.tagtog.net/-api/documents/v1"

    #Imports Document into project by URL, need to be the owner of project at this point
    def import_by_url(self, project_name, url_link):
        auth = requests.auth.HTTPBasicAuth(username=self.username, password=self.password)
        params = {"owner": self.username, "project": project_name, "output": "null", "url": url_link}
        response = requests.post(self.tagtogAPIUrl, params=params, auth=auth)
        print(response.text)

    #Imports Document into project by plaintext, need to be owner of project at this point
    def import_by_plaintext(self, project_name, plaintext):
        auth = requests.auth.HTTPBasicAuth(username=self.username, password=self.password)
        params = {"owner": self.username, "project": project_name, "output": "ann.json"}
        payload = {"text": plaintext}
        response = requests.post(self.tagtogAPIUrl, params=params, auth=auth, data=payload)
        print(response.text)


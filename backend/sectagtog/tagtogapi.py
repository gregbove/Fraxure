#Class for interacting with TagTog API
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

    #Imports Document into project by PDF, need to be owner of project at this point
    def import_by_pdf(self, project_name, filepath):
        auth = requests.auth.HTTPBasicAuth(username=self.username, password=self.password)
        params = {"owner": self.username, "project": project_name, "output": "ann.json"}
        #you can append more files to the list in case you want to upload multiple files
        files = [("files", open(filepath, "rb"))]
        response = requests.post(self.tagtogAPIUrl, params=params, auth=auth, files=files)
        print(response.text)

    #Imports Document into project by HTML, need to be owner of project at this point
    def import_by_html(self, project_name, filepath):
        auth = requests.auth.HTTPBasicAuth(username=self.username, password=self.password)
        params = {"owner": self.username, "project": project_name, "output": "ann.json"}
        #you can append more files to the list in case you want to upload multiple files
        files = [("files", open(filepath, "rb"))]
        response = requests.post(self.tagtogAPIUrl, params=params, auth=auth, files=files)
        print(response.text) 

    #Exports a document by ID in an HTML format
    def export_by_id_html(self, project_name, id):
        auth = requests.auth.HTTPBasicAuth(username=self.username, password=self.password)
        params = {"owner": self.username, "project": project_name, 'ids':id, "output": "html"}
        response = requests.get(self.tagtogAPIUrl, params=params, auth=auth)
        if response.status_code == 200:
            with open(id + '.html', 'wb') as f:
                f.write(self.responseGet.content)
    
    
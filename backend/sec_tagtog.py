from tagtogapi import TagTogAPI
from secapi import SECAPI
import os

class SECTagTog:
    def __init__(self, user, passw, directory, proj_name):
        self.tagtog = TagTogAPI(user, passw)
        self.sec = SECAPI(directory)
        self.dir = directory
        self.project_name = proj_name
    
    #Goes from (Form Type and Ticker) --> Uploaded TagTog Document
    def mostRecent(self, form_type, company_tick):
        #Downloads the type of file
        self.sec.getMostRecent(form_type, company_tick)
        print(self.dir)
        
        #Renames the file to the Ticker + File type
        os.rename(self.dir + "/filing-details.html", self.dir+ "/" +company_tick+ "_" + form_type + ".html")

        #Adds to the TagTog Project
        self.tagtog.import_by_html(self.project_name, self.dir+ "/" + company_tick + "_" + form_type + ".html")

        #Removes the files that were downloaded
        os.remove(self.dir+ "/" + company_tick + "_" + form_type + ".html")
        os.remove(self.dir+ "/" + "full-submission.txt")


def main():
    test_api = SECTagTog('ryanmurf9', 'testapipassword123', " ", "TestProject")
    test_api.mostRecent("10-K", "CVX")

if __name__ == "__main__":
    main()
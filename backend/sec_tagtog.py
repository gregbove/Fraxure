from tagtogapi import TagTogAPI
from secapi import SECAPI
import os

class SECTagTog:
    def __init__(self, user, passw, proj_name):
        self.tagtog = TagTogAPI(user, passw)
        self.sec = SECAPI(" ")
        self.dir = " "
        self.project_name = proj_name
    
    #Goes from (Form Type and Ticker) --> Uploaded TagTog Document
    def mostRecent(self, form_type, company_tick):
        #Downloads the type of file
        self.sec.getMostRecent(form_type, company_tick)
        print(self.dir)
        
        #Renames the file to the Ticker + File type
        newPath = self.dir + "/" + company_tick + "_" + form_type + ".html"
        os.rename(self.dir + "/filing-details.html", newPath)

        #Adds to the TagTog Project
        self.tagtog.import_by_html(self.project_name, newPath)

        #Removes the files that were downloaded
        os.remove(newPath)
        os.remove(self.dir+ "/" + "full-submission.txt")

    def byYear(self, form_type, company_tick, year):
        #Downloads the correct file
        self.sec.getByYear(form_type, company_tick, year)

        #Renames it
        newPath = self.dir + "/" + company_tick + "_" + form_type + "_" + year + ".html"
        os.rename(self.dir + "/filing-details.html", newPath)

        #Adds to the TagTog Project
        self.tagtog.import_by_html(self.project_name, newPath)

        #Removes the files that were downloaded
        os.remove(newPath)
        os.remove(self.dir+ "/" + "full-submission.txt")
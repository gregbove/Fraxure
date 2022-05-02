import requests
import os, stat
from sec_edgar_downloader import Downloader

class SECAPI:
    
    #Sets directory and creates downloader object
    def __init__(self, directory): 
        self.directory = directory
        self.dl = Downloader(directory)
    
    #Downloads the most recent form
    def getMostRecent(self, form_name, company_ticker):
        self.dl.get(form_name, company_ticker, amount=1)

    #Downloads all of the forms of a certain type for a company
    def getAllForCompany(self, form_name, company_ticker):
        self.dl.get(form_name, company_ticker)

    #Downloads all of the forms of a certain type for a company
    def getAllBetween(self, form_name, company_ticker, pre, post):
        self.dl.get(form_name, company_ticker, before=post, after=pre)
        
        # self.dl.get(form_name, company_ticker, after = pre, before = post)
    
    def getAllForCompanyQuery(self, form_name, company_ticker, search_query):
        self.dl.get(form_name, company_ticker, query=search_query)


        
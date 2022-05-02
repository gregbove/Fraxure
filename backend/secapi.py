import requests
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
    
    def getAllForCompanyQuery(self, form_name, company_ticker, search_query):
        self.dl.get(form_name, company_ticker, query=search_query)
    
    def getByYear(self, form_name, company_ticker, year):
        self.dl.get(form_name, company_ticker, after= year+"-01-01", before=year+"-12-31")


        
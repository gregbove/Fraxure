#Testing Driver for the TagTog API Class
import os


from tagtogapi import TagTogAPI

def main():
    t = TagTogAPI('ryanmurf9', 'testapipassword123')

    #(WORKING) Importing by plaintext
    #t.import_by_plaintext("TestProject", "HELLO WORLD!!")

    #(NOT WORKING) Importing by url
    #t.import_by_url('TestProject', 'https://www.sec.gov/Archives/edgar/data/0000045012/000004501222000013/hal-20211231.htm')

if __name__ == "__main__":
    main()
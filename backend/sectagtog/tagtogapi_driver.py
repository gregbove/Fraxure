#Testing Driver for the TagTog API Class
import os


from tagtogapi import TagTogAPI

def main():
    # t = TagTogAPI('gregbove10', 'password123')
    x = 1
    #(WORKING) Importing by plaintext
    #t.import_by_plaintext("TestProject", "HELLO WOORLD!!")

    #(WORKING) Importing by url
    #t.import_by_url('TestProject', 'https://www.sec.gov/Archives/edgar/data/0000093410/000009341022000019/cvx-20211231.htm')
    
    #(NOT WORKING) Importing by pdf
    #t.import_by_pdf("Test Project", "/home/ryanmurf9/Downloads/test_sec.pdf")

if __name__ == "__main__":
    main()
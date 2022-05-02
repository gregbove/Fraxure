# from tagtogapi import TagTogAPI
from tagtog.tagtogapi import TagTogAPI
from .secapi import SECAPI 
import os
import spacy
import json
import requests
import os
import html2text
from bs4 import BeautifulSoup
import re



class SECTagTog:
    def __init__(self, user, passw, directory, fil, proj_name):
        self.user = user
        self.passw = passw
        self.tagtog = TagTogAPI(user, passw)
        self.sec = SECAPI(directory + fil)
        self.dir = directory
        self.fil = fil
        self.project_name = proj_name

    
    def get_class_id(self, label):
        """
        
        Translates the spaCy label id into the tagtog entity type id
        - label: spaCy label id
        
        """
        # LOCATION e_1, PERSON e_2, ORG e_3 in final code
        choices = {'PERSON': 'e_1', 'ORG': 'e_2', 'MONEY': 'e_3', 'LOCATION': 'e_4', 'LOC': 'e_5', 'GPE': 'e_6'}
        return choices.get(label, None)

    def get_entities(self, spans, pipeline):
        """
        
        Translates a tuple of named entity Span objects (https://spacy.io/api/span) into a 
        list of tagtog entities (https://docs.tagtog.net/anndoc.html#ann-json). Each entity is
        defined by the entity type ID (classId), the part name where the annotation is (part),
        the entity offsets and the confidence (annotation status, who created it and probabilty).
        - spans: the named entities in the spaCy doc
        - pipeline: trained pipeline name
        """
        default_prob = 1
        default_part_id = 's1v1'
        default_state = 'pre-added'
        tagtog_entities = []
        for span in spans:
            class_id = self.get_class_id(span.label_)
            if class_id is not None:
                tagtog_entities.append( {
                    'classId': class_id,
                    'part': default_part_id,
                    'offsets':[{'start': span.start_char, 'text': span.text}],
                    'confidence': {'state': default_state,'who': ['ml:' + pipeline],'prob': default_prob},
                    'fields':{},
                    # this is related to the kb_id (knowledge base ID) field from the Span spaCy object
                    'normalizations': {}} )
        return tagtog_entities
    

    def complicated(self, user_arg, proj_arg, cik_arg, form_arg, doc_arg, text_arg, num, auth):
        pipeline = 'en_core_web_sm' 
        nlp = spacy.load(pipeline)
        tagtogAPIUrl = "https://www.tagtog.net/-api/documents/v1" 

        # Initialize ann.json (specification: https://docs.tagtog.net/anndoc.html#ann-json)
        annjson = {}
        # Set the document as not confirmed, an annotator will manually confirm whether the annotations are correct
        annjson['anncomplete'] = False
        annjson['metas'] = {}
        annjson['relations'] = []                      
        # Transform the spaCy entities into tagtog entities
        # print("This is it: " + doc.ents)
        annjson['entities'] = self.get_entities(doc_arg.ents, pipeline)

        # Parameters for the API call 
        # see https://docs.tagtog.net/API_documents_v1.html#examples-import-pre-annotated-plain-text-file
        folder = "pool/" + cik_arg
        params = {'owner': user_arg, 'project': proj_arg, 'output': 'null', 'format': 'default-plus-annjson', 'folder': folder}
        # Pre-annotated document composed of the content and the annotations
        #files=[('doc1.txt', text2), ('doc1.ann.json', json.dumps(annjson))]
        files=[(cik_arg + "_" + form_arg + '_Section-' + str(num) + '.txt', text_arg), (cik_arg + "_" + form_arg + '_Section-' + str(num) + '.ann.json', json.dumps(annjson))]
        # POST request to send the pre-annotated document
        response = requests.post(tagtogAPIUrl, params=params, auth=auth, files=files)

    
    #Goes from (Form Type and Ticker) --> Uploaded TagTog Document
    def mostRecent(self, form_type, company_tick):
        #Downloads the type of file
        self.sec.getMostRecent(form_type, company_tick) 
        print(self.dir)
        
        #Renames the file to the Ticker + File type
        #filing-details.html

        os.rename(self.dir + "/" + self.fil, self.dir + "/" +company_tick+ "_" + form_type + ".html")

        #Adds to the TagTog Project
        self.tagtog.import_by_html(self.project_name, self.dir + "/" + company_tick + "_" + form_type + ".html")
        # os.rename(self.dir + "/" + self.fil, self.dir + "/" +company_tick+ "_" + form_type + ".html")

        # self.tagtog.export_by_id_html(self.project_name, self.dir + "/" + company_tick + "_" + form_type)
        # os.rename(self.dir + "/" +company_tick+ "_" + form_type + ".html", self.dir + "/" +company_tick+ "_" + form_type + ".txt")

        full_string = ""
        with open(self.dir+ "/" + company_tick + "_" + form_type + ".html") as f:
            for line in f:
                full_string = full_string + line
            f.close()

        # Set the credentials at tagtog and project name
        
        #MY_USERNAME = 'gregbove10'
        #MY_PASSWORD = 'password123'
        #MY_PROJECT = 'project_folder'

        MY_USERNAME = self.user
        MY_PASSWORD = self.passw
        MY_PROJECT = self.project_name

        # API authentication
        tagtogAPIUrl = "https://www.tagtog.net/-api/documents/v1"
        auth = requests.auth.HTTPBasicAuth(username=MY_USERNAME, password=MY_PASSWORD)

        # text = "Paypal Holdings Inc (PYPL) President and CEO Daniel Schulman lives at 1040 Apple Street, West Islip NY 11795 Sold $2.7 million of Shares"
        # Load the spaCy trained pipeline (https://spacy.io/models/en#en_core_web_sm) and apply it to text
        pipeline = 'en_core_web_sm' 
        nlp = spacy.load(pipeline)

        # file1 = open("test.html","r+")
        # file1 = open(self.dir+ "/" + company_tick + "_" + form_type + ".html","r+") 
        # file1 = open(company_tick + "_" + form_type + ".html","r+") 
        #text2 = file1.read(100000)
        #print("Start 1")
        #print(text2)
        #print("End 1")
        #file1.close() 

        
        full_string = ""

        item_string = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
        item_bool = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]

        with open(self.dir+ "/" + company_tick + "_" + form_type + ".html") as f: 
            for line in f: 
                if line != None and "item 1." in line.lower():
                    print("Item 1" + line + "\n")
                    # print("add to 1 " + line)
                    for i in range(0, 15):
                        item_bool[i] = False
                    item_bool[0] = True 
                if line != None and "item 2." in line.lower():
                    # print("add to 2 " + line) 
                    for i in range(0, 15):
                        item_bool[i] = False
                    item_bool[1] = True
                    # print("Changed due to " + line)
                if line != None and "item 3." in line.lower():
                    # print("Changed due to " + line) 
                    for i in range(0, 15):
                        item_bool[i] = False
                    item_bool[2] = True
                if line != None and "item 4." in line.lower(): 
                    for i in range(0, 15):
                        item_bool[i] = False
                    item_bool[3] = True
                    # print("Changed due to " + line)
                if line != None and "item 5." in line.lower(): 
                    for i in range(0, 15):
                        item_bool[i] = False
                    item_bool[4] = True
                if line != None and "item 6." in line.lower(): 
                    for i in range(0, 15):
                        item_bool[i] = False
                    item_bool[5] = True

                    # print("Changed due to " + line)
                if line != None and "item 7." in line.lower(): 
                    for i in range(0, 15):
                        item_bool[i] = False
                    item_bool[6] = True

                if line != None and "item 8." in line.lower(): 
                    for i in range(0, 15):
                        item_bool[i] = False
                    item_bool[7] = True

                    # print("Changed due to " + line)
                if line != None and "item 9." in line.lower():
                    # print("Changed due to " + line) 
                    for i in range(0, 15):
                        item_bool[i] = False
                    item_bool[8] = True

                if line != None and "item 10." in line.lower(): 
                    for i in range(0, 15):
                        item_bool[i] = False
                    item_bool[9] = True

                    # print("Changed due to " + line)
                if line != None and "item 11." in line.lower():
                    # print("Changed due to " + line) 
                    for i in range(0, 15):
                        item_bool[i] = False
                    item_bool[10] = True
                if line != None and "item 12." in line.lower(): 
                    for i in range(0, 15):
                        item_bool[i] = False
                    item_bool[11] = True
                    # print("Changed due to " + line)
                if line != None and "item 13." in line.lower(): 
                    for i in range(0, 15):
                        item_bool[i] = False
                    item_bool[12] = True
                    # print("Changed due to " + line)
                if line != None and "item 14." in line.lower():
                    # print("Changed due to " + line) 
                    for i in range(0, 15):
                        item_bool[i] = False
                    item_bool[13] = True
                if line != None and "item 15." in line.lower(): 
                    for i in range(0, 15):
                        item_bool[i] = False
                    item_bool[14] = True

                    # print("Changed due to " + line)

                for i in range(0, 15):
                    if item_bool[i]:
                        item_string[i] = item_string[i] + line
                full_string = full_string + line
            f.close()

        h = html2text.HTML2Text()
        h.ignore_links = True
        
        text = h.handle(full_string)  

        doc = nlp(text) 

        item_text = []
        for i in range(0, 15):
            item_text.append(h.handle(item_string[i]))

        docs = []
        for i in range(0, 15):
            docs.append(nlp(item_text[i]))

        # item1_doc = nlp(item1_text)

        # Initialize ann.json (specification: https://docs.tagtog.net/anndoc.html#ann-json)
        annjson = {}
        # Set the document as not confirmed, an annotator will manually confirm whether the annotations are correct
        annjson['anncomplete'] = False
        annjson['metas'] = {}
        annjson['relations'] = []                      
        # Transform the spaCy entities into tagtog entities
        # print("This is it: " + doc.ents)
        annjson['entities'] = self.get_entities(doc.ents, pipeline)

        # Parameters for the API call 
        # see https://docs.tagtog.net/API_documents_v1.html#examples-import-pre-annotated-plain-text-file
        params = {'owner': MY_USERNAME, 'project': MY_PROJECT, 'output': 'null', 'format': 'default-plus-annjson'}
        # Pre-annotated document composed of the content and the annotations
        #files=[('doc1.txt', text2), ('doc1.ann.json', json.dumps(annjson))]
        files=[(company_tick + "_" + form_type + '-labeled.txt', text), (company_tick + "_" + form_type + '-labeled.ann.json', json.dumps(annjson))]
        # POST request to send the pre-annotated document
        response = requests.post(tagtogAPIUrl, params=params, auth=auth, files=files)

        print(response.text)

        for i in range(0, 15):
            self.complicated(MY_USERNAME, MY_PROJECT, company_tick, form_type, docs[i], item_text[i], i, auth)
        
        #Removes the files that were downloaded
        os.remove(self.dir + company_tick + "_" + form_type + ".html")
        #os.remove(self.dir+ "/" + "full-submission.txt")

    # CHANGE TO YEARLY
    def allBetween(self, form_type, company_tick, pre, post):
        #Downloads the type of file
        pred = pre.split('-')
        print(pred)
        postd = post.split('-')
        print(post)
        prey = int(pred[0])
        prem = int(pred[1])
        # pred = int(pred[2])

        posty = int(postd[0])
        postm = int(postd[1])
        # postd = int(pred[2])

        year = prey
        month = prem
        # day = pred


        while year <= posty:
            month = month % 11
            while month <= 12:
        
                m = str(month)
                if month < 10:
                    m = "0" + m
        
                # predate = str(year) + "-" + m + "-" + "01"
                # postdate = str(year) + "-" + m + "-" + "31"
                m31 = [1, 3, 5, 7, 8, 10, 12]
                m30 = [4, 6, 9, 11] 

                d = "28"
                if month in m31:
                    d = "31"
                if month in m30:
                    d = "30"

                predate = str(year) + "-" + m + "-" + "01"
                postdate = str(year) + "-" + m + "-" + d 
                print("trying: " + predate + " through " + postdate)
                self.sec.getAllBetween(form_type, company_tick, predate, postdate)
                if os.path.exists(self.dir + "/" + self.fil):
                    os.rename(self.dir + "/" + self.fil, self.dir + "/" + company_tick + "_" + form_type + "_" + predate + "_" + postdate + ".html")
                    self.tagtog.import_by_html(self.project_name, self.dir + "/" + company_tick + "_" + form_type + "_" + predate + "_" + postdate + ".html")
                    # print(response.text)
                    MY_USERNAME = self.user
                    MY_PASSWORD = self.passw
                    MY_PROJECT = self.project_name

                    # API authentication
                    tagtogAPIUrl = "https://www.tagtog.net/-api/documents/v1"
                    auth = requests.auth.HTTPBasicAuth(username=MY_USERNAME, password=MY_PASSWORD)

                    # text = "Paypal Holdings Inc (PYPL) President and CEO Daniel Schulman lives at 1040 Apple Street, West Islip NY 11795 Sold $2.7 million of Shares"
                    # Load the spaCy trained pipeline (https://spacy.io/models/en#en_core_web_sm) and apply it to text
                    pipeline = 'en_core_web_sm' 
                    nlp = spacy.load(pipeline)
                    # HERE
                    full_string = ""
                    item_string = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
                    item_bool = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]


                    with open(self.dir+ "/" + company_tick + "_" + form_type + "_" + predate + "_" + postdate + ".html") as f:
                        for line in f: 
                            if line != None and "item 1." in line.lower(): 
                                for i in range(0, 15):
                                    item_bool[i] = False
                                item_bool[0] = True 

                            if line != None and ("item 2." in line.lower() or "item 2" in line.lower()):
                    # print("add to 2 " + line) 
                                for i in range(0, 15):
                                    item_bool[i] = False
                                item_bool[1] = True
                    # print("Changed due to " + line)
                            if line != None and "item 3." in line.lower():
                    # print("Changed due to " + line) 
                                for i in range(0, 15):
                                    item_bool[i] = False
                                item_bool[2] = True
                            if line != None and "item 4." in line.lower(): 
                                for i in range(0, 15):
                                    item_bool[i] = False
                                item_bool[3] = True
                    # print("Changed due to " + line)
                            if line != None and "item 5." in line.lower(): 
                                for i in range(0, 15):
                                    item_bool[i] = False
                                item_bool[4] = True
                            if line != None and "item 6." in line.lower(): 
                                for i in range(0, 15):
                                    item_bool[i] = False
                                item_bool[5] = True

                    # print("Changed due to " + line)
                            if line != None and "item 7." in line.lower(): 
                                for i in range(0, 15):
                                    item_bool[i] = False
                                item_bool[6] = True

                            if line != None and "item 8." in line.lower(): 
                                for i in range(0, 15):
                                    item_bool[i] = False
                                item_bool[7] = True

                    # print("Changed due to " + line)
                            if line != None and "item 9." in line.lower():
                    # print("Changed due to " + line) 
                                for i in range(0, 15):
                                    item_bool[i] = False
                                item_bool[8] = True

                            if line != None and "item 10." in line.lower(): 
                                for i in range(0, 15):
                                    item_bool[i] = False
                                item_bool[9] = True

                    # print("Changed due to " + line)
                            if line != None and "item 11." in line.lower():
                    # print("Changed due to " + line) 
                                for i in range(0, 15):
                                    item_bool[i] = False
                                item_bool[10] = True
                            if line != None and "item 12." in line.lower(): 
                                for i in range(0, 15):
                                    item_bool[i] = False
                                item_bool[11] = True
                    # print("Changed due to " + line)
                            if line != None and "item 13." in line.lower(): 
                                for i in range(0, 15):
                                    item_bool[i] = False
                                item_bool[12] = True
                    # print("Changed due to " + line)
                            if line != None and "item 14." in line.lower():
                    # print("Changed due to " + line) 
                                for i in range(0, 15):
                                    item_bool[i] = False
                                item_bool[13] = True
                            if line != None and "item 15." in line.lower(): 
                                for i in range(0, 15):
                                    item_bool[i] = False
                                item_bool[14] = True

                    # print("Changed due to " + line)

                            for i in range(0, 15):
                                if item_bool[i]:
                                    item_string[i] = item_string[i] + line
                            full_string = full_string + line
                        f.close()

                    h = html2text.HTML2Text()
                    h.ignore_links = True
                    text = h.handle(full_string) 
                    doc = nlp(text)


                    annjson = {}
                    # Set the document as not confirmed, an annotator will manually confirm whether the annotations are correct
                    annjson['anncomplete'] = False
                    annjson['metas'] = {}
                    annjson['relations'] = []                      
                    # Transform the spaCy entities into tagtog entities
                    # print("This is it: " + doc.ents)
                    annjson['entities'] = self.get_entities(doc.ents, pipeline)

                    # Parameters for the API call 
                    # see https://docs.tagtog.net/API_documents_v1.html#examples-import-pre-annotated-plain-text-file
                   
                    params = {'owner': MY_USERNAME, 'project': MY_PROJECT, 'output': 'null', 'format': 'default-plus-annjson'}
                    # Pre-annotated document composed of the content and the annotations
                #files=[('doc1.txt', text2), ('doc1.ann.json', json.dumps(annjson))]
                    files=[(company_tick + "_" + form_type + "_" + predate + "_" + postdate + '.txt', text), (company_tick + "_" + form_type + "_" + predate + "_" + postdate + '.txt.ann.json', json.dumps(annjson))]
                    # POST request to send the pre-annotated document
                    response = requests.post(tagtogAPIUrl, params=params, auth=auth, files=files)

                    item_text = []
                    for i in range(0, 15):
                        item_text.append(h.handle(item_string[i]))

                    docs = [] 

                    for i in range(0, 15): 
                        if len(item_text[i]) < 150:
                            if i == 0:
                                text_ = re.split("Item 1. B|ITEM 1. B|Item 1\. B|ITEM 1\. B", text)
                                if len(text_) > 1:
                                    x = re.split("Item 2. P|ITEM 2. P|Item 2\. P|ITEM 2\. P", text_[1]) 
                                    item_text[i] = "B" + x[0]

                            if i == 1:
                                text_ = re.split("Item 2. P|ITEM 2. P|Item 2\. P|ITEM 2\. P", text)
                                if len(text_) > 1:
                                    x = re.split("Item 3. L|ITEM 3. L|Item 3\. L|ITEM 3\. L", text_[1]) 
                                    item_text[i] = "P" + x[0] + "Made it to 1"
                            if i == 2:
                                text_ = re.split("Item 3. L|ITEM 3. L|Item 3\. L|ITEM 3\. L", text)
                                if len(text_) > 1:
                                    x = re.split("Item 4. M|ITEM 4. M|Item 4\. M|ITEM 4\. M", text_[1]) 
                                    item_text[i] = "L" + x[0]
                            if i == 3:
                                text_ = re.split("Item 4. M|ITEM 4. M|Item 4\. M|ITEM 4\. M", text)
                                if len(text_) > 1:
                                    x = re.split("Item 5. M|ITEM 5. M|Item 5\. M|ITEM 5\. M", text_[1]) 
                                    item_text[i] = "M" + x[0]
                            if i == 4:
                                text_ = re.split("Item 5. M|ITEM 5. M|Item 5\. M|ITEM 5\. M", text)
                                if len(text_) > 1:
                                    x = re.split("Item 6. S|ITEM 6. S|Item 6\. S|ITEM 6\. S", text_[1]) 
                                    item_text[i] = "M" + x[0]
                            if i == 5:
                                text_ = re.split("Item 6. S|ITEM 6. S|Item 6\. S|ITEM 6\. S", text)
                                if len(text_) > 1:
                                    x = re.split("Item 7. M|ITEM 7. M|Item 7\. M|ITEM 7\. M", text_[1]) 
                                    item_text[i] = "S" + x[0]
                            if i == 6:
                                text_ = re.split("Item 7. M|ITEM 7. M|Item 7\. M|ITEM 7\. M", text)
                                if len(text_) > 1:
                                    x = re.split("Item 8. F|ITEM 8. F|Item 8\. F|ITEM 8\. F", text_[1]) 
                                    item_text[i] = "M" + x[0]
                            if i == 7:
                                text_ = re.split("Item 8. F|ITEM 8. F|Item 8\. F|ITEM 8\. F", text)
                                if len(text_) > 1:
                                    x = re.split("Item 9. C|ITEM 9. C|Item 9\. C|ITEM 9\. C", text_[1]) 
                                    item_text[i] = "F" + x[0]
                            if i == 8:
                                text_ = re.split("Item 9. C|ITEM 9. C|Item 9\. C|ITEM 9\. C", text)
                                if len(text_) > 1:
                                    x = re.split("Item 10. D|ITEM 10. D|Item 10\. D|ITEM 10\. D", text_[1]) 
                                    item_text[i] = "C" + x[0]
                            if i == 9:
                                text_ = re.split("Item 10. D|ITEM 10. D|Item 10\. D|ITEM 10\. D", text)
                                if len(text_) > 1:
                                    x = re.split("Item 11. E|ITEM 11. E|Item 11\. E|ITEM 11\. E", text_[1]) 
                                    item_text[i] = "D" + x[0]
                            if i == 10:
                                text_ = re.split("Item 11. E|ITEM 11. E|Item 11\. E|ITEM 11\. E", text)
                                if len(text_) > 1:
                                    x = re.split("Item 12. S|ITEM 12. S|Item 12\. S|ITEM 12\. S", text_[1]) 
                                    item_text[i] = "E" + x[0]
                            if i == 11:
                                text_ = re.split("Item 12. S|ITEM 12. S|Item 12\. S|ITEM 12\. S", text)
                                if len(text_) > 1:
                                    x = re.split("Item 13. C|ITEM 13. C|Item 13\. C|ITEM 13\. C", text_[1]) 
                                    item_text[i] = "S" + x[0]
                            if i == 12:
                                text_ = re.split("Item 13. C|ITEM 13. C|Item 13\. C|ITEM 13\. C", text)
                                if len(text_) > 1:
                                    x = re.split("Item 14. P|ITEM 14. P|Item 14\. P|ITEM 14\. P", text_[1]) 
                                    item_text[i] = "C" + x[0]
                            if i == 13:
                                text_ = re.split("Item 14. P|ITEM 14. P|Item 14\. P|ITEM 14\. P", text)
                                if len(text_) > 1:
                                    x = re.split("Item 15. E|ITEM 15. E|Item 15\. E|ITEM 15\. E", text_[1]) 
                                    item_text[i] = "P" + x[0]
                            if i == 14:
                                text_ = re.split("Item 15. E|ITEM 15. E|Item 15\. E|ITEM 15\. E", text)
                                if len(text_) > 1: 
                                    item_text[i] = "E" + text_[1]

                    for i in range(0, 15): 
                        if len(item_text[i]) < 150:
                            if i == 0:
                                text_ = re.split("Item 1. B|ITEM 1. B|Item 1\. B|ITEM 1\. B", text)
                                if len(text_) > 2:
                                    x = re.split("Item 2. P|ITEM 2. P|Item 2\. P|ITEM 2\. P", text_[2]) 
                                    item_text[i] = "B" + x[0]

                            if i == 1:
                                text_ = re.split("Item 2. P|ITEM 2. P|Item 2\. P|ITEM 2\. P", text)
                                if len(text_) > 2:
                                    x = re.split("Item 3. L|ITEM 3. L|Item 3\. L|ITEM 3\. L", text_[2]) 
                                    item_text[i] = "P" + x[0] + "Made it to 2"
                            if i == 2:
                                text_ = re.split("Item 3. L|ITEM 3. L|Item 3\. L|ITEM 3\. L", text)
                                if len(text_) > 2:
                                    x = re.split("Item 4. M|ITEM 4. M|Item 4\. M|ITEM 4\. M", text_[2]) 
                                    item_text[i] = "L" + x[0]
                            if i == 3:
                                text_ = re.split("Item 4. M|ITEM 4. M|Item 4\. M|ITEM 4\. M", text)
                                if len(text_) > 2:
                                    x = re.split("Item 5. M|ITEM 5. M|Item 5\. M|ITEM 5\. M", text_[2]) 
                                    item_text[i] = "M" + x[0]
                            if i == 4:
                                text_ = re.split("Item 5. M|ITEM 5. M|Item 5\. M|ITEM 5\. M", text)
                                if len(text_) > 2:
                                    x = re.split("Item 6. S|ITEM 6. S|Item 6\. S|ITEM 6\. S", text_[2]) 
                                    item_text[i] = "M" + x[0]
                            if i == 5:
                                text_ = re.split("Item 6. S|ITEM 6. S|Item 6\. S|ITEM 6\. S", text)
                                if len(text_) > 2:
                                    x = re.split("Item 7. M|ITEM 7. M|Item 7\. M|ITEM 7\. M", text_[2]) 
                                    item_text[i] = "S" + x[0]
                            if i == 6:
                                text_ = re.split("Item 7. M|ITEM 7. M|Item 7\. M|ITEM 7\. M", text)
                                if len(text_) > 2:
                                    x = re.split("Item 8. F|ITEM 8. F|Item 8\. F|ITEM 8\. F", text_[2]) 
                                    item_text[i] = "M" + x[0]
                            if i == 7:
                                text_ = re.split("Item 8. F|ITEM 8. F|Item 8\. F|ITEM 8\. F", text)
                                if len(text_) > 2:
                                    x = re.split("Item 9. C|ITEM 9. C|Item 9\. C|ITEM 9\. C", text_[2]) 
                                    item_text[i] = "F" + x[0]
                            if i == 8:
                                text_ = re.split("Item 9. C|ITEM 9. C|Item 9\. C|ITEM 9\. C", text)
                                if len(text_) > 2:
                                    x = re.split("Item 10. D|ITEM 10. D|Item 10\. D|ITEM 10\. D", text_[2]) 
                                    item_text[i] = "C" + x[0]
                            if i == 9:
                                text_ = re.split("Item 10. D|ITEM 10. D|Item 10\. D|ITEM 10\. D", text)
                                if len(text_) > 2:
                                    x = re.split("Item 11. E|ITEM 11. E|Item 11\. E|ITEM 11\. E", text_[2]) 
                                    item_text[i] = "D" + x[0]
                            if i == 10:
                                text_ = re.split("Item 11. E|ITEM 11. E|Item 11\. E|ITEM 11\. E", text)
                                if len(text_) > 2:
                                    x = re.split("Item 12. S|ITEM 12. S|Item 12\. S|ITEM 12\. S", text_[2]) 
                                    item_text[i] = "E" + x[0]
                            if i == 11:
                                text_ = re.split("Item 12. S|ITEM 12. S|Item 12\. S|ITEM 12\. S", text)
                                if len(text_) > 2:
                                    x = re.split("Item 13. C|ITEM 13. C|Item 13\. C|ITEM 13\. C", text_[2]) 
                                    item_text[i] = "S" + x[0]
                            if i == 12:
                                text_ = re.split("Item 13. C|ITEM 13. C|Item 13\. C|ITEM 13\. C", text)
                                if len(text_) > 2:
                                    x = re.split("Item 14. P|ITEM 14. P|Item 14\. P|ITEM 14\. P", text_[2]) 
                                    item_text[i] = "C" + x[0]
                            if i == 13:
                                text_ = re.split("Item 14. P|ITEM 14. P|Item 14\. P|ITEM 14\. P", text)
                                if len(text_) > 2:
                                    x = re.split("Item 15. E|ITEM 15. E|Item 15\. E|ITEM 15\. E", text_[2]) 
                                    item_text[i] = "P" + x[0]
                            if i == 14:
                                text_ = re.split("Item 15. E|ITEM 15. E|Item 15\. E|ITEM 15\. E", text)
                                if len(text_) > 2: 
                                    item_text[i] = "E" + text_[2]
                    
                    
                    for i in range(0, 15):
                        if len(item_text[i]) < 5:
                            item_text[i] = "Unable to parse into sections. View 'pool' folder in order to find the section you are seeking \nINFO: " + company_tick + ", " + form_type + ", " + predate + ", " + postdate + ', Section' + str(i+1)
                        docs.append(nlp(item_text[i]))

                    for i in range(0, 15):
                    # Initialize ann.json (specification: https://docs.tagtog.net/anndoc.html#ann-json)
                        annjson = {}
                    # Set the document as not confirmed, an annotator will manually confirm whether the annotations are correct
                        annjson['anncomplete'] = False
                        annjson['metas'] = {}
                        annjson['relations'] = []                      
                    # Transform the spaCy entities into tagtog entities
                    # print("This is it: " + doc.ents)
                        annjson['entities'] = self.get_entities(docs[i].ents, pipeline)

                    # Parameters for the API call 
                    # see https://docs.tagtog.net/API_documents_v1.html#examples-import-pre-annotated-plain-text-file
                        folder = "pool/" + company_tick
                        params = {'owner': MY_USERNAME, 'project': MY_PROJECT, 'output': 'null', 'format': 'default-plus-annjson', 'folder': folder}
                    # Pre-annotated document composed of the content and the annotations
                #files=[('doc1.txt', text2), ('doc1.ann.json', json.dumps(annjson))]
                        files=[(company_tick + "_" + form_type + "_" + predate + "_" + postdate + '_Section' + str(i+1) + '.txt', item_text[i]), (company_tick + "_" + form_type + "_" + predate + "_" + postdate + '_Section' + str(i+1) + '.txt.ann.json', json.dumps(annjson))]
                    # POST request to send the pre-annotated document
                        response = requests.post(tagtogAPIUrl, params=params, auth=auth, files=files)
                    # HERE

                month = month + 1
            year = year + 1  


def main(): 
    test_api = SECTagTog('gregbove10', 'password123', "", "project_folder")
    test_api.mostRecent("10-K", "CVX")

if __name__ == "__main__":
    main()
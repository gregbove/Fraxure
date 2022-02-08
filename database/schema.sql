

-- contains header information of the document
-- document sections referece the document entry and contain the actual text
-- a document being present doesnt guarentee its sections are present
DROP TABLE IF EXISTS DocumentHeader;
CREATE TABLE DocumentHeader (
    DocumentID INT PRIMARY KEY,
    FilingYear INT,
    CommissionFileNumber INT,
    EntityName VARCHAR(128),
    State CHAR(2),
    IRSEmployerID INT,
    Address VARCHAR(128),
    ZipCode INT
);

-- references the document header it belongs to
-- contains the section name and the document text
-- also contains tags like viewed, NER labelled, human approved
DROP TABLE IF EXISTS DocumentSection;
CREATE TABLE DocumentSection (
    DocumentID INT,
    SectionName TEXT(16),
    SectionText TEXT(1024)
);

-- references a document section, and specifically a set of words within the section
-- associates a tag with the words
DROP TABLE IF EXISTS EntityLabel;
CREATE TABLE EntityLabel (
    
);


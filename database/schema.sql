CREATE TABLE Document (
    DocumentID INT PRIMARY KEY,
    FilingYear INT,
    CommissionFileNumber INT,
    EntityName VARCHAR(128),
    State CHAR(2),
    IRSEmployerID INT,
    Address VARCHAR(128),
    ZipCode INT
);

CREATE TABLE DocumentSection (
    DocumentID INT,
    SectionName VARCHAR(16),
    SectionText VARCHAR(1024)
);

CREATE TABLE EntityLabel (
    
);

CREATE TABLE Jobs (
    
);
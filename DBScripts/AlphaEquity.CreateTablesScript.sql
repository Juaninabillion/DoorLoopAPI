
use AlphaEquity

CREATE TABLE Units (
    UnitId  nvarchar(100) PRIMARY KEY,
    UnitName NVARCHAR(255),
    UnitAddress NVARCHAR(255),
    PropertyID NVARCHAR(100),
    Status NVARCHAR(50),
    Description NVARCHAR(MAX)
);
CREATE INDEX IDX_Unit_ID ON Units (UnitId);

CREATE TABLE Leases (
    LeaseNumber NVARCHAR(100) PRIMARY KEY,
    PropertyNumber NVARCHAR(100) NOT NULL,
    StartDate DATE NOT NULL,
    EndDate DATE NOT NULL,
    Status NVARCHAR(50),
    LeaseType NVARCHAR(100)
);

CREATE INDEX IDX_Leases_PropertyNumber ON Leases (PropertyNumber);
CREATE INDEX IDX_Leases_Start_End_Date ON Leases (StartDate, EndDate);


CREATE TABLE Properties (
    PropertyID NVARCHAR(100) PRIMARY KEY,
    PropertyClass NVARCHAR(100),
    PropertyType NVARCHAR(100),
    PropertyName NVARCHAR(255)
);
CREATE INDEX IDX_Properties_Class ON Properties (PropertyClass);
CREATE INDEX IDX_Properties_Type ON Properties (PropertyType);

create table files 
(
	fileID  NVARCHAR(100) not null PRIMARY KEY,
	fileResourceID NVARCHAR(100),
	fileName NVARCHAR(MAX),
	unitID NVARCHAR(100),
	propertyID NVARCHAR(100)
)
create index IDX_Files_FileID on Files (fileid) 

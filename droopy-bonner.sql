PRAGMA foreign_keys = ON;

CREATE TABLE Employee (
  SSN TEXT NOT NULL,
  Birthdate REAL NOT NULL,
  First_Name TEXT NOT NULL,
  Last_Name TEXT NOT NULL,
  Salary REAL NOT NULL,
  Super_SSN TEXT,
  Storefront_ID INTEGER,
  Depot_ID INTEGER,
  Spaceship_ID INTEGER,

  PRIMARY KEY (SSN),
  FOREIGN KEY(Super_SSN) REFERENCES Employee(SSN),
  FOREIGN KEY(Spaceship_ID) REFERENCES Spaceship(ID),
  FOREIGN KEY(Storefront_ID) REFERENCES Storefront(ID),
  FOREIGN KEY(Depot_ID) REFERENCES Depot(ID),
  FOREIGN KEY(Spaceship_ID) REFERENCES Spaceship(ID)
);

CREATE TABLE Spaceship (
  ID INTEGER NOT NULL,
  Employee_ID INTEGER NOT NULL,
  Volume REAL NOT NULL,
  Class TEXT NOT NULL,
  Current_Coord_x REAL NOT NULL,
  Current_Coord_y REAL NOT NULL,
  Current_Coord_z REAL NOT NULL,
  Dest_PBID INTEGER,
  Dest_Address TEXT,

  PRIMARY KEY (ID),
  FOREIGN KEY (Employee_ID) REFERENCES Employee(ID),
  FOREIGN KEY(Dest_PBID, Dest_Address) REFERENCES Location(PBID, Address)
);

CREATE TABLE HoverTruck (
  ID INTEGER NOT NULL,
  Volume REAL NOT NULL,
  Current_Coord_x REAL NOT NULL,
  Current_Coord_y REAL NOT NULL,
  Current_Coord_z REAL NOT NULL,
  Dest_PBID INTEGER,
  Dest_Address TEXT,

  PRIMARY KEY (ID),
  FOREIGN KEY(Dest_PBID, Dest_Address) REFERENCES Location(PBID, Address)
);

CREATE TABLE Spacesuit (
  ID INTEGER NOT NULL,
  Size TEXT NOT NULL,
  Model TEXT NOT NULL,

  PRIMARY KEY (ID)
);

CREATE TABLE Spacesuit_Employees (
  Spacesuit_ID INTEGER NOT NULL,
  Employee_ID INTEGER NOT NULL,

  FOREIGN KEY (Spacesuit_ID) REFERENCES Spacesuit(ID),
  FOREIGN KEY (Employee_ID) REFERENCES Employee(ID)
);

CREATE TABLE Shipper (
  ID INTEGER NOT NULL,
  First_Name TEXT NOT NULL,
  Last_Name TEXT NOT NULL,
  Location_PBID INTEGER NOT NULL,
  Location_Address TEXT NOT NULL,

  PRIMARY KEY (ID),
  FOREIGN KEY(Location_PBID, Location_Address) REFERENCES Location(PBID, Address)
);

CREATE TABLE Recipient (
  ID INTEGER NOT NULL,
  First_Name TEXT NOT NULL,
  Last_Name TEXT NOT NULL,
  Location_PBID INTEGER NOT NULL,
  Location_Address TEXT NOT NULL,

  PRIMARY KEY (ID),
  FOREIGN KEY(Location_PBID, Location_Address) REFERENCES Location(PBID, Address)
);

CREATE TABLE Storefront (
  ID INTEGER NOT NULL,
  Name TEXT NOT NULL,
  Location_PBID INTEGER NOT NULL,
  Location_Address TEXT NOT NULL,

  PRIMARY KEY (ID),
  FOREIGN KEY(Location_PBID, Location_Address) REFERENCES Location(PBID, Address)
);

CREATE TABLE Depot (
  ID INTEGER NOT NULL,
  Name TEXT NOT NULL,
  Location_PBID INTEGER NOT NULL,
  Location_Address TEXT NOT NULL,

  PRIMARY KEY (ID)
);


CREATE TABLE PlanetaryBody (
  ID INTEGER NOT NULL,
  Coord_x REAL NOT NULL,
  Coord_y REAL NOT NULL,
  Coord_z REAL NOT NULL,

  PRIMARY KEY (ID)
);

CREATE TABLE PlanetaryBodyAtmosphere (
  PBID INTEGER NOT NULL,
  Atmosphere TEXT NOT NULL,

  FOREIGN KEY (PBID) REFERENCES PlanetaryBody(ID)
);

CREATE TABLE Location (
  PBID INTEGER NOT NULL,
  Address TEXT NOT NULL,

  FOREIGN KEY (PBID) REFERENCES PlanetaryBody(ID)
);

CREATE TABLE Package (
  ID INTEGER NOT NULL,
  Width REAL NOT NULL,
  Height REAL NOT NULL,
  Depth REAL NOT NULL,
  Mass REAL NOT NULL,
  Spaceship_ID INTEGER,
  Hovertruck_ID INTEGER,
  Storefront_ID INTEGER,
  Depot_ID INTEGER,
  Recipient_ID INTEGER NOT NULL,
  Shipper_ID INTEGER NOT NULL,

  PRIMARY KEY (ID),
  FOREIGN KEY(Spaceship_ID) REFERENCES Spaceship(ID),
  FOREIGN KEY(Storefront_ID) REFERENCES Storefront(ID),
  FOREIGN KEY(Hovertruck_ID) REFERENCES Hovertruck(ID),
  FOREIGN KEY(Depot_ID) REFERENCES Depot(ID),
  FOREIGN KEY(Recipient_ID) REFERENCES Recipient(ID),
  FOREIGN KEY(Shipper_ID) REFERENCES Shipper(ID)
);

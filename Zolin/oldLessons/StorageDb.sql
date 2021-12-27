CREATE TABLE Good (
	Id integer PRIMARY KEY AUTOINCREMENT,
	Name string,
	ManufacturerId integer PRIMARY KEY AUTOINCREMENT,
	Price float
);

CREATE TABLE Storage (
	Count integer,
	Id integer PRIMARY KEY AUTOINCREMENT
);

CREATE TABLE Manufacturer (
	ManufacturerId integer PRIMARY KEY AUTOINCREMENT,
	PrName string,
	Country string
);

CREATE TABLE Size (
	Id integer PRIMARY KEY AUTOINCREMENT,
	Size float
);






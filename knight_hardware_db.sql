CREATE TABLE Customers (	/*Creates Customer table */
  CustomerID   INT   IDENTITY   PRIMARY KEY,
  CustomerName    VARCHAR(255)   NOT NULL,
  City            VARCHAR(60)    NOT NULL,
  State           VARCHAR(60)    NOT NULL
);

CREATE TABLE Parts (	/*Creates Parts table */
  PartID				INT   IDENTITY   PRIMARY KEY,
  PartCode				VARCHAR(30)  NOT NULL,
  PartDescription       VARCHAR(255)   NOT NULL,
  InventoryOnHand       INT    NOT NULL,
  Price			MONEY	       NOT NULL
);

CREATE TABLE Orders (	/*Creates Orders table */
  OrderID		INT   IDENTITY   PRIMARY KEY,
  CustomerID	INT   NOT NULL,
  OrderDate		DATETIME2	NOT NULL,
  CONSTRAINT FK_OrdersCustomers FOREIGN KEY (CustomerID) REFERENCES Customers (CustomerID)
);

CREATE TABLE OrderDetails (		/*Creates OrdersDetails table */
  OrderID			INT   NOT NULL,
  PartID			INT   NOT NULL,
  NumberOrdered     INT	  NOT NULL,
  CONSTRAINT PK_OrderDetails PRIMARY KEY (OrderID, PartID),
  CONSTRAINT FK_OrderDetailsOrders FOREIGN KEY (OrderID) REFERENCES Orders (OrderID),
  CONSTRAINT FK_OrderDetailsParts FOREIGN KEY (PartID) REFERENCES Parts (PartID)
);

/* Insert values/data into the tables */
INSERT INTO Customers VALUES
('Al''s Appliance and Sport', 'Fillmore', 'FL'),
('Brookings Direct', 'Grove', 'FL'),
('Ferguson''s', 'Northfield', 'FL'), 
('The Everything Shop', 'Crystal', 'FL'),
('Johnson''s Department Store', 'Sheldon', 'FL');

INSERT INTO Parts VALUES
('AT94', 'Iron', 50, 24.95),
('DR93', 'Gas Range', 8, 495),
('KT03', 'Dishwasher', 8, 595),
('DW11', 'Washer', 12, 399.99),
('KL62', 'Dryer', 12, 349.99),
('BV06', 'Home Gym', 45, 794.95),
('CD52', 'Microwave Oven', 32, 165),
('KV29', 'Treadmill', 9, 1390);

INSERT INTO Orders VALUES
(1, '2017-10-20 12:45:30'),
(3, '2017-10-19 12:45:30'),
(4, '2017-10-22 12:45:30'),
(2, '2017-10-21 12:45:30'),
(5, '2017-10-23 12:45:30'),
(1, '2017-10-23 12:45:30'),
(5, '2017-10-21 12:45:30');

SET IDENTITY_INSERT Orders OFF; /* Turns off identity insert */

INSERT INTO OrderDetails VALUES
(1, 1, 11),
(2, 2, 1),
(2, 4, 1),
(3, 5, 4),
(4, 3, 4),
(5, 6, 4),
(5, 7, 4),
(6, 2, 4),
(7, 8, 4);

/* Drops table if needed */
DROP TABLE OrderDetails;
DROP TABLE Orders;
DROP TABLE Customers;
DROP TABLE Parts;
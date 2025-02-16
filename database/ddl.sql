SET FOREIGN_KEY_CHECKS = 0
DROP TABLE IF EXISTS Users, TimeSheets, LineItems

CREATE TABLE Users(
    userID int AUTO_INCREMENT NOT NULL UNIQUE,
    username VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    PRIMARY KEY (userID)
);

CREATE TABLE TimeSheets(
    sheetID int AUTO_INCREMENT NOT NULL UNIQUE,
    lineItem int NOT NULL,
    rate DECIMAL(3, 1),
    description VARCHAR(255),
    PRIMARY KEY (sheetID),
    FOREIGN KEY (lineItem) REFERENCES LineItems(itemID)
);

CREATE TABLE LineItems(
    itemID into AUTO_INCREMENT NOT NULL UNIQUE,
    sheetID int NOT NULL,
    date DATE NOT NULL,
    hours DECIMAL(3, 1),
    PRIMARY KEY (itemID),
    FOREIGN KEY (sheetID) REFERENCES TimeSheets(sheetID) ON DELETE CASCADE
)
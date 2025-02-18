SET FOREIGN_KEY_CHECKS = 0;
DROP TABLE IF EXISTS TimeSheets;

CREATE TABLE TimeSheets(
    sheetID INT AUTO_INCREMENT NOT NULL UNIQUE,
    rate DECIMAL(5, 2),
    description VARCHAR(255),
    lineItems JSON,
    PRIMARY KEY (sheetID)
);

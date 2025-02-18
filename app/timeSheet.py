class TimeSheet:
    def getSheets(self, db: object) -> dict:
        """
        Takes in a database object returning a list
        containing all the currently saved time sheets.
        """
        query = "SELECT * FROM TimeSheets"
        res = db.executeQuery(query, [])
        return res

    def createSheet(self, db: object) -> bool:
        """
        Takes in a database object returning True if the sheet
        creation was successful and False otherwise.
        """
        query = "INSERT INTO TimeSheets(rate, description, lineItems) VALUES\
                (NULL, NULL, NULL)"
        res = db.executeQuery(query, [])
        return True if res else False

    def saveSheet(self, db: object, rate: float,
                  description: str, lineItems: dict, sheetID: int) -> bool:
        """
        Takes in the database object, rate, description, line items, and sheet
        ID to save changes to a specific sheet. Returns True if successful and
        False otherwise.
        """
        query = "UPDATE TimeSheets SET rate = %s, description = %s,\
                lineItems = %s WHERE sheetID = %s"
        params = [rate, description, lineItems, sheetID]
        res = db.executeQuery(query, params)
        return True if res else False

    def deleteSheet(self, db: object, sheetID: int) -> bool:
        """
        Takes in a database object and sheet ID to delete a sheet returning
        True if successful and False otherwise
        """
        query = "DELETE FROM TimeSheets WHERE sheetID = %s"
        params = [sheetID]
        res = db.executeQuery(query, params)
        return True if res else False

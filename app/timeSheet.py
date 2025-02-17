class TimeSheet:
    def getSheets(self, db: object, userID: int) -> dict:
        """
        Takes in a database object and returns a dictionary containing
        all the time sheets for a specific user.
        """
        query = "SELECT * FROM TimeSheets WHERE userID = %s;"
        params = [userID]
        res = db.executeQuery(query, params)
        return res

    def createSheet(self, db: object, userID: int) -> bool:
        """
        """
        query = "INSERT INTO TimeSheets(userID) VALUES \
                ((SELECT userID FROM Users WHERE userID = %s))"
        params = [userID]
        res = db.executeQuery(query, params)
        return True if res else False

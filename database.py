import mysql.connector

from mysql.connector import errorcode


class Database:
    def __init__(self, config: object) -> None:
        self._config = {
            "user": config.db_user,
            "password": config.db_password,
            "database": config.db_name,
            "host": config.db_host
        }

    def executeQuery(self, query: str, params: list) -> list:
        """
        This function accepts a SQL query and a list of parameters returning
        the result of the query in the list or an empty list if the query was
        unsuccessful.
        """
        data = []
        cnx = None
        try:
            # setup connection and execute query
            cnx = mysql.connector.connect(**self._config)
            print("connection successful")
            cursor = cnx.cursor()
            cursor.execute(query, params)

            if query.startswith(("INSERT", "UPDATE", "DELETE")):
                cnx.commit()
                data = ["success", cursor.lastrowid]
                print("Transaction committed")
            else:
                data = cursor.fetchall()

        # error handling
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

        # close connection
        finally:
            if cnx:
                cnx.close()

        return data

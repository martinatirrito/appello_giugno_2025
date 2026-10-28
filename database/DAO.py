from database.DB_connect import DBConnect


class DAO():
    @staticmethod
    def getAllCircuits():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT * 
                    from circuits"""
        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(row)

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getAllYears():
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = "SELECT distinct year FROM seasons s  ORDER BY year"

        cursor.execute(query)

        for row in cursor:
            results.append(row["year"])

        cursor.close()
        conn.close()
        return results

    @staticmethod
    def getAllNodes(year1, year2):

        conn = DBConnect.get_connection()
        if conn is None:
            print("Errore di connessione al database")
            return []
        cursor = conn.cursor(dictionary=True)

        result = []

        query = """"""

        cursor.execute(query, (year1, year2,))

        for row in cursor:
            result.append(Constructor(**row))

        cursor.close()
        conn.close()
        return result
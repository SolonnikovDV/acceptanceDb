import sqlite3
from sqlite3 import Error
from sqlalchemy import create_engine
import pandas as pd

# importing data from excel file to sqlite

class ImportDataToDb:
    @classmethod
    def importDataFromExcel(cls, file, db_path, db_table_name):
        df = pd.read_excel(file)
        engine = create_engine(db_path)
        df.to_sql(db_table_name, con=engine, if_exists='replace', index=False)

    @classmethod
    def insertVaribleIntoTable(
            cls,
            acceptDate,
            owner,
            contractDate,
            costOfContraact):
        try:
            sqlite_connection = sqlite3.connect('myDb.db')
            cursor = sqlite_connection.cursor()
            print("Connected to SQLite")

            sqlite_insert_with_param = """INSERT INTO acceptance
                          (
                          'Дата извещения о проведении приемки', 
                          'Владелец договора', 
                          '№ договора, дата', 
                          'Сумма договора, руб. с НДС'
                          ) 
                          VALUES (?, ?, ?, ?);"""

            data_tuple = (acceptDate, owner, contractDate, costOfContraact)
            cursor.execute(sqlite_insert_with_param, data_tuple)
            sqlite_connection.commit()
            print("Python Variables inserted successfully into SqliteDb_developers table")

            cursor.close()

        except sqlite3.Error as error:
            print("Failed to insert Python variable into sqlite table", error)
        finally:
            if sqlite_connection:
                sqlite_connection.close()
                print("The SQLite connection is closed")
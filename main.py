import import_data_to_db as data
from main_window import MainWindow

file = 'AcceptanceOfGoods.xls'
db_path = 'sqlite:///myDb.db'
db_table_name = 'acceptance'

# create db and import excel file data to db
# data.ImportDataToDb.importDataFromExcel(file, db_path, db_table_name)

# insert data rows to db
# data.ImportDataToDb.insertVaribleIntoTable('2222-02-22', 'Онотоле', '№ 15 от 2020-02-20', 15000000.15)
# data.ImportDataToDb.insertVaribleIntoTable('2222-02-22', 'ФЕДРИЗЕНКО', '№ 15 от 2020-02-20', 15000000.15)

main_window = MainWindow(600, 400, 200, 200, 'Main Window')
main_window.run()
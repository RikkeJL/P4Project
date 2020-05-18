import xlsxwriter

data_storage = []
data_storage1 = []
data_storage2 = []
data_storage3 = []


def write_to_sheet():
    workbook = xlsxwriter.Workbook('DataCollection.xlsx')
    worksheet_network = workbook.add_worksheet('Data.xlsx')

    row = 1
    column = 0

    for item in data_storage:
        worksheet_network.write('A1', 'Frequency Change Data')
        worksheet_network.write(row, column, item)
        row += 1

    row = 1
    column = 1

    for item in data_storage1:
        worksheet_network.write('B1', 'Echo Data')
        worksheet_network.write(row, column, item)
        row += 1

    row = 1
    column = 2

    for item in data_storage2:
        worksheet_network.write('C1', 'Vibrato Data')
        worksheet_network.write(row, column, item)
        row += 1

    row = 1
    column = 3

    for item in data_storage3:
        worksheet_network.write('D1', 'Chorus Data')
        worksheet_network.write(row, column, item)
        row += 1

    workbook.close()

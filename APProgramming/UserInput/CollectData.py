import xlsxwriter

# Four arrays for storing the data collected from the program as it runs. Currently they are empty.
data_storage = []
data_storage1 = []
data_storage2 = []
data_storage3 = []


def write_to_sheet():
    workbook = xlsxwriter.Workbook('DataCollection.xlsx')  # Creates an Excel Workbook
    worksheet_network = workbook.add_worksheet('Data.xlsx')  # Creates a worksheet within the workbook

    row = 1  # Sets the starting row
    column = 0  # Sets the starting column

    for item in data_storage:  # For all items in data_storage
        worksheet_network.write('A1', 'Frequency Change Data')  # First write this in the first row and column
        worksheet_network.write(row, column, item)  # Writes the item stored in the array in the current row/column
        row += 1  # moves the row written on one down

    # Moves the column one over and resets row.
    row = 1
    column = 1

    # Code below repeats above code's procedure.
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

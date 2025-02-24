import csv

def read_specific_columns(filename, columns):
    with open(filename, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            selected_columns = [row[i] for i in columns]
            print(selected_columns)

csv_filename = "data.csv"
columns_to_read = [0, 2]
read_specific_columns(csv_filename, columns_to_read)

data.csv
Name, Age, City
John, 28, New York
Anna, 22, London
Peter, 34, Berlin
Maria, 25, Madrid
David, 30, Paris

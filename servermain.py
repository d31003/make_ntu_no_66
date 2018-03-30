import iot_download
import readfile
import csv

def create_csv(csv_file_name):
    with open("csv_file_name", "w") as my_empty_csv:
        pass

def add_csv(csv_string):
    with open(r'csvfile.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(csv_string)

create_csv()
csv_list=[]
csv_list=readfile.read("json format.txt")

add_csv(csv_list)
from io import RawIOBase
from os import read
from PyInquirer import prompt
import csv

def in_list(user, list):
    for i in list:
        if (user == i[0]):
            return True
    return False

def show_status():
    value = []
    with open('expense_report.csv', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            nb_users = len(row) - 3
            if (nb_users > 0):
                for i in range (nb_users):
                    user = row[3 + i]
                    if (not in_list(user, value)):
                        value.append([user, int(row[0])/(nb_users + 1)])
                    else:
                        for l in value:
                            if (user == l[0]):
                                l[1] += int(row[0])/(nb_users + 1)
            if (not in_list(row[2], value)):
                value.append([row[2], 0])
    for i in value:
        print(i[0] + " owes " + str(i[1]))
    return True
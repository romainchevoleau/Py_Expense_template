from PyInquirer import prompt
import csv

user_questions = [
    {
        "type":"input",
        "name":"Name",
        "message":"User name: ",
        
    }
]

def add_user():
    user = prompt(user_questions)
    with open('users.csv', 'a', newline='') as file:
        # create the csv writer
        writer = csv.DictWriter(file, fieldnames=user)
        # write a row to the csv file
        writer.writerow(user)
    return True

def get_user():
    users = []
    with open('users.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            users.append(row[0])
    return users
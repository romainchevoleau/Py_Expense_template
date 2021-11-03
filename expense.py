from PyInquirer import prompt
import csv
from user import get_user

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"list",
        "name":"spender",
        "message":"New Expense - Spender: ",
        "choices": get_user()
    }
]

involved_user = [
    {
        "type":"list",
        "name":"involved",
        "message":"Involved user: ",
        "choices": get_user()
    }
]

involved_question = [
    {
        "type":"confirm",
        "name":"involved_boolean",
        "message":"More involved users ?"
    }
]

def new_expense(*args):
    infos = prompt(expense_questions)
    question = prompt(involved_question)

    content = []
    content.append(infos['amount'])
    content.append(infos['label'])
    content.append(infos['spender'])

    while(question['involved_boolean']):
        user = prompt(involved_user)
        content.append(user['involved'])
        question = prompt(involved_question)

    with open('expense_report.csv', 'a', newline='') as file:
        # create the csv writer
        writer = csv.writer(file)
        # write a row to the csv file
        writer.writerow(content)

    print("Expense Added !")
    return True
from PyInquirer import prompt
from examples import custom_style_2
from user import add_user
from expense import expense_questions,new_expense
from status import show_status

def ask_option():
    main_option = {
        "type":"list",
        "name":"main_options",
        "message":"Expense Tracker v1",
        "choices": ["New Expense","Show Status","New User", "Exit"]
    }
    option = prompt(main_option)
    if (option['main_options']) == "New Expense":
        new_expense()
        ask_option()
    elif (option['main_options']) == "Show Status":
        show_status()
        ask_option()
    elif (option['main_options']) == "New User":
        add_user()
        ask_option()

def main():
    ask_option()

main()
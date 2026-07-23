import json
import datetime

try:
    with open('habits.json','r') as rfile:
        habitdata = json.load(rfile)
except FileNotFoundError:
    habitdata = {}

print('Habit Tracker')

while True:
    user_input = input('Enter command: ')

    inputsplit = user_input.split()
    command = inputsplit[0]

    if command.lower() == 'add':
        if len(inputsplit) == 2:
            habit_name = inputsplit[1]
        if habit_name not in habitdata:
            habitdata[habit_name] = []
        else:
            print("Habit already added!")
    elif command.lower() == 'done':
        if len(inputsplit) == 2:
            habit_name = inputsplit[1]
        if habit_name in habitdata:
            habitdata[habit_name].append(str(datetime.date.today()))
        else:
            print("Habit not found. Add it first")
    elif command.lower() == 'list':
        if not habitdata:
            print("List is empty. Add some habits!")
        else:
            print(f"{'Habit':<15}{'Times Done':<12}{'Last Done':<12}")
            print('-' * 39)

            for key, value in habitdata.items():
                #print(f"Habit Name: {key} | Date Completed: {value}")
                if not value:
                    print(f"{key:<15}{'0':<12}{'Never':<12}")
                else:
                    print(f"{key:<15}{len(value):<12}{value[-1]:<12}")
    elif command.lower() == 'exit':
        print("Exiting loop..")
        break

with open('habits.json','w') as wfile:
    json.dump(habitdata,wfile)
import json

try:
    with open('habits.json','r') as rfile:
        habitdata = json.load(rfile)
except FileNotFoundError:
    habitdata = []

print('Habit Tracker')

user_input = input('Enter a habit, format -- add <habit>: ')

inputsplit = user_input.split()

if inputsplit[0] == 'add':
    habitdata.append(inputsplit[1])

with open('habits.json','w') as wfile:
    json.dump(habitdata,wfile)

print("Habits: ", habitdata)
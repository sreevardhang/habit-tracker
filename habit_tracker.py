import json
import datetime

try:
    with open('habits.json','r') as rfile:
        habitdata = json.load(rfile)
except FileNotFoundError:
    habitdata = {}

print('\nHabit Tracker\n')
print("List of available commands: add, done, list, exit")
print("Format: add/done <habit name>")
print("list/exit are single word commands\n")

def calculate_streak(date_strings):
    if not date_strings:
        return 0
    
    # Step 1: convert strings to date objects
    date_objects = []
    for d in date_strings:
        date_objects.append(datetime.date.fromisoformat(d)) # your conversion here
        pass
    
    # Step 2: remove duplicates, sort oldest -> newest
    unique_sorted_dates = sorted(set(date_objects))  # your code here
    
    # Step 3: walk backward from the end, count consecutive days
    streak = 1  # the most recent date always counts as day 1 of the streak
    
    for i in range(len(unique_sorted_dates) -1, 0, -1):
        duration = unique_sorted_dates[i] - unique_sorted_dates[i-1]
        if duration.days == 1:
            streak += 1
        else:
            break
    
    return streak

while True:
    user_input = input('Enter command: \n')

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
            print(f"{'Habit':<15}{'Times Done':<12}{'Streak':<12}{'Last Done':<12}")
            print('-' * 50)

            for key, value in habitdata.items():
                #print(f"Habit Name: {key} | Date Completed: {value}")
                if not value:
                    print(f"{key:<15}{'0':<12}{'0':<12}{'Never':<12}")
                else:
                    print(f"{key:<15}{len(value):<12}{calculate_streak(value):<12}{value[-1]:<12}")
    elif command.lower() == 'exit':
        print("Exiting loop..")
        break

with open('habits.json','w') as wfile:
    json.dump(habitdata,wfile)
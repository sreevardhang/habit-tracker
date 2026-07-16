
habits = []

print('Habit Tracker')

user_input = input('Enter a habit, format -- add <habit>: ')

inputsplit = user_input.split()

if inputsplit[0] == 'add':
    habits.append(inputsplit[1])

print("Habits: ", habits)
from datetime import datetime
import pandas as p
import django

user_input = input("Enter your goal with a deadline separated by colon: ")
input_list = user_input.split(":")
goal = input_list[0]
deadline = input_list[1]
deadline_converted = datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.today()
time_till = deadline_converted - today_date

print(f"Your goal is {goal} and deadline is {time_till.days}")
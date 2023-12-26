calculation_to_units = 24
name_of_unit = "hours"


def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"


def validate_and_execute():
    if value_entered.isdigit():
        user_input_given = int(value_entered)
        if user_input_given > 0:
            my_var = days_to_units(int(user_input_given))
            print(my_var)
        elif user_input_given == 0:
            print("you entered zero")
    else:
        print("please enter a valid input")


user_input = ""
while user_input != "exit":
    user_input = input("Please enter a valid number: ")

    for value_entered in user_input.split(","):
        validate_and_execute()
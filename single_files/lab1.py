calculation_to_units = 24
name_of_unit = "hours"


def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"


def validate_and_execute():
    if user_input.isdigit():
        user_input_given = int(user_input)
        if user_input_given > 0:
            my_var = days_to_units(int(user_input_given))
            print(my_var)
        elif user_input_given == 0:
            print("you entered zero")
    else:
        print("please enter a valid input")


user_input = input("Enter a value for number of days\n")
validate_and_execute()
print(type("This is a string"))
print(type(3))
print(type(23.23))
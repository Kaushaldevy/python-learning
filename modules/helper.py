calculation_to_units = {"hours": 24, "days": 1}
name_of_unit = {"hours": "hours", "days": "days"}


def days_to_units(num_of_days, unit):
    try:
        return f"{num_of_days} days are {num_of_days * calculation_to_units[unit]} {name_of_unit[unit]}"
    except ValueError:
        print("unsupported units")


def validate_and_execute(days_and_units_dictionary):
    try:
        value_entered = int(days_and_units_dictionary["days"])
        if value_entered > 0:
            my_var = days_to_units(value_entered, days_and_units_dictionary["unit"])
            print(my_var)
        elif value_entered == 0:
            print("you entered zero")
        else:
            print("please enter a non-negative value")
    except ValueError:
        print("please enter a valid input")


user_input_message = "Please enter a valid number and a conversion unit: "
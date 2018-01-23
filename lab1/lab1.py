import argparse
import json


def constraint_tuid(argument_value: str) -> bool:
    if not argument_value: return
    return len(argument_value) == 9 and argument_value.isdigit()


def constraint_status(argument_value: str) -> bool:
    if not argument_value: return
    return argument_value.lower() in ["undergraduate", "graduate", "u", "g", "undergrad"]


def constraint_weak(argument_value: str) -> bool:
    if not argument_value: return
    return True


def input_valid_value(argument_key: str) -> str:
    constraint_pass = False
    while not constraint_pass:
        user_input = input("Enter value for {}: ".format(argument_key))
        constraint_pass = argument_constraint_dictionary[argument_key](user_input)
    return user_input


def input_save_selection() -> bool:
    while True:
        user_input = input("Save Student Record to File? [Y/N]: ")
        if user_input.lower() in ["y", "yes", "ye"]:
            return True
        elif user_input.lower() in ["n", "no"]:
            return False


# dictionary to look up argument variables to a formal name and their validation function
argument_constraint_dictionary = {
    'Last Name':  constraint_weak,
    'First Name': constraint_weak,
    'Middle Name': constraint_weak,
    'Date of Birth': constraint_weak,
    'Phone Number': constraint_weak,
    'Expected Graduation Date': constraint_weak,
    'Temple University ID': constraint_tuid,
    'Email Address': constraint_weak,
    'Academic Major': constraint_weak,
    'Student Status': constraint_status
}

# command line arguments that can be entered
parser = argparse.ArgumentParser(description="Student Record Entry Program")
parser.add_argument("-i",
                    dest='flag_interactive',
                    action='store_true')
parser.add_argument("-l", help="Student Last Name", metavar="LASTNAME",
                    dest='Last Name',
                    action='store')
parser.add_argument("-f", dest='First Name', action='store', metavar="FIRSTNAME", help="First Name")
parser.add_argument("-m", dest='Middle Name', action='store', metavar="MIDDLENAME", help="Middle Name")
parser.add_argument("-b", dest='Date of Birth', action='store', metavar="DD/MM/YYYY", help="Date of Birth")
parser.add_argument("-p", dest='Phone Number', action='store', metavar="XXX-XXX-XXX", help="Phone Number")
parser.add_argument("-g", dest='Expected Graduation Date', action='store', metavar="DD/MM/YYYY",
                    help="Expected Graduation Date")
parser.add_argument("-t", dest='Temple University ID', action='store', metavar="TUID",
                    help="Temple University Identification Number")
parser.add_argument("-e", dest='Email Address', action='store', metavar="EMAIL", help="Email Address")
parser.add_argument("-j", dest='Academic Major', action='store', metavar="MAJOR", help="Academic Major")
parser.add_argument("-F", help="Flag to force saving of incomplete record.",
                    dest='flag_force_save',
                    action='store_true')
group = parser.add_mutually_exclusive_group()  # can enter as EITHER undergrad OR graduate
group.add_argument("-U", dest='flag_undergraduate', action='store_true', help="Undergraduate Student Flag")
group.add_argument("-G", dest='flag_graduate', action='store_true', help="Graduate Student Flag")

# get parsed arguments from the command line and create Namespace
argument_namespace = parser.parse_args()

# create a dictionary from the namespace consisting of the arguments and their values
argument_dictionary = vars(argument_namespace)

# get flags and remove them from dictionary
interactive_mode = argument_dictionary.pop('flag_interactive')
undergraduate = argument_dictionary.pop('flag_undergraduate')
graduate = argument_dictionary.pop('flag_graduate')
save = argument_dictionary.pop('flag_force_save')

# add 'status' to arguments dictionary based off flags
argument_dictionary['Student Status'] = "Undergraduate" if undergraduate else "Graduate" if graduate else None

# get all missing or invalid values from command line arguments
missing_arguments = list(filter(lambda dictionary_item: not argument_constraint_dictionary[dictionary_item[0]](dictionary_item[1]), argument_dictionary.items()))

# if interactive mode flag has been set, go through list of missing arguments and prompt for user input
if interactive_mode:
    for argument in missing_arguments:
        argument_dictionary[argument[0]] = input_valid_value(argument[0])
    # ask if user wants to save data entered
    save = input_save_selection()

# if interactive mode has NOT been set display all missing arguments
else:
    if missing_arguments:
        print("Missing/Invalid Argument: ", end="")
        for argument in missing_arguments:
            print("[ {} ]".format(argument[0]), end=" ")
    else:
        save = True

if save:
    data_file = open('output.dat', 'a')
    data_file.write(json.dumps(argument_dictionary, indent=4) + '\n')
    data_file.close()

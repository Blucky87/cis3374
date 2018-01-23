import argparse
import json

# command line arguments that can be entered
parser = argparse.ArgumentParser(description="Student Record Entry Program")
parser.add_argument("-i", help="prompt for inputting missing/invalid arguments",
                    dest='flag_interactive',
                    action='store_true')
parser.add_argument("-l", help="last name", metavar="lastname",
                    dest='last name',
                    action='store')
parser.add_argument("-f", help="first name", metavar="firstname",
                    dest='first name',
                    action='store')
parser.add_argument("-m", help="middle name", metavar="middlename",
                    dest='middle name',
                    action='store')
parser.add_argument("-b", help="date of birth", metavar="dd/mm/yyyy",
                    dest='date of birth',
                    action='store')
parser.add_argument("-p", help="phone number", metavar="xxx-xxx-xxx",
                    dest='phone number',
                    action='store')
parser.add_argument("-g", help="expected graduation date", metavar="dd/mm/yyyy",
                    dest='expected graduation date',
                    action='store',)
parser.add_argument("-t", help="9 digit tuid", metavar="xxxxxxxxx",
                    dest='temple university id',
                    action='store')
parser.add_argument("-e", help="email address", metavar="email",
                    dest='email address',
                    action='store')
parser.add_argument("-j", help="academic major", metavar="major",
                    dest='academic major',
                    action='store')

# can be flagged as EITHER undergrad OR graduate
group = parser.add_mutually_exclusive_group()
group.add_argument("-U", help="undergraduate student status",
                   dest='flag_undergraduate',
                   action='store_true')
group.add_argument("-G", help="graduate student status",
                   dest='flag_graduate',
                   action='store_true')


def constraint_tuid(value: str) -> bool:
    return len(value) == 9 and value.isdigit() \
        if value \
        else False


def constraint_status(value: str) -> bool:
    return value == "undergraduate" or value == "graduate" \
           if value is not None \
           else False


def constraint_weak(value: str) -> bool:
    return value is not None


def input_valid_value(key: str) -> str:
    user_input = None
    constraint_passing_input = user_input
    while not constraint_passing_input:
        user_input = input("enter value for {}: ".format(key))
        constraint_passing_input = passing_constraints[key](user_input)
    return user_input


def input_save_selection(dictionary) -> bool:
    print("-"*25)
    for (key, value) in dictionary.items():
        print(" {}: {}".format(key, value))
    print("-"*25)
    while True:
        user_input = input("save student record to file? [y/n]: ").lower()
        if user_input in ["y", "yes", "ye"]:
            return True
        elif user_input in ["n", "no"]:
            return False


# dictionary to look up validation checking functions by argument key
passing_constraints = {
    'last name':  constraint_weak,
    'first name': constraint_weak,
    'middle name': constraint_weak,
    'date of birth': constraint_weak,
    'phone number': constraint_weak,
    'expected graduation date': constraint_weak,
    'temple university id': constraint_tuid,
    'email address': constraint_weak,
    'academic major': constraint_weak,
    'student status': constraint_status
}


# get parsed arguments from the command line and create Namespace
argument_namespace = parser.parse_args()

# make a dictionary from the namespace using arguments and their values as (k,v)
argument_dictionary = vars(argument_namespace)

# save flags and remove them from argument dictionary
interactive = argument_dictionary.pop('flag_interactive')
undergraduate = argument_dictionary.pop('flag_undergraduate')
graduate = argument_dictionary.pop('flag_graduate')
save = True

# add 'Student Status' key to argument dictionary, value is based off of flags
argument_dictionary['student status'] = "undergraduate" if undergraduate \
                                        else "graduate" if graduate \
                                        else None

# filter argument dict items to list of (k,v) pairs that do not pass constraints
missing_argument_list = \
    list(filter(
        lambda dictionary_item:
            not passing_constraints[dictionary_item[0]](dictionary_item[1]),
        argument_dictionary.items()))

# if interactive, go through list of missing arguments and prompt for user input
if interactive:
    for argument in missing_argument_list:
        argument_dictionary[argument[0]] = input_valid_value(argument[0])
    save = input_save_selection(argument_dictionary)

# print help screen if missing or invalid argument values exist
else:
    if missing_argument_list:
        parser.print_help()
        save = False

# if saving is set, append all argument dictionary (k,v) pairs to a file as json
if save:
    record_file = open('student_records.dat', 'a')
    record_file.write(json.dumps(argument_dictionary, indent=4) + '\n')
    record_file.close()

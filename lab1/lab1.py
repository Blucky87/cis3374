import argparse
import json
     
def get_valid_value(key):
     value = None
     while not arg_dict[key]['constraint'](value):
          value = input("Enter value for {}: ".format(arg_dict[key]['formal']))
     return value

def valid_tuid(value):
     if value is None: return False
     return len(value) == 9 and value.isdigit() is True

def valid_status(value):
     if value is None: return False
     return value.lower() == "undergraduate" or value.lower() == "graduate"

def no_constraint(value):
     if value is None: return False
     elif len(value) == 0: return False
     return True

def save_choice():
     while True:
          value = input("Save Student Record to File? [Y/N]: ").lower()
          if value == 'y':
               return True
          elif value == 'n':
               return False

# dictionary to match argument variables to a formal name and their validation function
arg_dict = {
     'name_last':        {'formal': "Last Name", 'constraint': no_constraint},
     'name_first':       {'formal': "First Name", 'constraint': no_constraint},
     'name_middle':      {'formal': "Middle Name", 'constraint': no_constraint},
     'date_birth':       {'formal': "Date of Birth", 'constraint': no_constraint},
     'contact_phone':    {'formal': "Phone Number", 'constraint': no_constraint},
     'date_graduation':  {'formal': "Expected Graduation Date", 'constraint': no_constraint},
     'tuid':             {'formal': "Temple University ID", 'constraint': valid_tuid},
     'contact_email':    {'formal': "Email Address", 'constraint': no_constraint},
     'major':            {'formal': "Academic Major", 'constraint': no_constraint},
     'status':           {'formal': "Student Status", 'constraint': valid_status}
}

# command line arguments that can be entered
parser = argparse.ArgumentParser(description="Student Record Entry Program")
parser.add_argument("-i", dest='interactive_mode', action='store_true', help="Interactive Entry")
parser.add_argument("-l", dest='name_last', action='store', metavar="LASTNAME", help="Student Last Name")
parser.add_argument("-f", dest='name_first', action='store', metavar="FIRSTNAME", help="First Name")
parser.add_argument("-m", dest='name_middle', action='store', metavar="MIDDLENAME", help="Middle Name")
parser.add_argument("-b", dest='date_birth', action='store', metavar="DD/MM/YYYY", help="Date of Birth")
parser.add_argument("-p", dest='contact_phone', action='store', metavar="XXX-XXX-XXX", help="Phone Number")
parser.add_argument("-g", dest='date_graduation', action='store', metavar="DD/MM/YYYY", help="Expected Graduation Date")
parser.add_argument("-t", dest='tuid', action='store', metavar="TUID", help="Temple University Identification Number")
parser.add_argument("-e", dest='contact_email', action='store', metavar="EMAIL", help="Email Address")
parser.add_argument("-j", dest='major', action='store', metavar="MAJOR", help="Academic Major")
parser.add_argument("-F", dest='force_save', action='store_true', help="Flag to set forced saving of incomplete record.")
group = parser.add_mutually_exclusive_group()
group.add_argument("-U", dest='undergraduate', action='store_true', help="Undergraduate Student Flag")
group.add_argument("-G", dest='graduate', action='store_true', help="Graduate Student Flag")

# get parsed arguments from the command line
args = parser.parse_args()

# create dictionary namespace based on arguments
arguments_dict = vars(args)

# remove flags from namespace
interactive_mode = arguments_dict.pop('interactive_mode')
undergraduate = arguments_dict.pop('undergraduate')
graduate = arguments_dict.pop('graduate') 
force_save = arguments_dict.pop('force_save')

# create 'status' in namespace based off flags
arguments_dict['status'] = "Undergraduate" if undergraduate else "Graduate" if graduate else None

# get all missing or invalid values from command line arguments
missing_fields = list(filter(lambda x: not arg_dict[x[0]]['constraint'](x[1]), arguments_dict.items()))

# record saving turned on by default
should_save = True

# if interactive mode flag has been set, go through list of missing arguments
if interactive_mode is True:
     for item in missing_fields:
          arguments_dict[arg_name] = get_valid_value(item[0])
     # ask if user wants to save data entered
     should_save = save_choice()

# if interactive mode has NOT been set display all 
else:
     if len(missing_fields) > 0:
          should_save = force_save
          print("Missing/Invalid Argument: ", end="")
          for item in missing_fields:
               print(arg_dict[item[0]]['formal'], end="")
          if should_save is True: 
               print("\nSaving Partial Record.")
          
# write to file as a json dump
if should_save is True:
     data_file = open('output.dat', 'a')
     data_file.write(json.dumps(arguments_dict, indent=4) + '\n')
     data_file.close()


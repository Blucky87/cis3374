import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
# parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                     help='an integer for the accumulator')
parser.add_argument('-l, --last',
                    dest='name_last',
                    action='store',
                    help='Last Name')

parser.add_argument('-f, --first',
                    dest='name_first',
                    action='store',
                    help='First Name')

parser.add_argument('-m, --middle',
                    dest='name_middle',
                    action='store',
                    help='Middle Name')

parser.add_argument('-d, --dob',
                    dest='date_birth',
                    action='store',
                    help='Date of Birth in format dd/mm/yyyy ')

parser.add_argument('-p, --phone',
                    dest='contact_phone',
                    action='store',
                    help='Phone Number in format XXXXXXXXXX')

parser.add_argument('-g, --graduation',
                    dest='date_graduation',
                    action='store',
                    help='Graduation Date in format dd/mm/yyyy')

parser.add_argument('-t, --tuid',
                    dest='tuid',
                    action='store',
                    help='Temple University Identification number')

parser.add_argument('-e, --email',
                    dest='contact_email',
                    action='store',
                    help='Email address')

parser.add_argument('-j, --major',
                    dest='major',
                    action='store',
                    help='Academic Major')

parser.add_argument('-u, --undergrad',
                    dest='undergrad',
                    action='store',
                    help='Undergraduate')

args = parser.parse_args()
print(args)
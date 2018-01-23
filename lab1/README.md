
# Lab1 - Student Profile Program Usage

Requires Python 3  

## Usage
#### for basic entry:
```sh
python student_profile_program.py -i
```
it will walk you through manual entry  of each argument

#### for prefilled entry:
```sh
python student_profile_program.py -i -l Luckenbill -f Brian -e tuf37823@temple.edu
```
it will walk you through the missing arguments such as middle name, phone, etc  

#### for full entry:
```sh
python student_profile_program.py -f john -m joe -l smith \
-e jsmith@aol.com \
-p 6271121212 \
-b 01071940 \
-g 12202020 \
-j "Information Science & Technology" \
-t 123456789 \
-U
```
if all arguments are present and valid it will immediatly write to external file  
 __if -i flag is set, program will prompt for save confirmation__  


#### for multiple entries:
```sh
for i in {1..10}; do python student_profile_program.py -i; done
```
run in a shell script

## Flags
#### -i flag
```sh
python student_profile_program.py -i 
```

prompts user for all missing or incorrect fields

#### -U flag
sets student profile as undergraduate  
__mutually exclusive with the -G flag__  
#### -G flag
sets student profile as graduate  
__mutually exclusive with the -U flag__

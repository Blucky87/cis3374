
# Lab1 - Student Profile Program Usage

Requires Python 3  

## Usage
#### for basic entry:
```sh
python student_profile.py -i
```
it will walk you through manual entry  

#### for prefilled entry:
```sh
python student_profile.py -i -l Luckenbill -f Brian -e tuf37823@temple.edu
```
it will walk you through the missing arguments such as middle name, phone, etc  

#### for full entry:
```sh
python student_profile.py -f john -m joe -l smith \
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


## Flags
#### -i flag
```sh
python student_profile_program.py -i 
```

prompts user for all missing or incorrect fields

#### -l flag
```sh
python student_profile_program.py -i 
```
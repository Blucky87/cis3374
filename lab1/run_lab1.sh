#!/bin/bash



if ! [ -x "$(command -v whiptail)" ]; then
    echo "whiptail must be installed"
    exit 1
fi


backtitle="Lab 1 - Brian Luckenbill"

main() {
    clear

    if [ -z "$1" ]; then
        guided_input
        nextitem="Save"
    else
        nextitem=$1
    fi

    options=()
    options+=("Last Name" "$name_last")
    options+=("First Name" "$name_first")
    options+=("Middle Name" "$name_middle")
    options+=("Date of Birth" "$date_birth")
    options+=("Phone Number" "$contact_phone")
    options+=("Graduation Date" "$date_graduation")
    options+=("TUID" "$student_tuid")
    options+=("Email Address" "$contact_email")
    options+=("Major" "$student_major")
    options+=("Student Status" "$student_status")
    options+=(" " " ")
    options+=("Guided Input" " ")
    options+=(" " " ")
    options+=("Save" " ")

    sel=$(whiptail --backtitle "$backtitle" --title "Lab 1 Text-based User Interface" --menu "Use (Up/Down/Left/Right) Arrows to Select and (Enter) to Make Selection" --clear --cancel-button "Exit" --default-item "$nextitem" 0 0 0 "${options[@]}" 3>&1 1>&2 2>&3)

    if [ $? -eq 0 ]; then
        case $sel in
            "Guided Input")
                guided_input
                nextitem="Save"
            ;;
            "Last Name")
                set_name_last
                nextitem="First Name"
            ;;
            "First Name")
                set_name_first
                nextitem="Middle Name"
            ;;
            "Middle Name")
                set_name_middle
                nextitem="Date of Birth"
            ;;
            "Date of Birth")
                set_date_birth
                nextitem="Phone Number"
            ;;
            "Phone Number")
                set_contact_phone
                nextitem="Graduation Date"
            ;;
            "Graduation Date")
                set_date_graduation
                nextitem="TUID"
            ;;
            "TUID")
                set_student_tuid
                nextitem="Email Address"
            ;;
            "Email Address")
                set_contact_email
                nextitem="Major"
            ;;
            "Major")
                set_student_major
                nextitem="Student Status"
            ;;
            "Student Status")
                set_student_status
                nextitem="Save"
            ;;
            "Save")
                save_student
                nextitem="Guided Input"
            ;;
        esac
            main "$nextitem"
    else
        clear
        break
    fi

}

set_name_last() {
    if [ -n "$1" ]; then
        name_last=$1
    else
        name_last=$(whiptail --backtitle "$backtitle" --title "Last Name" --inputbox "Enter Student Last Name:" 0 0 "$name_last" 3>&1 1>&2 2>&3)
    fi
}

set_name_first() {
    if [ -n "$1" ]; then
        name_first=$1
    else
        name_first=$(whiptail --backtitle "$backtitle" --title "First Name" --inputbox "Enter Student First Name:" 0 0 "$name_first" 3>&1 1>&2 2>&3)
    fi
}

set_name_middle() {
    if [ -n "$1" ]; then
        name_middle=$1
    else
        name_middle=$(whiptail --backtitle "$backtitle" --title "Middle Name" --inputbox "Enter Student Middle Name:" 0 0 "$name_middle" 3>&1 1>&2 2>&3)
    fi
}

set_date_birth() {
    if [ -n "$1" ]; then
        date_birth=$1
    else
        date_birth=$(whiptail --backtitle "$backtitle" --title "Date of Birth" --inputbox "Enter Student Date of Birth dd/mm/yyyy:" 0 0 "$date_birth" 3>&1 1>&2 2>&3)
    fi
}

set_contact_phone() {
    if [ -n "$1" ]; then
        contact_phone=$1
    else
        contact_phone=$(whiptail --backtitle "$backtitle" --title "Phone Number" --inputbox "Enter Student Phone Number xxx-xxx-xxxx:" 0 0 "$contact_phone" 3>&1 1>&2 2>&3)
    fi
}

set_date_graduation() {
    if [ -n "$1" ]; then
        date_graduation=$1
    else
        date_graduation=$(whiptail --backtitle "$backtitle" --title "Expected Graduation Date" --inputbox "Enter Student Date of Expected Graduation dd/mm/yyyy:" 0 0 "$date_graduation" 3>&1 1>&2 2>&3)
    fi
}

set_student_tuid() {
    if [ -n "$1" ]; then
        student_tuid=$1
    else
        student_tuid=$(whiptail --backtitle "$backtitle" --title "Temple University ID" --inputbox "Enter Student TUID:" 0 0 "$student_tuid" 3>&1 1>&2 2>&3)
    fi
}

set_contact_email() {
    if [ -n "$1" ]; then
        contact_email=$1
    else
        contact_email=$(whiptail --backtitle "$backtitle" --title "Email Address" --inputbox "Enter Student E-mail Address:" 0 0 "$contact_email" 3>&1 1>&2 2>&3)
    fi
}

set_student_major() {
    if [ -n "$1" ]; then
        student_major=$1
    else
        student_major=$(whiptail --backtitle "$backtitle" --title "Academic Major" --inputbox "Enter Student Academic Major:" 0 0 "$student_major" 3>&1 1>&2 2>&3)
    fi
}

set_student_status() {
    if [ -n "$1" ]; then
        student_status=$1
    else
        options=()
        options+=("Undergraduate" "")
        options+=("Graduate" "")
        sel=$(whiptail --backtitle "$backtitle" --title "Student Status" --menu "Choose Student Status:" 0 0 0 "${options[@]}" 3>&1 1>&2 2>&3)
        if [ $? -eq 0 ]; then
            case $sel in
                "Undergraduate")
                    student_status="Undergraduate"
                ;;
                "Graduate")
                    student_status="Graduate"
                ;;
            esac

        fi
    fi
}

waitforkeypress(){
  read -n1 -p "Press any key to continue..."
}

guided_input(){
    set_name_last
    set_name_first
    set_name_middle
    set_date_birth
    set_contact_phone
    set_date_graduation
    set_student_tuid
    set_contact_email
    set_student_major
    set_student_status
}

clear_all_fields(){
    name_last=""
    name_first=""
    name_middle=""
    date_birth=""
    contact_phone=""
    date_graduation=""
    student_tuid=""
    contact_email=""
    student_major=""
    student_status=""
}

save_student() {
    if [ "$student_status" = "Undergraduate" ]; then
        status_arg="-U"
    elif [ "$student_status" = "Graduate" ]; then
        status_arg="-G"
    fi

 echo "python lab1 -l \"$name_last\" -f \"$name_first\" -m \"$name_middle\" -b \"$date_birth\" -p \"$contact_phone\" -g \"$date_graduation\" -t \"$student_tuid\" -e \"$contact_email\" -j \"$student_major\" $status_arg"
 waitforkeypress
 clear_all_fields
}

main
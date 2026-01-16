import sys

def get_number():
    """
    Gets a valid 11-digit phone number from the user.
    Returns the number as a string or 0 if user types 'cancel'.
    """
    while True:
        number = input("Enter Phone Number (11 digits required, or 'cancel'): ").strip()

        if number.isdigit() and len(number) == 11:
            return number
        elif number == 'cancel':
            return 0
        else:
            print("Error: Phone number must be exactly 11 digits and contain only numbers.")


def print_main_menu():
    """Displays the main menu options."""
    print("--- MAIN MENU ---")
    print("1. Add New Contact")
    print("2. View All Contacts")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. Exit")
    print("-----------------")

def get_choice_main_menu():
    """
    Gets a menu choice between 1-5.
    Loops until user enters a valid input.
    """
    while True:
        choice = input("Enter your choice (1-5): ").strip()

        if choice.isdigit()== False:
            print("Invalid input. Please enter a number.")
        elif int(choice) >= 1 and int(choice) <= 5:
            return int(choice)
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

def get_choice_edit_menu():
    """
    Gets a choice from the edit menu (1-4).
    Returns 0 if user types 'cancel'.
    """
    while True:
        choice = input("Enter your choice (1-4)(or 'cancel'): ").strip()

        if choice == 'cancel':
            return 0
        elif choice.isdigit()== False:
            print("Invalid input. Please enter a number.")
        elif int(choice) >= 1 and int(choice)<= 4:
            return int(choice)
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

def edit_contact_menu(contact_data):
    """Displays editable fields and updates the selected one."""
    print("Which field do you want to change?")
    print(f"1: Name (Current: {contact_data['name']})")
    print(f"2: Phone Number (Current: {contact_data['phone_number']})")
    print(f"3: Email (Current: {contact_data['email']})")
    print(f"4: Country (Current: {contact_data['country']})")

    choice = get_choice_edit_menu()

    if choice == 1:
        name = input("Enter NEW Name (or 'cancel'): ").strip()
        if name == 'cancel':
            return 0
        else:
            contact_data["name"] = name
            print(f"Success! Name updated for {name}.")
            return contact_data

    elif choice == 2:
        phone_number = input("Enter NEW Phone Number (or 'cancel'): ").strip()
        if phone_number == 'cancel':
            return 0
        else:
            contact_data["phone_number"] = phone_number
            print(f"Success! Phone Number updated for {contact_data['name']}.")
            return contact_data

    elif choice == 3:
        email = input("Enter NEW Email (or 'cancel'): ").strip()
        if email == 'cancel':
            return 0
        else:
            contact_data["email"] = email
            print(f"Success! Email updated for {contact_data['name']}.")
            return contact_data

    elif choice == 4:
        country = input("Enter NEW Country (or 'cancel'): ").strip()
        if country == 'cancel':
            return 0
        else:
            contact_data["country"] = country
            print(f"Success! Country updated for {contact_data['name']}.")
            return contact_data

    elif choice == 0:
        return 0


def add_new_contact(contacts_list):
    """
    Adds a new contact to the list.
    Cancels the operation if user types 'cancel'.
    """
    contact_data = dict()
    print("--- ADD NEW CONTACT (Type 'cancel' to return to menu) ---")

    name = input("Enter Name (Required)(or 'cancel'): ").strip()
    if name == 'cancel':
        print("Operation cancelled. Returning to main menu.")
        return
    elif len(name) == 0:
        print("Error: Name cannot be empty. Operation cancelled.")
        return
    else:
        contact_data['name'] = name

    phone_number = get_number()
    if phone_number == 0:
        print("Operation cancelled. Returning to main menu.")
        return
    else:
        contact_data['phone_number'] = phone_number

    email = input("Enter Email Address (or 'cancel'): ").strip()
    if email == 'cancel':
        print("Operation cancelled. Returning to main menu.")
        return

    elif len(email) == 0:
        print("Error: Email Address cannot be empty. Operation cancelled.")
        return
    else:
        contact_data['email'] = email

    country = input("Enter Country (or 'cancel'): ").strip()
    if country == 'cancel':
        print("Operation cancelled. Returning to main menu.")
        return
    elif len(country) == 0:
        print("Error: Country cannot be empty. Operation cancelled.")
        return
    else:
        contact_data['country'] = country

    # Adds new contact
    contacts_list.append(contact_data)
    print(f"SUCCESS: Contact {name} added.")



def view_all_contacts(contacts_list):
    """ Displays all contacts in a formatted table. """
    print()
    print("|" + "-" * 30 + " CONTACT LIST " + "-" * 30 + "|")
    print("|%-5s|%-15s|%-15s|%-25s|%-10s|" % ("Index", "Name", "Phone", "Email", "Country"))
    print("|" + "=" * 74 + "|")
    if len(contacts_list) == 0:
        print("    The contact list is currently empty.")
    else:
        index = 1
        for contact_data in contacts_list:
            row = (
                index,
                contact_data['name'],
                contact_data['phone_number'],
                contact_data['email'],
                contact_data['country']
            )
            print("|%-5s|%-15s|%-15s|%-25s|%-10s|" % row )
            index += 1
    print("+" + "-" * 74 + "+")



def edit_contact(contacts_list):
    """
    Searches contacts and handles multiple matches.
    Opens the edit menu for the selected contact.
    """
    print("--- EDIT CONTACT (Type 'cancel' to return to menu) ---")
    # Gets search input
    name = input("Enter the name (or part of the name) of the contact to edit or type 'cancel' to return to menu: ").strip()

    if name == 'cancel':
        print("Operation cancelled. Returning to main menu.")
        return

    # Finds matching names
    else:
        names_contain_input = []
        for contact_data in contacts_list:
            if contact_data['name'] == name or name in contact_data['name']:
             names_contain_input.append(contact_data['name'])

        # No match
        if len(names_contain_input) == 0:
            print(f"No contacts found matching {name}.")
            return

        # Multiple matches
        elif len(names_contain_input) > 1:
            print("Multiple contacts found. Please select one to edit: ")
            index_list = []

            # Stores indexes of matching contacts.
            for index, contact_data in enumerate(contacts_list):
                if contact_data['name'] in names_contain_input:
                    index_list.append(index)

            # Display options
            row = 1
            for index in index_list:
                contact_data = contacts_list[index]
                print(f"[{row}] {contact_data['name']} ({contact_data['phone_number']})")
                row = row + 1

            # Gets user selection
            select_contact = int(input("Enter number of contact to edit, or type 0 to cancel: "))
            if select_contact == 0:
                print("Operation cancelled. Returning to main menu.")
                return

            # Converts selection to actual contact
            contact_data = contacts_list[index_list[select_contact - 1]]

        # One match
        elif len(names_contain_input) == 1:
            for contact_data in contacts_list:
                if contact_data['name'] == names_contain_input[0]:
                    contact_index = int(contacts_list.index(contact_data))
            contact_data = contacts_list[contact_index]

        # Opens edit menu
        print(f"Editing contact: {contact_data['name']}.")
        new_contact_data = edit_contact_menu(contact_data)

        if new_contact_data == 0:
            print("Update cancelled. Returning to main menu.")
            return

        # Updates actual contact.
        else:
            contact_data = new_contact_data



def delete_contact(contacts_list):
    """
    Searches contacts, handles multiple matches,
    asks for confirmation and deletes the selected contact.
    """
    print("--- DELETE CONTACT (Type 'cancel' to return to menu) ---")
    # Gets search input
    name = input("Enter the name (or part of the name) of the contact to delete or type 'cancel' to return to menu: ").strip()

    if name == 'cancel':
        print("Operation cancelled. Returning to main menu.")
        return
    # Finds matching names
    else:
        names_contain_input = []
        for contact_data in contacts_list:
            if contact_data['name'] == name or name in contact_data['name']:
                names_contain_input.append(contact_data['name'])
        # No match
        if len(names_contain_input) == 0:
            print(f"No contacts found matching {name}.")
            return

        # Multiple matches
        elif len(names_contain_input) > 1:
            print("Multiple contacts found. Please select one to delete: ")
            index_list = []

            # Stores indexes of matching contacts
            for index, contact_data in enumerate(contacts_list):
                if contact_data['name'] in names_contain_input:
                    index_list.append(index)

            # Display options
            row = 1
            for index in index_list:
                contact_data = contacts_list[index]
                print(f"[{row}] {contact_data['name']} ({contact_data['phone_number']})")
                row += 1

            # Gets user selection
            select_contact = int(input("Enter number of contact to delete, or type 0 to cancel: "))
            if select_contact == 0:
                print("Deletion cancelled. Returning to main menu.")
                return

            # Converts selection to actual contact
            contact_data = contacts_list[index_list[select_contact - 1]]

        # One match
        elif len(names_contain_input) == 1:
            for contact_data in contacts_list:
                if contact_data['name'] == names_contain_input[0]:
                    contact_index = int(contacts_list.index(contact_data))
            contact_data = contacts_list[contact_index]

        # Asks confirmation before deleting
        print(f"WARNING: You are about to delete {contact_data['name']}.")
        yes_no = input("Are you sure you want to delete this contact? (yes/no): ").strip()

        if yes_no == 'no':
            print("Deletion cancelled. Returning to main menu.")
            return
        elif yes_no == 'yes':
            # Deletes contact
            contacts_list.remove(contact_data)
            print(f"SUCCESS: Contact {contact_data['name']} has been deleted.")
        else:
            print("Invalid input. Deletion cancelled. Returning to main menu.")
            return


def run_manager(contacts_list):
    """Runs the main menu and handles user choices."""
    while True:
        print_main_menu()
        choice = int(get_choice_main_menu())
        if choice == 1:
            add_new_contact(contacts_list)
        elif choice == 2:
            view_all_contacts(contacts_list)
        elif choice == 3:
            edit_contact(contacts_list)
        elif choice == 4:
            delete_contact(contacts_list)
        elif choice == 5:
            print("Exiting Contact Manager. Goodbye!")
            break


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        input_file_path = sys.argv[1]
        try:
            sys.stdin = open(input_file_path,'r')
        except FileNotFoundError:
            sys.exit(1)
    contacts_list = []
    run_manager(contacts_list)
    if len(sys.argv) > 1:
        sys.stdin.close()

#b2250765060

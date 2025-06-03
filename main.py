import time
import populations
import invasions
import fieldoffices


def menu_options():
    failed_input = 1
    options = ("\nEnter one of the below number options:"
              + "\n1 - See active district populations" 
              + "\n2 - See active invasions"
              + "\n3 - See active field offices"
              + "\n4 - EXIT APP")
    print(options)
    while failed_input:
        for attempt in range(5):
            if attempt == 4:
                print("Too many invalid entries. Program exiting...")
                time.sleep(1)
                exit()
            user_input = input("> ")
            if user_input not in ["1", "2", "3", "4"]:
                print(f"\nInvalid input. {options}")
            else:
                failed_input = 0
                break
    print()
    return user_input


def menu():
    print("Welcome to the ToonTown Rewritten App.\n")
    user_input = menu_options()
    if user_input == "1":
        populations.main()
    elif user_input == "2":
        invasions.main()
    elif user_input == "3":
        fieldoffices.main()
    elif user_input == "4":
        print("Thank you for using the ToonTown Rewritten App."
              + "\nProgram closing...")

menu()

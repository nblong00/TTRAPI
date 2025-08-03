import time
import populations
import invasions
import fieldoffices
import sillymeter


def menu_options():
    failed_input = True
    options = """
              \rEnter one of the below number options:
              \r1 - See active district populations
              \r2 - See active invasions
              \r3 - See active field offices
              \r4 - Check if Silly Meter is active
              \r5 - EXIT APP
              """
    print(options)
    while failed_input:
        for attempt in range(5):
            if attempt == 4:
                print("Too many invalid entries. Program exiting...")
                time.sleep(1)
                exit()
            user_input = input("> ")
            if user_input not in ["1", "2", "3", "4", "5"]:
                print(f"\nInvalid input. {options}")
            else:
                failed_input = False
                break
    return user_input


def menu():
        while True:
            print("\nWelcome to the ToonTown Rewritten App.")
            user_input = menu_options()
            if user_input == "1":
                populations.main()
            elif user_input == "2":
                invasions.main()
            elif user_input == "3":
                fieldoffices.main()
            elif user_input == "4":
                sillymeter.main()
            elif user_input == "5":
                print("""
                      \rThank you for using the ToonTown Rewritten App.
                      \rProgram closing...
                      """)
                time.sleep(1)
                exit()


if __name__ == '__main__':
    menu()

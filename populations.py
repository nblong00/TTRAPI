import pandas
import utils
import time

URL = "https://www.toontownrewritten.com/api/population"
ENDPOINT = "(POP)"


def welcome(data):
    print("\n-Welcome to the ToonTown Rewritten (TTR) Population Map-")
    print(f"It is currently {utils.dt()}")
    print(f"Total population: {data['totalPopulation']} users")
    time.sleep(0.5)


def user_options():
    failed_input = 1
    options = ("\nEnter one of the below number options:" +
              "\n1 - See all district populations" + 
              "\n2 - See only high population districts" +
              "\n3 - See only low population districts\n")
    print(options)
    while failed_input:
        for attempt in range(5):
            if attempt == 4:
                print("Too many invalid entries. Program exiting...")
                time.sleep(1)
                exit()
            user_input = input("> ").lower()
            if user_input not in ["1", "2", "3"]:
                print(f"\nInvalid input. {options}")
            else:
                failed_input = 0
                break
    print()
    return user_input


def get_API_write_csv(data, user_input):
    column_names = ["DistrictName",
                     "Population",
                     "Status"]
    utils.create_csv_for_data(column_names)
    for district in data["populationByDistrict"]:
        if user_input == "1":
            json_to_write(data, district)
        elif user_input == "2" and data["populationByDistrict"][district] >= 150:
            json_to_write(data, district)
        elif user_input == "3" and data["populationByDistrict"][district] <= 150:
            json_to_write(data, district)


def json_to_write(data, district):
    data_to_write = [district, 
                        str(data["populationByDistrict"][district]) + " Users",
                        data["statusByDistrict"][district].title()]
    utils.write_data_to_csv(data_to_write)


def dataframe_map_name(user_input):
    if user_input == "1":
        print("All Districts Population Map:\n")
    elif user_input == "2":
        print("High Population District Map:\n")
    elif user_input == "3":
        print("Low Population District Map:\n")


def pull_API_data_again(end_program, refresh_current_map_pop, restart_program):
    for attempt in range(5):
        if attempt == 4:
            print("Too many invalid entries. Program closing...")
            end_program = 1
            restart_program = 0
            return end_program, refresh_current_map_pop, restart_program
        user_input = input("> ").lower()
        if user_input in ["no", "n"]:
            end_program = 1
            restart_program = 0
            print("\nWould you like to go back to the Populations submenu? (yes/no)\n")
            for input_attempt in range(5):
                if input_attempt == 4:
                    print("Too many invalid entries. Program closing...")
                    end_program = 1
                    restart_program = 0
                    return end_program, refresh_current_map_pop, restart_program
                restart_program_input = input("> ").lower()
                if restart_program_input in ["yes", "y", "ye"]:
                    restart_program = 1
                    end_program = 0
                    return end_program, refresh_current_map_pop, restart_program
                elif restart_program_input not in ["no", "n", "yes", "y", "ye"] and input_attempt <= 2:
                    print("\nInvalid entry. Go back to the Populations submenu? (yes/no)\n")
                    continue
                elif restart_program_input in ["no", "n"]:
                    print("\nExiting Population Map...")
                    restart_program = 0 
                    return end_program, refresh_current_map_pop, restart_program
        elif user_input not in ["no", "n", "yes", "y", "ye"] and attempt <= 2:
            print("\nInvalid entry. Refresh the current population map? (yes/no)\n")
            continue
        elif user_input in ["yes", "y", "ye"] and attempt <= 3:
            print("\nRefreshing Current Population Map...\n")
            time.sleep(1)
            refresh_current_map_pop = 1
            restart_program = 0
            return end_program, refresh_current_map_pop, restart_program


def main_logic_loops(data):
    end_program = 0
    refresh_current_map_pop = 0
    restart_program = 1
    while not end_program:
        user_input = user_options()
        get_API_write_csv(data, user_input)
        while refresh_current_map_pop or restart_program:
            dataframe_map_name(user_input)
            result = pandas.read_csv("adjustedData.csv")
            print(result)
            print("\nWould you like to refresh the current population map? (yes/no)\n")
            (end_program,
             refresh_current_map_pop,
             restart_program) = pull_API_data_again(end_program,
                                                    refresh_current_map_pop,
                                                    restart_program)
            if restart_program or end_program:
                break


def main():
    data = utils.error_checking_and_logging(URL, ENDPOINT)
    utils.checking_if_error_is_active(data, ENDPOINT)
    welcome(data)
    main_logic_loops(data)
    time.sleep(1)

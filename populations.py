import requests
import pandas
import utils
import time
import logging

logging.basicConfig(filename="api.log", level=logging.INFO)
url = "https://www.toontownrewritten.com/api/population"
header = {"Content-Type":"application/json",
        "Accept-Encoding":"deflate",
        "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:138.0) Gecko/20100101 Firefox/138.0"}


def welcome(data):
    print("\n-Welcome to the ToonTown Rewritten (TTR) Population Map-")
    print(f"It is currently {utils.dt()}")
    print(f"Total population: {data['totalPopulation']} users")
    time.sleep(0.5)


def get_API_write_csv(data, user_input):
    column_names = ["DistrictName",
                     "Population",
                     "Status"]
    utils.create_CSV_for_data(column_names)
    for district in data["populationByDistrict"]:
        json_fields = []
        if user_input == "1":
            json_fields = [district, 
                        str(data["populationByDistrict"][district]) + " Users",
                        data["statusByDistrict"][district].title()]
        elif user_input == "2":
            if data["populationByDistrict"][district] >= 150:
                json_fields = [district, 
                        str(data["populationByDistrict"][district]) + " Users",
                        data["statusByDistrict"][district].title()]
        elif user_input == "3":
            if data["populationByDistrict"][district] <= 150:
                json_fields = [district, 
                        str(data["populationByDistrict"][district]) + " Users",
                        data["statusByDistrict"][district].title()]
        data_to_write = json_fields
        utils.write_data_to_CSV(data_to_write)


def pull_API_data_again(end_program, refresh_current_map_pop, restart_program):
    for attempt in range(5):
        if attempt == 4:
            print("Too many invalid entries. Program closing...")
            end_program = True
            restart_program = False
            return end_program, refresh_current_map_pop, restart_program
        user_input = input("> ")
        if user_input.lower() in ["no", "n"]:
            end_program = True
            restart_program = False
            print("\nWould you like to restart the Population Map program? (yes/no)\n")
            restart_program_input = input("> ")
            if restart_program_input in ["yes", "y", "ye"]:
                restart_program = True
                end_program = False
            else:
                print("\nThank you for using the ToonTown Rewritten Population Map!")
                print("Program closing...")
            return end_program, refresh_current_map_pop, restart_program
        elif user_input.lower() not in ["no", "n", "yes", "y", "ye"] and attempt <= 2:
            print("\nInvalid entry. Would you like to refresh the current population map? (yes/no)\n")
            continue
        elif user_input.lower() in ["yes", "y", "ye"] and attempt <= 3:
            print("\nRefreshing Current Population Map...\n")
            time.sleep(0.5)
            refresh_current_map_pop = True
            restart_program = False
            return end_program, refresh_current_map_pop, restart_program


def user_options():
    failed_input = True
    options = ("\nEnter one of the below number options:" +
              "\n1 - See all district populations" + 
              "\n2 - See only high population districts" +
              "\n3 - See only low population districts\n")
    print(options)
    while failed_input:
        for i in range(5):
            if i == 4:
                print("Too many invalid entries. Program exiting...")
                time.sleep(1)
                exit()
            user_input = input("> ")
            if user_input not in ["1", "2", "3"]:
                print(f"\nInvalid input. {options}")
            else:
                failed_input = False
                break
    print()
    return user_input


def error_checking_and_logging():
    pass


def api_get_call():
    response = requests.get(url, headers=header)
    data = response.json() 
    return data

def main():
    end_program = False
    refresh_current_map_pop = False
    restart_program = True
    data = api_get_call()
    welcome(data)
    while not end_program:
        user_input = user_options()
        get_API_write_csv(data, user_input)
        while refresh_current_map_pop or restart_program:
            result = pandas.read_csv("adjustedData.csv")
            print(result)
            print("\nWould you like to refresh the current population map? (yes/no)\n")
            end_program, refresh_current_map_pop, restart_program = pull_API_data_again(end_program,
                                                                                        refresh_current_map_pop,
                                                                                        restart_program)
            if restart_program or end_program:
                break
    time.sleep(1.5)


main()

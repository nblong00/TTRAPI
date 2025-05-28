import requests
import pandas
import utils
import time

url = "https://www.toontownrewritten.com/api/population"
header = {"Content-Type":"application/json",
        "Accept-Encoding":"deflate",
        "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:138.0) Gecko/20100101 Firefox/138.0"}


def welcome(data):
    print("\n-Welcome to the ToonTown Rewritten (TTR) Population Map-")
    print(f"It is currently {utils.dt()}")
    print(f"Total population: {data['totalPopulation']} users\n")
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


def pull_API_data_again(end_program):
    for attempt in range(5):
        if attempt == 4:
            print("Too many invalid entries. Program closing...")
            end_program = True
            return end_program
        user_input = input("> ")
        if user_input.lower() in ["no", "n"]:
            end_program = True
            print("\nThank you for using the ToonTown Rewritten Population Map!")
            print("Program closing...")
            return end_program
        elif user_input.lower() not in ["no", "n", "yes", "y", "ye"] and attempt <= 2:
            print("Invalid entry. Would you like to refresh the population map? (yes/no)")
            continue
        elif user_input.lower() in ["yes", "y", "ye"] and attempt <= 3:
            print("\nRestarting Population Map Program...\n")
            end_program = False
            time.sleep(1)
            return end_program


def user_options(data):
    print("Enter one of the below number options:" +
              "\n1 - See all district populations" + 
              "\n2 - See only high population districts" +
              "\n3 - See only low population districts\n")
    user_input = input("> ")
    get_API_write_csv(data, user_input)


def error_checking_and_logging():
    pass


def main():
    end_program = False
    while not end_program:
        response = requests.get(url, headers=header)
        data = response.json()
        welcome(data)
        user_options(data)
        result = pandas.read_csv("adjustedData.csv")
        print(result)
        print("\nWould you like to restart the population map? (yes/no)")
        end_program = pull_API_data_again(end_program)

main()

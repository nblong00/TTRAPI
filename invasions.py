import requests
import pandas
import utils
import time
import logging
import datetime
from dateutil import relativedelta
import math

logging.basicConfig(filename="api.log", level=logging.INFO)
url = "https://www.toontownrewritten.com/api/invasions"
header={"Content-Type":"application/json",
        "Accept-Encoding":"deflate",
        "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:138.0) Gecko/20100101 Firefox/138.0"}


def welcome():
    print("\n-Welcome to the ToonTown Rewritten (TTR) invasion scanner-")
    print(f"It is currently {utils.dt()}\n")
    time.sleep(0.5)


def sorting_for_CSV(data):
    column_names = ["DistrictName", "Type", "Progress"]
    utils.create_CSV_for_data(column_names)
    for district in data['invasions']:
            data_to_write = [district, 
                            data['invasions'][district]['type'],
                            data['invasions'][district]['progress']]
            # print(datetime.datetime.fromtimestamp(data['invasions'][district]['startTimestamp']))
            # max_progress_value = int(data['invasions'][district]['progress'].split("/")[1])
            # max_time_for_invasion = math.ceil((max_progress_value * 0.7) / 60)
            # print(max_time_for_invasion)
            if 'Tele\u0003marketer' in data['invasions'][district]['type']:
                data['invasions'][district]['type'] = "Telemarketer" 
            elif 'Micro\u0003manager' in data['invasions'][district]['type']:
                data['invasions'][district]['type'] = "Micromanager"
            else:
                pass
            utils.write_data_to_CSV(data_to_write)


def error_checking_and_logging(response):
    if response.status_code != 200:
            logging.warning(f"{utils.dt()} - Response code received: {response.status_code}")
            print(f"API responded with an unsuccessful {response.status_code} code.")
    else:
        logging.info(f"{utils.dt()} - Response code received: {response.status_code}")
    try:
        data = response.json()
        logging.info(f"API data updated from central TTR server at " + 
                    f"{utils.convert_epoch_timestamp_string(data)}")
        return data
    except requests.exceptions.JSONDecodeError:
        logging.error(f"{utils.dt()} - API JSON may be malformed. " + 
                    "We were unable to extract data from the response.")
        input("Press ENTER to close program...")
        exit()


def pull_API_data_again(end_program):
    for attempt in range(5):
        if attempt == 4:
            print("Too many invalid entries. Program closing...")
            end_program = True
            return end_program
        user_input = input("> ")
        if user_input.lower() in ["no", "n"]:
            end_program = True
            print("\nThank you for using the ToonTown Rewritten invasion scanner!")
            print("Program closing...")
            return end_program
        elif user_input.lower() not in ["no", "n", "yes", "y", "ye"] and attempt <= 2:
            print("Invalid entry. Would you like to check for new invasions? (yes/no)")
            continue
        elif user_input.lower() in ["yes", "y", "ye"] and attempt <= 3:
            print("\nPulling current invasions in ToonTown Rewritten...\n")
            end_program = False
            time.sleep(1)
            return end_program
        else:
            pass


def main():
    end_program = False
    welcome()
    while not end_program:
        response = requests.get(url, headers=header)
        data = error_checking_and_logging(response)
        sorting_for_CSV(data)
        result = pandas.read_csv("adjustedData.csv")
        print(result)
        print("\nDo you want to pull a new list of current invasions? (yes/no)")
        end_program = pull_API_data_again(end_program)
    time.sleep(0.5)


main()

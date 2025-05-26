import requests
import pandas
import utils
import time
import logging

logging.basicConfig(filename="api.log", level=logging.INFO)
url = "https://www.toontownrewritten.com/api/invasions"
header={"Content-Type":"application/json",
        "Accept-Encoding":"deflate",
        "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:138.0) Gecko/20100101 Firefox/138.0"}


def welcome():
    print("\n-Welcome to the ToonTown Rewritten invasion scanner-")
    print(f"It is currently {utils.dt()}\n")
    time.sleep(0.5)


def main():
    end_program = False
    welcome()
    while not end_program:
        response = requests.get(url, headers=header)
        if response.status_code != 200:
            logging.warning(f"{utils.dt()} - Response code received: {response.status_code}")
            print(f"API responded with an unsuccessful {response.status_code} code.")
        else:
            logging.info(f"{utils.dt()} - Response code received: {response.status_code}")
        try:
            data = response.json()
        except requests.exceptions.JSONDecodeError:
            logging.error(f"{utils.dt()} - API JSON may be malformed. " + 
                        "We were unable to extract data from the response.")
            input("Press ENTER to close program...")
            exit()
        logging.info(f"API data updated from central TTR server at {utils.convert_epoch_timestamp(data)}")
        utils.export_cleanedup_CSV_and_import(data)
        result = pandas.read_csv("adjustedData.csv")
        print(result)
        print("\nDo you want to pull a new list of current invasions? (yes/no)")
        for attempt in range(5):
            if attempt == 4:
                print("Too many invalid entries. Program closing...")
                end_program = True
                break
            user_input = input("> ")
            if user_input.lower() in ["no", "n"]:
                end_program = True
                print("\nThank you for using the TTR invasion scanner!\n")
                break
            elif user_input.lower() not in ["no", "n", "yes", "y", "ye"] and attempt <= 2:
                print("Invalid entry. Would you like to check for new invasions? (yes/no)")
                continue
            else:
                print("\nPulling current invasions in ToonTown Rewritten...\n")
                time.sleep(1)
                break
    time.sleep(0.5)


main()

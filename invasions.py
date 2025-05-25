import requests
import pandas
import utils
import time
import datetime

url = "https://www.toontownrewritten.com/api/invasions"
header={"Content-Type":"application/json",
        "Accept-Encoding":"deflate",
        "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:138.0) Gecko/20100101 Firefox/138.0"}


def welcome():
    print("\n-Welcome to the TTR invasions scanner-")
    print(f"It is currently {utils.dt()}\n")
    time.sleep(0.5)

def main():
    end_program = False
    welcome()
    while not end_program:
        response = requests.get(url, headers=header)
        data = response.json()
        utils.export_cleanedup_CSV_and_import(data)
        result = pandas.read_csv("adjustedData.csv")
        print(result)
        print("\nDo you check for new invasions? (yes/no)")
        for attempt in range(5):
            if attempt == 4:
                print("Too many invalid entries. Program closing...")
                end_program = True
                break
            user_input = input("> ")
            if user_input.lower() in ["no", "n"]:
                end_program = True
                break
            elif user_input.lower() not in ["no", "n", "yes", "y", "ye"] and attempt <= 2:
                print("Invalid entry. Would you like to check for new invasions? (yes/no)")
                continue
    time.sleep(0.5)

main()

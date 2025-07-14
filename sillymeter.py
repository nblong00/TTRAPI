import utils
import datetime
import time
from dateutil import relativedelta

URL = "https://www.toontownrewritten.com/api/sillymeter"
ENDPOINT = "(SIM)"


def timestamp_conversions(data):
    converted_starting_timestamp = (datetime.datetime.fromtimestamp(data['nextUpdateTimestamp']))
    time_difference = relativedelta.relativedelta(converted_starting_timestamp,
                                                  datetime.datetime.now())
    if data['state'] == "Active" and data['winner'] == None:
        return_statement = f"Silly Points will be updated in {time_difference.minutes} minutes!"
        if time_difference.minutes <= 1:
            return_statement = f"Silly Points will be updated in 1 minute!"
    elif data['state'] == "Inactive":
        return_statement = f"Silly Meter will become active in {time_difference.minutes} minutes!"
        if time_difference.minutes <= 1:
            return_statement = f"Silly Meter will become active in 1 minute!"
    elif data['state'] == "Reward":
        return_statement = f"Silly Meter reward ends in {time_difference.minutes} minutes!"
        if time_difference.minutes <= 1:
            return_statement = f"Silly Meter reward ends in 1 minute!"
    print(return_statement)


def update_silly_meter_status():
    refresh_status = input("Refresh Silly Meter Status (yes/no): \n> ")
    if refresh_status in ["yes", "ye", "y"]:
        time.sleep(0.5)
        return 0
    elif refresh_status in ["no", "n"]:
        time.sleep(0.5)
        return 1


def main_logic_loop(data):
    end = 0
    while not end:
        if data['state'] == "Inactive":
            print("\n=================================")
            print("\nSilly Meter not currently active!\n")
            timestamp_conversions(data)
            print("=================================")
            time.sleep(0.5)
        elif data['state'] == "Active" and data['winner'] == None:
            print("\n=================================")
            print("Silly Meter is active but reward not decided!")
            print("Potential Rewards & Descriptions:")
            print("=================================\n")
            current_rewards(data)
            print()
            timestamp_conversions(data)
        end = update_silly_meter_status()


def current_rewards(data):
    i = 0
    for reward in data['rewards']:
        print(reward + " | " + data['rewardDescriptions'][i])
        i += 1


def main():
    data = utils.error_checking_and_logging(URL, ENDPOINT)
    main_logic_loop(data)

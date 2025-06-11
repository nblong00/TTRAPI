import utils
import datetime
import time
from dateutil import relativedelta

URL = "https://www.toontownrewritten.com/api/sillymeter"
ENDPOINT = "(SIM)"


def timestamp_conversions(data):
    converted_starting_timestamp = (datetime.datetime.fromtimestamp(data["nextUpdateTimestamp"]))
    time_difference = relativedelta.relativedelta(converted_starting_timestamp,
                                                  datetime.datetime.now())
    if data["state"] == "Active" and data['winner'] == None:
        return_statement = f"Silly Points will be updated in {time_difference.minutes} minutes!"
        if time_difference.minutes <= 1:
            return_statement = f"Silly Points will be updated in 1 minute!"
    elif data["state"] == "Inactive":
        return_statement = f"Silly Meter will become active in {time_difference.minutes} minutes!"
        if time_difference.minutes <= 1:
            return_statement = f"Silly Meter will become active in 1 minute!"
    elif data["state"] == "Reward":
        return_statement = f"Silly Meter reward ends in {time_difference.minutes} minutes!"
        if time_difference.minutes <= 1:
            return_statement = f"Silly Meter reward ends in 1 minute!"
    print(return_statement)


def logic_loop(data):
    if data["state"] == "Inactive":
        print("=================================")
        print("\nSilly Meter not currently active!\n")
        timestamp_conversions(data)
        print("=================================")
        time.sleep(0.5)
    elif data["state"] == "Active" and data['winner'] == None:
        print("=================================")
        print("Silly Meter is active but reward not decided!")
        print("Potential Rewards & Descriptions:")
        print("=================================\n")
        current_rewards(data)
        print()
        timestamp_conversions(data)
        # print(data)


def current_rewards(data):
    i = 0
    for reward in data["rewards"]:
        print(reward + " | " + data["rewardDescriptions"][i])
        i += 1


def main():
    data = utils.error_checking_and_logging(URL, ENDPOINT)
    logic_loop(data)

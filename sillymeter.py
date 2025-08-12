from dateutil import relativedelta
import utils
import datetime
import time

URL = "https://www.toontownrewritten.com/api/sillymeter"
ENDPOINT = "(SIM)"


def current_rewards(data):
    i = 0
    for reward in data['rewards']:
        print(reward + " | " + data['rewardDescriptions'][i])
        i += 1


def timestamp_conversions(data):
    converted_starting_timestamp = (datetime.datetime.fromtimestamp(data['nextUpdateTimestamp']))
    time_difference = relativedelta.relativedelta(converted_starting_timestamp,
                                                  datetime.datetime.now())
    if data['state'] == "Active" and data['winner'] == None:
        return_statement = f"\rSilly Points will be updated in {time_difference.minutes} minutes!"
        if time_difference.minutes <= 1:
            return_statement = f"\rSilly Points will be updated in 1 minute!"
    elif data['state'] == "Inactive":
        return_statement = f"\rSilly Meter will become active in {time_difference.minutes} minutes!"
        if time_difference.minutes <= 1:
            return_statement = f"\rSilly Meter will become active in 1 minute!"
    elif data['state'] == "Reward":
        return_statement = f"\rSilly Meter reward ends in {time_difference.minutes} minutes!"
        if time_difference.minutes <= 1:
            return_statement = f"\rSilly Meter reward ends in 1 minute!"
    print(return_statement)


def update_silly_meter_status():
    refresh_status = input("Refresh Silly Meter Status (yes/no): \n> ")
    if refresh_status in ["yes", "ye", "y"]:
        time.sleep(0.5)
        return False
    elif refresh_status in ["no", "n"]:
        time.sleep(0.5)
        return True


def main_logic_loop(data):
    end = False
    while not end:
        if data['state'] == "Inactive":
            print("""
                  \r=================================
                  \rSilly Meter not currently active!
                  """, end=" ")
            timestamp_conversions(data)
            print("=================================\n")
        elif data['state'] == "Active" and data['winner'] == None:
            print("""
                  \r=================================
                  \rSilly Meter is active but reward not decided!
                  \rPotential Rewards & Descriptions:
                  \r=================================
                  """)
            current_rewards(data)
            print()
            timestamp_conversions(data)
        end = update_silly_meter_status()


def main():
    data = utils.error_checking_and_logging(URL, ENDPOINT)
    main_logic_loop(data)

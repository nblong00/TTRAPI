from dateutil import relativedelta
import pandas
import utils
import time
import datetime
import math

URL = "https://www.toontownrewritten.com/api/invasions"
ENDPOINT = "(INV)"


def welcome():
    print("\n-Welcome to the ToonTown Rewritten (TTR) Invasion Scanner-")
    print(f"It is currently {utils.dt()}\n")
    time.sleep(0.5)


def sorting_for_CSV(data):
    column_names = ["DistrictName", "Type", "Progress", "InvasionTimeoutIn"]
    utils.create_CSV_for_data(column_names)
    for district in data["invasions"]:
            if "Tele\u0003marketer" in data["invasions"][district]["type"]:
                data["invasions"][district]["type"] = "Telemarketer" 
            elif "Micro\u0003manager" in data["invasions"][district]["type"]:
                data["invasions"][district]["type"] = "Micromanager"
            elif "Blood\u0003sucker" in data["invasions"][district]["type"]:
                data["invasions"][district]["type"] = "Bloodsucker"
            data_to_write = [district, 
                            data["invasions"][district]["type"],
                            data["invasions"][district]["progress"],
                            remaining_invasion_time(data, district)]
            utils.write_data_to_CSV(data_to_write)


def remaining_invasion_time(data, district):
    converted_starting_timestamp = (datetime.datetime.fromtimestamp(data["invasions"][district]["startTimestamp"]))
    max_progress_value = int(data["invasions"][district]["progress"].split("/")[1])
    allowed_invasion_time = math.ceil((max_progress_value * 0.7) / 60)
    hours_left = 0
    minutes_left = 0
    if divmod(allowed_invasion_time, 60)[0] >= 1:
        hours_left = 1
        minutes_left = divmod(allowed_invasion_time, 60)[1]
        # Accounting for Mega-Invasions (time based)
        if max_progress_value == 1000000:
            hours_left = 3
            data["invasions"][district]["progress"] = "-Mega-Invasion-"
        invasion_end_time = (converted_starting_timestamp
                            + datetime.timedelta(hours = hours_left, 
                                                minutes = minutes_left))
    else:
        minutes_left = divmod(allowed_invasion_time, 60)[1]
        invasion_end_time = (converted_starting_timestamp
                            + datetime.timedelta(minutes = minutes_left))
    diff_now_end = relativedelta.relativedelta(invasion_end_time, 
                                                                    datetime.datetime.now())
    if diff_now_end.hours >= 1:
        time_in_invasion = f"{diff_now_end.hours} hour {diff_now_end.minutes} minutes"
        if diff_now_end.minutes in range(10):
            # Explicit double space on below line for formatting in command prompt
            time_in_invasion = f"{diff_now_end.hours} hour  {diff_now_end.minutes} minutes"
        return time_in_invasion
    elif diff_now_end.minutes <= 0:
        ending_message = "Invasion ending"
        return ending_message
    else:
        time_in_invasion = f"{diff_now_end.minutes} minutes"
        return time_in_invasion


def pull_API_data_again(end_program):
    for attempt in range(5):
        if attempt == 4:
            print("Too many invalid entries. Program closing...")
            end_program = 1
            return end_program
        user_input = input("> ")
        if user_input.lower() in ["no", "n"]:
            end_program = 1
            print("\nThank you for using the ToonTown Rewritten invasion scanner!")
            print("Program closing...")
            return end_program
        elif user_input.lower() not in ["no", "n", "yes", "y", "ye"] and attempt <= 2:
            print("Invalid entry. Would you like to check for new invasions? (yes/no)")
            continue
        elif user_input.lower() in ["yes", "y", "ye"] and attempt <= 3:
            print("\nPulling current invasions in ToonTown Rewritten...\n")
            end_program = 0
            time.sleep(1)
            return end_program


def main():
    end_program = 0
    welcome()
    while not end_program:
        data = utils.error_checking_and_logging(URL, ENDPOINT)
        utils.checking_if_error_is_active(data, ENDPOINT)
        sorting_for_CSV(data)
        result = pandas.read_csv("adjustedData.csv")
        print(result)
        print("\nDo you want to pull a new list of current invasions? (yes/no)")
        end_program = pull_API_data_again(end_program)
    time.sleep(1)


main()

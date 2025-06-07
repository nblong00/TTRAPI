import utils
import time

URL = "https://www.toontownrewritten.com/api/sillymeter"
ENDPOINT = "(SIM)"

def main():
    data = utils.error_checking_and_logging(URL, ENDPOINT)
    # print(data)
    utils.create_CSV_for_data(["State", "Winner", "RewardDescription", "ProjectedEndTime"])
    time.sleep(0.5)
    if data["state"] == "Inactive":
        print("=================================")
        print("\nSilly Meter not currently active!\n")
        print("=================================")
        time.sleep(0.5)
    else:
        print(data["rewards"][data["winner"]])
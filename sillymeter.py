import utils
import time
import pandas

URL = "https://www.toontownrewritten.com/api/sillymeter"
ENDPOINT = "(SIM)"


def main():
    data = utils.error_checking_and_logging(URL, ENDPOINT)
    if data["state"] == "Inactive":
        print("=================================")
        print("\nSilly Meter not currently active!\n")
        print("=================================")
        time.sleep(0.5)
        current_rewards(data)
        result = pandas.read_csv("adjustedData.csv")
        print(result)
    else:
        utils.create_CSV_for_data(["State", "Winner", "RewardDescription", "ProjectedEndTime"])
        print(data["rewards"][data["winner"]])


def current_rewards(data):
    i = 0
    utils.create_CSV_for_data(["PotentialReward", "RewardDescription"])
    for reward in data["rewards"]:
        utils.write_data_to_CSV([reward, data["rewardDescriptions"][i]])
        i += 1

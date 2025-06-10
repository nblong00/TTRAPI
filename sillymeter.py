import utils
import time

URL = "https://www.toontownrewritten.com/api/sillymeter"
ENDPOINT = "(SIM)"


def main():
    data = utils.error_checking_and_logging(URL, ENDPOINT)
    if data["state"] == "Inactive":
        print("=================================")
        print("\nSilly Meter not currently active!\n")
        print("=================================")
        time.sleep(0.5)
    elif data["state"] == "Active" and data['winner'] == None:
        print("=================================")
        print("Silly Meter is active but reward not decided!")
        print("Potential Rewards & Descriptions:")
        print("=================================\n")
        current_rewards(data)
        # print(data)


def current_rewards(data):
    i = 0
    for reward in data["rewards"]:
        print(reward + " | " + data["rewardDescriptions"][i])
        i += 1

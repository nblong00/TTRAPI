import utils

URL = "https://www.toontownrewritten.com/api/sillymeter"
ENDPOINT = "(SIM)"


data = utils.error_checking_and_logging(URL, ENDPOINT)
# print(data)
utils.create_CSV_for_data(["State", "Winner", "RewardDescription", "ProjectedEndTime"])

if data["state"] == "Inactive":
    print("=================================")
    print("\nSilly Meter not currently active!\n")
    print("=================================")
else:
    print(data["rewards"][data["winner"]])
import utils

URL = "https://www.toontownrewritten.com/api/sillymeter"
ENDPOINT = "(SIM)"


data = utils.error_checking_and_logging(URL, ENDPOINT)
print(data)
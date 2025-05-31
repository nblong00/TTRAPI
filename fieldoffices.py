import utils

URL = "https://www.toontownrewritten.com/api/fieldoffices"
ENDPOINT = "(FOS)"

data = utils.error_checking_and_logging(URL, ENDPOINT)
print(data)
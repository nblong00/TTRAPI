import requests
import utils
import pandas
import time

url = "https://www.toontownrewritten.com/api/population"
header = {"Content-Type":"application/json",
        "Accept-Encoding":"deflate",
        "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:138.0) Gecko/20100101 Firefox/138.0"}


def welcome():
    print("\n-Welcome to the ToonTown Rewritten (TTR) invasion scanner-")
    print(f"It is currently {utils.dt()}\n")
    time.sleep(0.5)


def get_API_write_csv(data):
    column_names = ["DistrictName",
                     "Population",
                     "Status"]
    utils.create_CSV_for_data(column_names)
    for district in data["populationByDistrict"]:
        json_fields = [district, 
                       str(data["populationByDistrict"][district]) + " Users",
                       data["statusByDistrict"][district].title()]
        data_to_write = json_fields
        utils.write_data_to_CSV(data_to_write)


def main():
    welcome()
    response = requests.get(url, headers=header)
    data = response.json()
    get_API_write_csv(data)
    result = pandas.read_csv("adjustedData.csv")
    print(result)

main()
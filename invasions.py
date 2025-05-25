import requests
import pandas
import utils

url = "https://www.toontownrewritten.com/api/invasions"
header={"Content-Type":"application/json",
        "Accept-Encoding":"deflate",
        "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:138.0) Gecko/20100101 Firefox/138.0"}


def main():
    response = requests.get(url, headers=header)
    data = response.json()
    utils.export_cleanedup_CSV_and_import(data)
    result = pandas.read_csv('adjustedData.csv')
    print(result)
    

main()
                 
import csv
import datetime
import requests
import logging
import os

logging.basicConfig(filename="api.log", level=logging.INFO)


def csv_new_line(csvfile: complex) -> None:
    lastchar = csvfile.read(1)
    if lastchar != "\n":
        csvfile.write("\n")


def dt() -> str:
    current_dt = datetime.datetime.now()
    dt_string = datetime.datetime.strftime(current_dt,
                                           "%I:%M%p on %m-%d-%Y")
    return dt_string


def convert_epoch_timestamp_string(data: complex) -> str:
    converted_epoch_timestamp = datetime.datetime.fromtimestamp(data['lastUpdated'])
    dt_string = datetime.datetime.strftime(converted_epoch_timestamp,
                                           "%I:%M%p on %m-%d-%Y")
    return dt_string


def create_csv_for_data(column_names: list[str]) -> None:
    with open("adjustedData.csv", "w+", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=",", lineterminator="")
        writer.writerow(column_names)
        csv_new_line(csvfile)


def write_data_to_csv(write_data: complex) -> None:
    with open("adjustedData.csv", "a+", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=",", lineterminator="")
        writer.writerow(write_data)
        csv_new_line(csvfile)


def delete_csv_from_system():
    os.remove("adjustedData.csv")


def error_checking_and_logging(url: str, endpoint: str) -> complex:
    header = {"Content-Type":"application/json",
        "Accept-Encoding":"deflate",
        "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:138.0) Gecko/20100101 Firefox/138.0"}
    response = requests.get(url, headers=header)
    if response.status_code != 200:
            logging.warning(f"{endpoint} {dt()} - Response code received: {response.status_code}")
            print(f"{endpoint} API responded with an unsuccessful {response.status_code} code.")
    else:
        logging.info(f"{endpoint} {dt()} -  Response code received: {response.status_code}")
    try:
        data = response.json()
        if endpoint != "(SIM)":
            logging.info(f"{endpoint} API data updated from central TTR server at {convert_epoch_timestamp_string(data)}")
        return data
    except requests.exceptions.JSONDecodeError:
        logging.error(f"{endpoint} {dt()} - API JSON may be malformed. We were unable to extract data from the response.")
        input("Press ENTER to close program...")
        exit()

def checking_if_error_is_active(data: complex, endpoint: str) -> None:
    if data["error"] != None:
        print("Error relayed via API.")
        print("Documenting error in logs...")
        logging.error(f"{endpoint} {dt()} - API is reporting error in payload: {data['error']}")
        input("Press ENTER to close...")
        exit()

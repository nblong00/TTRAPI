import csv
import datetime


def csv_new_line(csvfile):
    lastchar = csvfile.read(1)
    if lastchar != '\n':
        csvfile.write('\n')


def dt():
    current_dt = datetime.datetime.now()
    dt_string = datetime.datetime.strftime(current_dt, "%I:%M%p on %m-%d-%Y")
    return dt_string


def convert_epoch_timestamp_string(data):
    converted_epoch_timestamp = datetime.datetime.fromtimestamp(data["lastUpdated"])
    dt_string = datetime.datetime.strftime(converted_epoch_timestamp, "%I:%M%p on %m-%d-%Y")
    return dt_string


def create_CSV_for_data(column_names):
    with open("adjustedData.csv", "w+", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=",", lineterminator="")
        writer.writerow(column_names)
        csv_new_line(csvfile)


def write_data_to_CSV(write_data):
    with open("adjustedData.csv", "a+", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=",", lineterminator="")
        writer.writerow(write_data)
        csv_new_line(csvfile)

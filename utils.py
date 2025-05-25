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

def convert_epoch_timestamp(data):
    converted_epoch_timestamp = datetime.datetime.fromtimestamp(data["lastUpdated"])
    dt_string = datetime.datetime.strftime(converted_epoch_timestamp, "%I:%M%p on %m-%d-%Y")
    return dt_string

def export_cleanedup_CSV_and_import(data):
    with open('adjustedData.csv', 'w+', newline='') as csvfile:
        reader = csv.reader(csvfile)
        writer = csv.writer(csvfile, delimiter=',', lineterminator='')
        writer.writerow(['DistrictName', 'Type', 'Progress'])
        csv_new_line(csvfile)
        for district in data['invasions']:
            if 'Tele\u0003marketer' in data['invasions'][district]['type']:
                data['invasions'][district]['type'] = "Telemarketer" 
            elif 'Micro\u0003manager' in data['invasions'][district]['type']:
                data['invasions'][district]['type'] = "Micromanager"
            else:
                pass
            writer.writerow([district, 
                            data['invasions'][district]['type'],
                            data['invasions'][district]['progress']])
            csv_new_line(csvfile)

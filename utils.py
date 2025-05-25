import csv


def csv_new_line(csvfile):
    lastchar = csvfile.read(1)
    if lastchar != '\n':
        csvfile.write('\n')


def export_cleanedup_CSV_and_import(data):
    with open('adjustedData.csv', 'w+', newline='') as csvfile:
        reader = csv.reader(csvfile)
        writer = csv.writer(csvfile, delimiter=',', lineterminator='')
        first_row = next(reader, None)
        if first_row and first_row[0] == 'districtName':
            pass
        else:
            writer.writerow(['districtName', 'type', 'progress'])
            csv_new_line(csvfile)
        for district in data['invasions']:
            writer.writerow([district, 
                            data['invasions'][district]['type'],
                            data['invasions'][district]['progress']])
            csv_new_line(csvfile)

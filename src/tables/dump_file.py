import csv


def dump_file(file, headers, rows):
    with open(file, 'w') as f:
        writer = csv.writer(f, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow(headers)
        writer.writerows(rows)

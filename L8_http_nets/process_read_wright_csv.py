import csv
def read_csv_cars():
    with open('cars.csv') as f:
        csv_reader = csv.reader(f, delimiter=',')
        lines_count = 0
        print("csv_reader:", csv_reader)
        for row in csv_reader:
            # print(repr(row))
            if lines_count == 0:
                print("Columns:", " | ".join(row))
            else:
                # print("values:",', '.join(row))
                print(f"Car from {row[0]} by {row[1]} ({row[2]}) [{row[3]}] ${row[4]}")
            lines_count += 1
        print("Read", lines_count, 'lines.')

def read_csv_cars_to_dict():
    with open('cars.csv') as f:
        csv_reader = csv.DictReader(f, delimiter=',')
        lines_count = 0
        print("csv_reader", csv_reader)
        for row in csv_reader:
            # print(repr(row))
            if lines_count == 0:
                print("Columns:", " | ".join(row.keys()))
            print(f"Car from {row['year']} by {row[' vendor']} ({row[' name']}) [{row[' comment']}] ${row[' price']}")
            lines_count += 1
        print("Got", lines_count, 'data lines.')

def write_csv_dict():
    FIELD_NAME = "name"
    FIELD_DEPARTMENT = "department"
    FIELD_BM = "birth month"
    with open("employee_birth_month.csv", "w") as f:
        fieldnames = [
            FIELD_NAME,
            FIELD_DEPARTMENT,
            FIELD_BM,
        ]
        csv_writer = csv.DictWriter(f,
                                    fieldnames=fieldnames,
                                    # delimiter=",",
                                    # quotechar='"',
                                    # quoting=csv.QUOTE_MINIMAL,
                                    )
        csv_writer.writeheader()
        csv_writer.writerow({
            FIELD_NAME : 'John Smith',
            FIELD_DEPARTMENT : 'IT Department',
            FIELD_BM : 'march',
        })

        csv_writer.writerow({
            FIELD_NAME : 'Ann White',
            FIELD_DEPARTMENT : 'Accounting',
            FIELD_BM : 'may',
        })

        #quote chars
        csv_writer.writerow({
            FIELD_NAME : 'Ann Black',
            FIELD_DEPARTMENT : 'Accounting,Management',
            FIELD_BM : '',
        })

if __name__ == '__main__':
    # read_csv_cars()
    # print('-'*10)
    # read_csv_cars_to_dict()
    write_csv_dict()
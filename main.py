# libraries / packages
import csv
import json
import sys
import argparse


# constructs the argument parser and parses the arguments
def get_args():
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--input_file", required=True,
                    help="filepath to csv", type=str)
    ap.add_argument("-c", "--country_code", required=True,
                    help="two digit country code", type=str)

    args = ap.parse_args()

    return args.input_file, args.country_code


# takes each hotel instances in the csv (filepath) input and translates it into
# a dictionary definitoin held in the data dict as a hotel value
def dict_create(arguments):
    print(arguments[0])
    filepath = arguments[0]
    country = arguments[1]

    data = {}   # creation of empty dict to hold hotel values
    data["hotel"] = []

    with open(filepath, encoding='mac_roman') as csv_file:
        read_csv = csv.reader(csv_file)
        fields = next(read_csv)
        for row in read_csv:
            data["hotel"].append({
                "cityCode": "%s" % row[5],
                "name": "%s" % row[0],
                "url": "https://www.booking.com/hotel/%s/%s.html?"
                % (country, row[1]),
                "nokenQuality": "%s" % row[2],
                "nokenType": "%s" % row[3],
                "neighborhood": "%s" % row[4]
                })

    print("DICTIONARY CREATED ✅")
    return data


# converts data dict into a JSON stored in the output file "hotels.json"
def json_create(dict):
    with open('hotels.json', 'w') as outfile:
        json.dump(dict["hotel"], outfile, ensure_ascii=False)

    print("DICTIONARY CONVERTED TO JSON ✅")
    confirmation()


# confirms completion of full translation
def confirmation():
    print("CSV to JSON conversion is Complete 🥳")
    print("check the csvConverter folder for a file named hotels.json")
    print(
        "please rename the file before running the script again or it will be"
        " deleted"
        )


if __name__ == "__main__":
    arguments = get_args()
    json_create(dict_create(arguments))

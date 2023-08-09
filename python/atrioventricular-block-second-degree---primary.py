# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"3297.00","system":"readv2"},{"code":"102330.0","system":"med"},{"code":"102553.0","system":"med"},{"code":"103752.0","system":"med"},{"code":"10922.0","system":"med"},{"code":"19060.0","system":"med"},{"code":"27928.0","system":"med"},{"code":"36629.0","system":"med"},{"code":"40118.0","system":"med"},{"code":"93216.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('atrioventricular-block-second-degree-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["atrioventricular-block-second-degree---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["atrioventricular-block-second-degree---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["atrioventricular-block-second-degree---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)

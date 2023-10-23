import csv

input_file = 'data/Sam_num.csv'  # replace with your input file name
output_file = 'output.csv'  # replace with your output file name


def delete_empty_rows(input_file, output_file):
    with open(input_file, newline='', encoding='utf-8') as infile, open(output_file, 'w', newline='',
                                                                        encoding='utf-8') as outfile:
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)

        # Write the headers to the output file
        writer.writeheader()

        for row in reader:
            # Check if the "Numbers" column is empty
            if row['Numbers']:
                # If not empty, write the row to the output file
                writer.writerow(row)


# Call the function
delete_empty_rows(input_file, output_file)

import csv

def capitalize_first_letters(text):
    return ' '.join(word.capitalize() for word in text.split())


def convert_csv(input_filename, output_filename):
    with open(input_filename, 'r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)

        with open(output_filename, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile, delimiter=',')
            for row in reader:
                writer.writerow(row)
    clean_information_to_text(output_filename)


def clean_information_to_text(filename):
    with open(filename[:-4] + '.csv', 'r') as csvfile:
        with open(filename[:-4] + '_converted.txt', 'w') as outfile:
            csvreader = csv.reader(csvfile)
            t = 0
            for row in csvreader:
                if len(row) > 1 and t > 2:
                    names_to_capitalize = [row[i] for i in range(4, 9) if len(row[i]) > 2]
                    if names_to_capitalize:
                        modified_names = [capitalize_first_letters(name.strip()) for name in names_to_capitalize]
                        outfile.write(' '.join(modified_names) + ' ')
                    outfile.write(capitalize_first_letters(row[3].strip()) + ' ')
                    outfile.write(capitalize_first_letters(row[11].strip()) + ' ')
                    outfile.write(capitalize_first_letters(row[12].strip()) + '\n')
                t += 1


convert_csv('./data/Sam400bdd.csv', './data/boulangerie_information_sam.csv')
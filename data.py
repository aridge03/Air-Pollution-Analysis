import csv

# Specify the input file name
input_file = "global air pollution dataset.csv"
# Specify the output file name for the new CSV file
output_file = "first_40_lines.csv"

# Read the first 40 lines from the CSV file
with open(input_file, "r", newline="", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    rows_to_keep = [next(reader) for _ in range(40)]

# Write the first 40 lines to the new CSV file
with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(rows_to_keep)

print("The first 40 lines of 'game_info.csv' have been saved to 'first_40_lines.csv'")
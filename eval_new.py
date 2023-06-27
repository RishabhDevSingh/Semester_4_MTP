import csv

# Read pred.csv file and store combinations
pred_combinations = []
with open('pred.csv', 'r') as pred_file:
    reader = csv.reader(pred_file)
    next(reader)  # Skip header row
    for row in reader:
        mention_id = row[1]
        concept_id = row[4]
        combination = (mention_id, concept_id)
        pred_combinations.append(combination)

# Read gold.csv file and store combinations
gold_combinations = []
with open('gold.csv', 'r') as gold_file:
    reader = csv.reader(gold_file)
    next(reader)  # Skip header row
    for row in reader:
        mention_id = row[1]
        concept_id = row[4]
        combination = (mention_id, concept_id)
        gold_combinations.append(combination)

# Compare the combinations and find the missing ones
missing_combinations = []
for combination in pred_combinations:
    if combination not in gold_combinations:
        missing_combinations.append(combination)

# Calculate accuracy
total_rows = len(pred_combinations)
accuracy = 1 - (len(missing_combinations) / total_rows)

# Write the missing combinations to a text file
with open('missing_combinations.txt', 'w') as output_file:
    for combination in missing_combinations:
        output_file.write(f"Combination {combination} is present in pred.csv but not in gold.csv\n")

# Write accuracy value to a text file
with open('accuracy.txt', 'w') as accuracy_file:
    accuracy_file.write(f"Accuracy: {accuracy}\n")

import csv

def separate_entries(pred_file):
    # Read pred.csv and sort entries based on score column
    with open(pred_file, 'r') as pred_csv:
        pred_data = list(csv.DictReader(pred_csv))
        pred_data.sort(key=lambda x: float(x['score']))

        # Create and write separate CSV files for each score range
        score_ranges = [('0.90-0.99', 0.9, 1.0), ('0.80-0.90', 0.8, 0.9), ('0.70-0.80', 0.7, 0.8)]
        for range_name, min_score, max_score in score_ranges:
            range_filename = f"{range_name}.csv"
            with open(range_filename, 'w', newline='') as range_csv:
                fieldnames = pred_data[0].keys()
                writer = csv.DictWriter(range_csv, fieldnames=fieldnames)
                writer.writeheader()

                for row in pred_data:
                    score = float(row['score'])
                    if min_score <= score < max_score:
                        writer.writerow(row)

# Example usage
pred_file = 'pred.csv'
separate_entries(pred_file)

import json







































data = '[' + data + ']'

# Load the data as a JSON array
json_array = json.loads(data)

# Extract and print the "text" fields from each object in the array
data_out=""

count=0
for sublist in json_array:
    for item in sublist:
        count=count+1
        data_out=data_out+("Mention_id -")+(item['mention_id'])+(" text -")+ (item['text'])+(" Doc Id ")+(item['content_document_id'])+("\n")

print (count)
# Open the file in write mode
#print(data_out)
with open("output.txt", "w") as file:
    # Write the data to the file
    file.write(data_out)

# Output saved to file
print("Data saved to output.txt")


#code to fetch mentions details in text set











data_test = '[' + data_test + ']'

# Load the data as a JSON array
json_array = json.loads(data_test)

# Extract and print the "text" fields from each object in the array
data_out_test=""

count_test=0
for sublist in json_array:
    for item in sublist:
        count_test=count_test+1
        data_out_test = data_out_test+("Mention_id -")+(item['mention_id'])+(" text -")+ (item['text'])+(" Doc Id ")+(item['content_document_id'])+("\n")

print (count_test)
# Open the file in write mode
#print(data_out)
with open("output_test.txt", "w") as file:
    # Write the data to the file
    file.write(data_out_test)

# Output saved to file
print("Data saved to output.txt")

        

##   # Write the data to the file
 #   file.write(data)
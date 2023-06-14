import csv
import time
import psutil

# Start to calculate the time
begin = time.time()

# Getting the data from CSV file
with open("french_dictionary.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    translated_dict = {}
    
    for row in csv_reader:
        translated_dict[row[0].strip()] = row[1].strip()
        
# Counting and replacing the english words from the given txt file.
with open("t8.shakespeare.txt", "r") as file:
    data = file.read()
    new_data = []

    for word in translated_dict.keys():
        replaced = translated_dict[word]
        count = data.count(word)
        data = data.replace(word, replaced)
        upper_word, upper_replaced = word.capitalize(), replaced.capitalize()
        count += data.count(upper_word)
        data = data.replace(upper_word, upper_replaced)
        if count > 0:
            new_data.append([word, replaced, count])

# Wrting the translated data into a new file.
with open("t8.shakespeare.translated.txt", "w") as new_file:
    new_file.write(data)

# Creating a new CSV file for number of replacements.
with open("frequency.csv", "w", newline='') as new_csv:
    csv_writer = csv.writer(new_csv, delimiter=",")

    header = ["English Word", "French Word", "Frequency"]

    csv_writer.writerow(header)
    csv_writer.writerows(new_data)

# Calculating the time and memory taken by the script.
total_time = int(time.time() - begin)
total_memory = round(psutil.Process().memory_info().rss / (1024 * 1024), 3)

# Writing the data into the file.
with open("performance.txt", "w") as performance:
    performance.write("Time to process: 0 minutes {0} seconds\nMemory used: {1} MB".format(total_time, total_memory))
    
print("Time to process: 0 minutes {0} seconds\nMemory used: {1} MB".format(total_time, total_memory))
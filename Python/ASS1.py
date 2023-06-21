def count_words(file_name):
    file = open(file_name, 'r')
    data = file.read()
    file.close()

    # Normalize to lowercase and replace non-alphanumeric characters with spaces
    cleaned_data = ""
    for ch in data:
        if ch.isalnum() or ch.isspace():
            cleaned_data += ch.lower()
        else:
            cleaned_data += " "
        
    # Split the text into words
    words = cleaned_data.split()
        
    # Count the frequency of each word
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
        
    # Sort the words by frequency
    items = list(word_counts.items())
    for i in range(len(items)):
        for j in range(i, len(items)):
            if items[i][1] < items[j][1]:
                items[i], items[j] = items[j], items[i]
        
    return items

def save_report(word_counts, report_file):
    file = open(report_file, 'w')
    # Write each word and its frequency to the report file
    for pair in word_counts:
        line = pair[0] + ": " + str(pair[1]) + "\n"
        file.write(line)
    file.close()

def main():
    file_name = "/Users/abhijithnair/Downloads/python automation /sample.txt"
    report_file = "/Users/abhijithnair/Downloads/python automation /reports.txt"
    
    word_counts = count_words(file_name)
    save_report(word_counts, report_file)
    print("Report saved successfully!")

if __name__ == "__main__":
    main()

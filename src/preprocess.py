import re

def remove_file_uploads(text):
    return re.sub(r'\[.*?\]\(.*?\)', '', text)

def remove_hyperlinks(text):
    return re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text)

def is_deleted_removed(text):
    return text == '[deleted]' or text == '[removed]'

# Remove blank lines and strip lines
# Remove hyperlinks, `[deleted]`, `[removed]`, [file](filename)
def preprocess(input_file, output_file):
    with open(input_file, 'r') as in_file:
        with open(output_file, 'w') as out_file:
            for line in in_file:
                # Check if the line is not empty or contains only whitespace
                line = line.strip()
                if not line or is_deleted_removed(line):
                    continue

                # Note that order possibly matters!
                line = remove_file_uploads(line)
                line = remove_hyperlinks(line)

                # If line is blank after processing, skip
                line = line.strip()
                if not line:
                    continue

                out_file.write(line + '\n')

if __name__ == "__main__":
    file_name = "AskReddit"
    input_file_path = f"../data/{file_name}.txt"
    output_file_path = f"../data/{file_name}_processed.txt"

    preprocess(input_file_path, output_file_path)
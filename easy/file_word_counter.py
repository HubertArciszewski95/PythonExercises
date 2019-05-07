# Download the words1.txt file from the attachment and then create a Python function
# that takes a text file as input and returns the number of words contained in the text file.


def word_counter(data):
    read_data = data.read()
    split_data = read_data.split()
    return len(split_data)


with open("/Users/hubertarciszewski/Downloads/words1.txt", "r") as data:
    print(word_counter(data))

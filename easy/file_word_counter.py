# Download the words1.txt file from the attachment and then create a Python function
# that takes a text file as input and returns the number of words contained in the text file.
# Please take into consideration that some words can be separated by a comma with no space.
# For example "Hi,it's me." would need to be counted as three words.


def word_counter(data):
    read_data = data.read().replace(",", " ")
    split_data = read_data.split()
    return len(split_data)


with open("/Users/hubertarciszewski/Downloads/words2.txt", "r") as data:
    print(word_counter(data))

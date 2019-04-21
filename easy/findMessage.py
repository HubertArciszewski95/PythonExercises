# You are given a chunk of text.
# Gather all capital letters in one word in the order that they appear in the text.


# First solution
def find_message(msg):
    secret = ""
    for x in msg:
        if x == x.upper() and x.isalpha():
            secret += x
    return secret


# Second solution
def find_message2(msg):
    z = [x for x in msg if x == x.upper() and x.isalpha()]
    return "".join(z)


print(find_message("How are you? Eh, ok. Low or Lower? Ohhh.")) # "HELLO"
print(find_message("hello world!")) # "", "Nothing"
print(find_message("HELLO WORLD!!!"))  # HELLOWORLD", "Capitals"

letters = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
shift = 1
message = raw_input("Enter a message\n")
msgout = ""

for i in message:
    msgout += letters[letters.index(i) + shift]
print msgout



# Word_Count_Test

# Get the name of the file and open it
name = input('Enter the file: ')
handle = opent(name, 'r')

# Count word frecuency
counts = dict()
for line in handle:
    words = line,split()
    for word in words:
        counts(word) = counts.get(word, 0) + 1

# Find the most common word
bigcount = None
bigwoword = None
for word in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

# Print result
print(bigword, bigcount)
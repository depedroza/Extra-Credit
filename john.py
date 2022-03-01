# Renamed file for easier typing
# Program assumes txt file in same folder as .py

john_infile = open("John.txt", "r")

search = ["Father", "God", "Christ", "Spirit", "spirit", "life", "man"]
john_list = [line.rstrip("\n").split() for line in john_infile]

searches = {}
for line in john_list:
    for word in search:
        searches[word] = str(line.count(word))

for key in searches:
    print(key + ": " + searches[key])

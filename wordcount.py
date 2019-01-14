# put your code here.
file = open("test.txt", "r")
# print(file.read())


def word_count(file):

    word_count = {}


    for line in file: 
        line_strip = line.rstrip()
        line_split = line_strip.split(" ")
        for word in line_split:
            # if "," in word:
            #     word = word.replace(",", "")
            # elif "." in word:
            #     word = word.replace(".", "")
            # elif "?" in word:
            #     word = word.replace("?", "")

            word_count[word] = word_count.get(word, 0) + 1

    for word, count in word_count.items():
        print(f"{word} {count}")

word_count(file)
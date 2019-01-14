# put your code here.

def word_count(file):
    file = open(file, "r")

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

    file.close()

word_count("test.txt")
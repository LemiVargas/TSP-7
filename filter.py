# This is the dictionary for the most common words used on wikipedia. We can use this for when we make comparisons between
# Wikipedia pages, and ignore these words to not skew the similarity results.
def main():
    word_filter = read_text('/Users/jackson/PycharmProjects/pythonProject/commonwords.txt')
    print(word_filter)


def read_text(file_name):
    file_data = []
    text_file = open(file_name, "r")

    for word in text_file.read().split():
        file_data.append(word)

    text_file.close()
    return file_data


if __name__ == "__main__":
    main()

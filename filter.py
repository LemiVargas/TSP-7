# This is the dictionary for the most common words used on wikipedia. We can use this for when we make comparisons between
# Wikipedia pages, and ignore these words to not skew the similarity results.
def main():
    test_list = ["Hi", "The", "Michigan"]
    print(test_list)
    test_list = filter_words(test_list)
    print(test_list)


def filter_words(page_words: list[str]) -> list:

    """
    Given a list, remove any occurrences of the 100 most common english words
    :param page_words:
    :return: a list with the 100 most common english words filtered out
    """

    word_filter = read_text('commonwords.txt')
    filtered = []
    for word in page_words:

        if word.lower() not in word_filter:
            filtered.append(word)
    return filtered


def read_text(file_name):
    file_data = []
    text_file = open(file_name, "r")

    for word in text_file.read().split():
        file_data.append(word)

    text_file.close()
    return file_data


if __name__ == "__main__":
    main()

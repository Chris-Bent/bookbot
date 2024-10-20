def main():
    bookPath = "books/frankenstein.txt"
    text = getText(bookPath)
    numWords = numOfWords(text)
    print(f"{numWords} words found in the document")


def numOfWords(text):
    words = text.split()
    return len(words)


def getText(path):
    with open(path) as f:
        return f.read()


main()


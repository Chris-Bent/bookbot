def main():
    bookPath = "books/frankenstein.txt"
    print(f"-------------------- Report on {bookPath} --------------------")
    text = getText(bookPath)
    numWords = numOfWords(text)
    characterString = text.lower() 
    characterCount = countCharacters(characterString)
    #characterList = [{key: value} for key, value in characterCount.items()]
    print(f"--- {numWords} words found in the document ---")
    for key, value in characterCount.items(): 
        print(f"--- The {key}: character was found {value} times ---")

    print("-------------------- End report --------------------")

# Take text and split into words, return the length of the list.
def numOfWords(text):
    words = text.split()
    return len(words)

# Access and read documents to be analysed. 
def getText(path):
    with open(path) as f:
        return f.read()

# CountCharacters
# Initialise new dict
# for each character in characterString
    # if character in dictionary add one to count
    # else add the character and start count at 1
def countCharacters(characterString):
    characterCount = {}
    for char in characterString:
        if char in characterCount:
            characterCount[char] += 1
        else:
             characterCount[char] = 1
    return characterCount
     


main()

# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content():
    # [assignment] Add your code here
    with open('story.txt') as data:
        #read file into contents
        contents = data.read()

    return contents


def count_words():
    #Set content of file into text, create empty dictionary
    text = read_file_content()
    counts = dict()
    words = text.split()
    # [assignment] Add your code here
    #Iterate over each word and increase counts if find dublicate
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
print(count_words())
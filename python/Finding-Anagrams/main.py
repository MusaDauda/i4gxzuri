# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

def find_anagram(word, anagram):
    # [assignment] Add your code here
    #convert string to lowercase
    word = word.lower()
    anagram = anagram.lower()
    #check for the equality of both string length
    if (len(word)) == (len(anagram)):
        #sort the strings
        sorted_word = sorted(word)
        sorted_anagram = sorted(anagram)
        if (sorted_word == sorted_anagram):
            print("True")   #comment this code if you will be using "print(find_anagram("Santa", "Satan"))"
            return True     #comment this code if you will be using "find_anagram("Santa", "Satan")" or leave it.
        else:
            print("False")      #comment this code if you will be using "print(find_anagram("Santa", "Satan"))"
            return False        #comment this code if you will be using "find_anagram("Santa", "Satan")" or leave it


find_anagram("Santa", "Satan")
#print(find_anagram("Santa", "Satan"))
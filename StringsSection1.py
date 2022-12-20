# StringsSection1
# Cooper Cross
# 12/12/19

message = input("Enter a message or word: ").lower()

def vowelCount(string):
    vowel1 = string.count("a")
    vowel2 = string.count("e")
    vowel3 = string.count("i")
    vowel4 = string.count("o")
    vowel5 = string.count("u")
    
    vowels = vowel1+vowel2+vowel3+vowel4+vowel5
    
    print("The vowel count is "+str(vowels))

vowelCount(message)
    

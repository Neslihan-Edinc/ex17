def letter_count(text):
    letters=("qwertyuıopasdfghjklzxcvbnm")
    letter_count=0
    for char in text.lower():
        if char in letters:
            letter_count+=1
    return letter_count
def find_the_longest_word(text):
    words=text.split()
    longest_word=None
    for word in words:
        if longest_word is None or len(word)>len(longest_word):
            longest_word=word
    return longest_word
user_input=input("enter a text: ")
print(f"the longest word is : {find_the_longest_word(user_input)}")



        








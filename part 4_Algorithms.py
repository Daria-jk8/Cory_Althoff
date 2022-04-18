# 1. --> FizzBuzz

def fizz_buzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)        

fizz_buzz()            

# 2. --> Sequential Search

def ss(number_list, n):
    found = False
    for i in number_list:
        if i == n:
            found = True
            break
    return found

numbers = range(0, 100)
s1 = ss(numbers, 2)
print(s1, "<--")

s2 = ss(numbers, 202)
print(s2, "<--")

# 3. --> Palindrome

def palindrome(word):
    word = word.lower()
    return word[::-1] == word

print(palindrome('Python'))
print(palindrome("Radar"))
print(palindrome("Malayalam"))

"""Malayalam is a Dravidian language spoken in the Indian state of Kerala 
and the union territories of Lakshadweep and Puducherry by the Malayali people. 
It is one of 22 scheduled languages of India and is spoken by 2.88% of Indians.
"""
# RACECAR, REFER, MADAM, level, kayak, noon, deed

# 4. --> Anagram

def anagram(w1, w2):
    w1 = w1.lower()
    w2 = w2.lower()
    return sorted(w1) == sorted(w2)

print(anagram('listen', 'silent'), '<--')    
print(anagram('race', 'care'))  
print(anagram('april', 'may'))  

# 5. --> Count occurrences of characters

def count_characters(string):
    count_dict = {}
    for c in string:
        if c in count_dict:
            count_dict[c] += 1
        else:
            count_dict[c] = 1
    print(count_dict)    

count_characters('Google')           
count_characters('Psychotomimetic')  

# 6. --> Recursion

""""a function can call other functions. It is even possible for the function to call itself. 
These types of construct are termed as recursive functions. """

# https://en.wikipedia.org/wiki/99_Bottles_of_Beer
#  https://www.youtube.com/watch?v=_Y3CtecroEY&ab_channel=Melvins-Topic

def bottles_of_beer(bob):
    if bob < 1:
        print("""No more bottles of beer on the wall. No more bottles of beer.""")
        return 
    tmp = bob
    bob -= 1 
    print("""{} bottles of beer on the wall. {} bottles of beer. 
          Take one down and pass it around, {} bottles of beer on the wall.
          """.format(tmp, 
                     tmp, 
                     bob))
    
    bottles_of_beer(bob)

bottles_of_beer(99)    



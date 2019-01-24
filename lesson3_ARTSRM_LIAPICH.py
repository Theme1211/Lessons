


'''
Ex3
In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

Example:

high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 9 3 4 -5") # return "9 -5"
Notes:

All numbers are valid Int32, no need to validate them.
There will always be at least one number in the input string.
Output string must be two numbers separated by a single space, and highest number is first.
'''


def high_and_low(numbers):
    # Your code here
    return
    
    
assert high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6") == "542 -214"
assert high_and_low("1 2 -3 4 5") == "5 -3"


l = [1, 2, 3, 4, 5, 6]
while True:

    try:
        enter = int(input('enter a number or Enter to finish: '))
        l.append(enter)
    except:
        break

print('max = ', max(l), 'min = ', min(l), 'summ =', sum(l), 'avg = ', sum(l) / len(l))


'''
Ex4
Jaden Smith, the son of Will Smith, is the star of films such as The Karate Kid (2010) and After Earth (2013). 
Jaden is also known for some of his philosophy that he delivers via Twitter. 
When writing on Twitter, he is known for almost always capitalizing every word.

Your task is to convert strings to how they would be written by Jaden Smith. 
The strings are actual quotes from Jaden Smith, but they are not 
capitalized in the same way he originally typed them.

Example:

Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"
'''


def toJadenCase(string):
    # Your code here
    return
    

assert toJadenCase("How can mirrors be real if our eyes aren't real") == "How Can Mirrors Be Real If Our Eyes Aren't Real"


s = 'How can mirrors be real if our eyes are'
print(s.title())

'''
Ex5
Implement a function that adds two numbers together and returns their sum in binary. 
The conversion can be done before, or after the addition.

The binary number returned should be a string
'''


def add_binary(a,b):
    #your code here
    return
    
    
assert add_binary(1,1) == "10"
assert add_binary(0,1) == "1"
assert add_binary(1,0) == "1"
assert add_binary(2,2) == "100"
assert add_binary(51,12) == "111111"



x = int(input("натуральное число: "))
n = ""

while x > 0:
    y = str(x % 2)
    n = y + n
    x = int(x / 2)

print(n)
'''
Ex6*
Complete the function that counts the number of unique consonants in a string (made up of printable ascii characters).

Consonants are letters used in English other than "a", "e", "i", "o", "u". We will count "y" as a consonant.

Remember, your function needs to return the number of unique consonants - disregarding duplicates. 
For example, if the string passed into the function reads "add", 
the function should return 1 rather than 2, since "d" is a duplicate.

Similarly, the function should also disregard duplicate consonants of differing cases. 
For example, "Dad" passed into the function should return 1 as "d" and "D" are duplicates.

Examples

"add" ==> 1
"Dad" ==> 1
"aeiou" ==> 0
"sillystring" ==> 7
'''


def count_consonants(text):
    # Your code here
    return
    
    
assert count_consonants('sillystring') == 7
assert count_consonants('aeiou') == 0
assert count_consonants('abcdefghijklmnopqrstuvwxyz') == 21
assert count_consonants('Count my unique consonants!!') == 7


import re

res = re.findall('([бвгджзйклмнпрстфхцчшщ])', 'паааыьдлпьыдлвп аываывпываыа')
res.sort()
print(res)

'''
Ex7
Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. 
Return the resulting string.
'''


def fake_bin(x):
    # Your code here
    return
    
    
tests = [
    # [expected, input]
    ["01011110001100111", "45385593107843568"],
    ["101000111101101", "509321967506747"],
    ["011011110000101010000011011", "366058562030849490134388085"],
    ["01111100", "15889923"],
    ["100111001111", "800857237867"],
]

for exp, inp in tests:
    assert fake_bin(inp) == exp


st = []

print("Ввведите Числа:")
for i in range(12):
    st.append(eval(input()))
    if st[i] >= 5:
        st[i] = 1
    elif st[i] < 5:
        st[i] = 0

print(st)

'''


Ex9
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Note: If the number is a multiple of both 3 and 5, only count it once.
'''


def solution(number):
    # Your code here
    return
    
    
assert solution(10) == 23


s = 0
for value in range(1, 10):
    if value % 3 == 0 or value % 5 == 0:
        s += value
        print("ЧИСЛО", value)
print(s)


'''
Ex10
My grandfather always predicted how old people would get, and right before he passed away he revealed his secret!

In honor of my grandfather's memory we will write a function using his formula!

Take a list of ages when each of your great-grandparent died.
Multiply each number by itself.
Add them all together.
Take the square root of the result.
Divide by two.
Example

predict_age(65, 60, 75, 55, 60, 63, 64, 45) == 86
Note: the result should be rounded down to the nearest integer.
'''


def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    # your code here
    return
    
    
assert predict_age(65,60,75,55,60,63,64,45) == 86


a = (1, 2, 3)
x = sum(a)
print(x ** 0.5/2)

'''
Ex11
Complete the function so that it takes an array of keys and a default value and returns a dictionary 
with all keys set to the default value.

Example

["draft", "completed"], 0   # should return {"draft": 0, "completed: 0}
'''


def populate_dict(keys, default):
    # your code here
    return
    
    
assert populate_dict(["draft", "completed"], 0) == {"completed": 0, "draft": 0}
assert populate_dict(["a", "b", "c"], None) == {"c": None, "b": None, "a": None}
assert populate_dict([1, 2, 3, 4], "OK") == {1: "OK", 2: "OK", 3: "OK", 4: "OK"}

d = {20: '1', '2': 2, 3: '3',}


def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k


print(get_key(d, '1'))
print(get_key(d, 2))
print(get_key(d, 42))

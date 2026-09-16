"""
message = "\tHello Python"
print(message)

name = "\tfavour nya"
print(name.upper())

age = "20"
details = f"{name} \n\t{age}"
print(details)

print(4*5)
print(4**3)
"""
print("what is your name")
name = input()
print("my name is " + name)
print(64//3)
print(3**3)
num1 = input("pick a number: ")
print("pick another number")
num2 = input("pick another number: ")

add = int(num1) + int(num2)

print("The sum is: ")
print(add)
number1 = int(num1)
number2 = int(num2)
if number1 % number2 == 0:
    print("number is even")
elif number1 < number2 or number1<= 0:
    print("num cannot be divided")
elif not(number1 < number2 or number1 <= 0) :
    print("divisible")
elif number1 % number2 != 0 :
    print("number is odd")


age = input("Enter age:")
if int(age) < 18:
    print("you are not of legal age")
elif int(age) >= 18:
    print("You are of legal age")

for x in range(10):
    print(x)
res = 0
count = 1
while count <= 100:
    res += count
    count+=1
print("The sum of numbers from 1 to 100 is:", res)
res = 0
while True:
    num = int(input("Enter a number: "))
    if num == 0:
        break
    res += num
fruits = ["apple", "pear", 3]
fruits[1] = "banana"
fruits.append('strawberry')
print(fruits)
fruits[0:1] = 's'
print(fruits)
for fruit in fruits:
    if fruit == 3:
        print("seen")
    else:
        print("not seen")
fruits = ("apple", "pear", 3)
position = (0,1)
color = (255,255,255)
print(type(color))
print(fruits)
text = input("Enter something: ")
print(text.strip())
print(len(text))
print(text.lower())
print(text.upper())
print(text.capitalize)
print(text.split())
text = "I am a girl named fiona"
print(text[0::3])
def add(x):
    return (x + 2)**2

def sub(x):
    return (x - 2)**2

def prtstr(str):
    print(str)

def acc(mass, force):
    a = mass * force
    return acc
prtstr("hello")
number = add(7)
num = sub(7)
print(number, num)
nickname = ["RJ", 179, "Shooky", 174, "Mang", 177, "Koya", 181, "Chimmy", 174, "Tata", 179, "Cooky", 174]
# nickname.remove()
nickname[0:2] = ["new_name", 1.75]
del nickname[2]
# Copying Lists: Simply using the equals sign (=) copies the reference to the list, not the actual list. To create an independent copy, use the list() function or slicing:
y = list(nickname)  # or x[:]
print(nickname[8:10])
print(nickname)
animal_emoticon = [["Hamster", 33], ["Cat", 33], ["Squirrel", 32], ["Koala", 31], ["Chick", 30], ["Tiger", 30], ["Rabbit", 28]]
print(animal_emoticon)

areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0, "bedroom", 10.75, "bathroom", 10.50]
# Add poolhouse data to areas, new list is areas_1
areas_1 = areas + ["poolhouse", 24.5]
# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 +["garage", 15.45]

# print(areas_2)
n = round(15.45, 1)
print(pow(3,3))
print(type(n))
print(n)
# help(round)

r = [10, 15, 14.1, 2, 5.7]
sort = sorted(r, reverse=True)
print(sort)

pasta_type = "pasta"

# Update pasta type to be more specific
pasta_type = pasta_type.replace("pasta","fusilli pasta" )

ingredient_one = "BASIL"

# Standardize ingredient_none to lowercase
ingredient = ingredient_one.lower()

print(pasta_type)
print(ingredient)

# dictionaries are unordered

bangtan = {"Rm": 31,
            "Jin": 33,
            "Suga": 33,
            "J-hope": 32,
            "Jimin": 30,
            "V": 30,
            "Jk": 28}
bangtan["Mr Lee"] = 40
# print(bangtan["Suga"])
print(bangtan.keys())
print(bangtan.values())
print(bangtan.items())
for names, val in bangtan.items():
    print(names, ":", val, "old")
if "Jimin" in bangtan.keys():
    print("True")
elif "Jimin" not in bangtan.items():
    print("false")
sets: unordered
bulletproof = ["im", "Kim", "Min", "Jung", "Park", "Kim", "Jeon"]
print(bulletproof.index("Jung"))
for name in bulletproof:
    if "Fiona" not in bulletproof:
        bulletproof.append("Fiona")
print(bulletproof)
if bulletproof[0] != "Kim":
    print("Error")
print(type(bulletproof))
print(bulletproof)
b_boys = set(bulletproof)
print(type(b_boys))
b = tuple(bulletproof)
b_boys.add("Lee")
print(type(b))
print(sorted(b, reverse=True))

#  tuples are ordered but their values are constant, they have inde
bangtan_boys = ("Rj", 179, "Shooky", 174, "Mang", 177, "Koya", 181, "Chimmy", 174, "Tata", 179, "Cooky", 174)
print(bangtan_boys[8])
print(bangtan_boys)

from numpy import array
print(float("1.5"))

from openai import OpenAI
client = OpenAI()
response = client.chat.completions.create(
    model="gpt-4o-mini",
    max_completion_tokens=100,
  
    # Enter your prompt
    messages=[{"role": "user", "content": "Suggest tasks I could automate with the OpenAI API in my job."}]
)

print(response.choices[0].message.content)

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

response = client.chat.completions.create(
   model="gpt-4o-mini",
   # Add in the extra examples and responses
   messages=[
       {"role": "system", "content": "You are a helpful Geography tutor that generates concise summaries for different countries."},
       {"role": "user", "content": "Give me a quick summary of Portugal."},
       {"role": "assistant", "content": "Portugal is a country in Europe that borders Spain. The capital city is Lisboa."},
       {"role": "user", "content": "Talk about Chinese cuisine"},
       {"role": "assistant", "content": "Focus on food that with ingredient available in most part of the world"},
       {"role": "user", "content": "Where are the must visit places when touring Nigeria"},
       {"role": "assistant", "content": "include the safely level of each place from bad to good (1-5)"},
       {"role": "user", "content": "How many hours flight from Nigeria to China"},
       {"role": "assistant", "content": "include all stops and which airline, flght time is the best"},
       {"role": "user", "content": "Give me a quick summary of Greece."}
   ]
)
car_count = 20
car_count = "fish"
print("There are {} cars on the road.".format(car_count))
# print(response.choices[0].message.content)
import string
print(string.ascii_lowercase)
print(string.digits)
print(string.punctuation)

area = 3
print(f"The area of the square is: {area / 10000} m^2")
print(f"The area of the square is: {area} / 10000 m^2")
length = int(input("What is the length of rectangle? "))


"""
Author: Brother Burton

Purpose: Determine and display letter grades, including +/-.
"""

grade = int(input("What is your grade percent? "))

if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F"

# Adding + or -
sign = ""

last_digit = grade % 10

if last_digit >= 7:
    sign = "+"
elif last_digit < 3:
    sign = "-"
else:
    sign = ""

# Handle the A+ grades
if grade >= 93:
    sign = ""

# Handle the F+ and F- grades
if letter == "F":
    sign = ""

print(f"Your letter grade is: {letter}{sign}")
if grade >= 80:
    letter = "B"
elif grade >= 90:
    letter = "A"
if grade >= 70:
    print("Congratulations! You passed the class!")
else:
    print("Stay focused and you'll get it next time!")
#Welcome to my fun and silly clever stories adventure!
#Enter the words below, and watch them come together to create a funny story.
def mad_libs():
    print("Welcome to the Mad Libs Game! 🎉")
    print("Please enter the following:\n")

    adjective = input("Enter an adjective: ")
    animal = input("Enter an animal: ")
    verb1 = input("Enter a verb ending ing: ")
    exclamation = input("Enter an exclamation: ").capitalize()
    verb2 = input("Enter another verb: ")
    verb3 = input("Enter one more verb: ")

    story = f"""
    YOUR MAD LIBS STORY 📖

The other day, I was really in trouble. It all started when I saw a very
{adjective} {animal} {verb1} down the hallway.

"{exclamation}!" I yelled.

But all I could think to do was {verb2} over and over again.

Miraculously, that caused it to stop, but not before it tried to
{verb3} right in front of my family!
The End. 
"""

    print(story)


mad_libs()
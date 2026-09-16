# def solution(name):
#     input(name)
#     return "Hello" + name + "welcome"
# solution()

def calculate_inventory():
    customers = 3
    cereal_per_customer = 2.5
    milk_per_customer = 1.25
        
    starting_cereal = 10.0
    starting_milk = 15.0
        
        # 1. Use multiplication to calculate the totals needed
    total_cereal = cereal_per_customer * customers
    total_milk = milk_per_customer * customers
        
        # 2. Use subtraction to calculate the remaining inventory
    remaining_cereal = starting_cereal - total_cereal
    remaining_milk = starting_milk  - total_milk
        
    return remaining_cereal, remaining_milk

print(calculate_inventory())


client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a request to complete the story
story = "Leo the little bear loved looking at the shiny stars every single night.He always wished he could touch one because they " \
"looked so soft and bright.One evening, he saw a beautiful shooting star fall quickly into the deep forest.He ran through the tall trees and happily found a glowing, magical star flower on the ground.Leo hugged the warm flower tightly and knew his special dream had finally come true."
prompt = f"Complete the story(in triple backticks delimeters) with two paragraph in the style of shakespeare: ```{story}```"

# Get the generated response
response = get_response(prompt)

print("\n Original story: \n", story)
print("\n Generated story: \n", response)

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create the instructions
instructions = "Infer the language and the number of sentences of the given delimited 'text';if the text contains more than one sentence, generate a suitable title for it, otherwise, write 'N/A' for the title. ```{text}```"

# Create the output format
output_format = "Include the text, language, number of sentences, and title, each on a separate line,and ensure to use 'Text:', 'Language:', and 'Title:' as prefixes for each line."
text = "Text:', 'Language:', and 'Title:' as prefixes for each line"
prompt = instructions + output_format + f"```{text}```"
response = get_response(prompt)
print(response) 
#                           ------------ EX 1 --------------
#
# def say_hi(name, age):
#     result = f"Hi. My name is {name} and I'm {age} years old"
#     return result
#
#
# assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
# assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
# print('ОК')


#                           ------------ EX 2 --------------

# # option 1
# def correct_sentence(text):
#     if text[0].islower():
#         new_text = text[0].upper() + text[1:]
#     else:
#         new_text = text

#     if text[-1] != ".":
#         new_text += "."
#
#     return new_text

#  option 2
def correct_sentence(text):
    new_text = text[0].capitalize() + text[1:]

    if not text.endswith("."):
        new_text += "."

    return new_text


assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')

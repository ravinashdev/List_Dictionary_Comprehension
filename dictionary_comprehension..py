# Dictionary Comprehension
# From a list
# new_dictionary = { new_key:new_value for item in iterable}
from operator import indexOf

nato_alphabet = ["Alfa", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel", "India", "Juliett", "Kilo", "Lima", "Mike", "November", "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango", "Uniform", "Victor", "Whiskey", "Xray", "Yankee", "Zulu"]
nato_alphabet_dictionary = {item[0]:item for item in nato_alphabet}
print("nato_alphabet_dictionary:",nato_alphabet_dictionary)

# From another Dictionary
# new_dictionary = { new_key:(new_value/expression) for (key,value) in dict.items() if test/condition}
nato_alphabet_dictionary_index = { nato_alphabet.index(value):value for (key,value) in nato_alphabet_dictionary.items() if len(value) < 10 }
nato_alphabet_dictionary_index_reversed = {value:key for (key,value) in nato_alphabet_dictionary_index.items()}
print("nato_alphabet_dictionary_index:",nato_alphabet_dictionary_index)
print("nato_alphabet_dictionary_index_reversed:",nato_alphabet_dictionary_index_reversed)

# NATO Name convert name to NATO alphabet
name = "Ryan"
nato_name = [nato_alphabet_dictionary[item.upper()] for item in name]
nato_name_index = [nato_alphabet_dictionary_index_reversed[item] for item in nato_name]
print("nato_name:",nato_name)
print("nato_name_index:",nato_name_index)

# Word length dictionary
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
sentence_words = sentence.split()
# print(sentence_words)
word_dictionary = {sentence_words.index(item):item for item in sentence_words}
# print(word_dictionary)
word_length_dictionary = { value:len(value) for (key,value) in word_dictionary.items()}
# print(word_length_dictionary)
result = word_length_dictionary
print("word_length_dictionary:",word_length_dictionary)

# Temperature Conversion
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
def c_to_f(c):
    fahrenheit = (c * 1.8) + 32
    return round(fahrenheit,1)
weather_f = {key:c_to_f(value) for (key, value) in weather_c.items()}
print("weather_f:",weather_f)
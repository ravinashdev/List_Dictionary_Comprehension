# Dictionary Comprehension
# From a list
# new_dictionary = { new_key:new_value for item in iterable}
from operator import indexOf

nato_alphabet = ["Alfa", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel", "India", "Juliett", "Kilo", "Lima", "Mike", "November", "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango", "Uniform", "Victor", "Whiskey", "Xray", "Yankee", "Zulu"]
nato_alphabet_dictionary = {item[0]:item for item in nato_alphabet}
print(nato_alphabet_dictionary)

# From another Dictionary
# new_dictionary = { new_key:(new_value/expression) for (key,value) in dict.items() if test/condition}
nato_alphabet_dictionary_index = { nato_alphabet.index(value):value for (key,value) in nato_alphabet_dictionary.items() if len(value) < 10 }
nato_alphabet_dictionary_index_reversed = {value:key for (key,value) in nato_alphabet_dictionary_index.items()}
print(nato_alphabet_dictionary_index)
print(nato_alphabet_dictionary_index_reversed)

# NATO Name convert name to NATO alphabet
name = "Ryan"
nato_name = [nato_alphabet_dictionary[item.upper()] for item in name]
nato_name_index = [nato_alphabet_dictionary_index_reversed[item] for item in nato_name]
print(nato_name)
print(nato_name_index)


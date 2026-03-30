# Imports pandas
import pandas as pd
# Convert CSV file to a dataframe
nato_alphabet_dataframe = pd.read_csv("nato_phonetic_alphabet.csv")
print("nato_alphabet_dataframe:",nato_alphabet_dataframe)
# Request user to type name
user_name = input("Enter your name: ").upper()
# Convert user input name into an iterable list
user_name_list = list(user_name)
# Create a new dictionary from the dataframe using dictionary comprehension
phonetic_dictionary = { row["letter"]:row["code"] for (index,row) in nato_alphabet_dataframe.iterrows()}
# Create a new list that contains the NATO version of your name using list comprehension
nato_name = [phonetic_dictionary[item] for item in user_name_list]
print("nato_name:",nato_name)
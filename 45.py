'''Experiment No:-12
   Title:-  Extracting Words from Text File *
   Aim:-    Develop a Python program that reads a text file and prints words of specified
            lengths (e.g., three, four, five, etc.) found within the file.
   Name:-   Shaikh Alkaish Husain Ahmad Husain
   UIN:-    241P088
   Roll No:-19
   Div:-    D
   Class:-  F.E.(Computer Enigneering)
   Date:-                           '''
import re
def get_words_by_length(filename, lengths):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
        words = re.findall(r"\b[a-zA-Z']+\b", text)  # Improved regex
        # Initialize dictionary properly
        length_dict = {length: [] for length in lengths}
        for word in words:
            if len(word) in length_dict:
                length_dict[len(word)].append(word)
        for length, words in length_dict.items():
            print(f"Words of length {length}: {set(words)}")
    except FileNotFoundError:
        print("Error: File Not Found")
    except ValueError:
        print("Error: Please enter valid integers for lengths.")
    except Exception as e:
        print(f"Error: An error occurred - {e}")
        
# User Input Handling
filename = input("Enter a filename: ").strip()
lengths_input = input("Enter lengths (comma-separated): ").strip()
lengths = [int(x) for x in lengths_input.split(',')] if lengths_input else []
get_words_by_length(filename, lengths)

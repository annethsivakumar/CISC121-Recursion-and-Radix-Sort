"""
CISC-121 2023W
Name: <Anneth Sivakumar>
Student Number: <20320973>
Email:  <21as221@queensu.ca>
Date: 2023-03-16
I confirm that this assignment solution is my own work and conforms to Queen’s standards of Academic Integrity.
"""
from functions import is_anagram

def main():
  """
  This function implements the interface for the program.
  Parameters: None.
  Return: None.
  """
  # Ask user to enter two words.
  word1 = input("Please enter the first word: ").upper().replace(" ", "")
  word2 = input("Please enter the second word: ").upper().replace(" ", "")
  # Check if the strings contain only letters from a-z.
  if word1.isalpha() and word2.isalpha():
      # Determine if both words are anagrams, and print true or not.
      if is_anagram(word1, word2):
          print(f"{word1} and {word2} are anagrams.")
      else:
          print(f"{word1} and {word2} are not anagrams.")
  # If the user enters a symbol or number, print error.
  else:
      print("Invalid input! Please enter words containing only the alphabets.")

  
main()
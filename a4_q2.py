"""
CISC-121 2023W
Name: <Anneth Sivakumar>
Student Number: <20320973>
Email:  <21as221@queensu.ca>
Date: 2023-03-16
I confirm that this assignment solution is my own work and conforms to Queen’s standards of Academic Integrity.
"""
from functions import *

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
    # Create a list of unique prime numbers for each letter in word1.
    lst_word1 = []
    for n in word1:
      prime_num = primeify(n)
      lst_word1.append(prime_num)
    # Create a list of unique prime numbers for each letter in word2.
    lst_word2 = []
    for n in word2:
      prime_num = primeify(n)
      lst_word2.append(prime_num)
    # Make output cleaner, if there is anagram - print only one list.
    if is_anagram(word1, word2):
      print(f"{word1} and {word2} are anagrams." + "\n")
      # Print sorted and unsorted list.
      print(f"Unsorted List of Unique Prime Numbers for Anagram: {lst_word1}")
      print(f"Sorted List of Unique Prime Numbers for Anagram: {radix_sort(lst_word1)}")
    # Otherwise print word1 and word2 list.
    else:
      print(f"{word1} and {word2} are not anagrams.")
      # Print sorted and unsorted list for word1 and word2.
      print("\n" + f"Unsorted List of Unique Prime Numbers for {word1}: {lst_word1}")
      print(f"Sorted List of Unique Prime Numbers for {word1}: {radix_sort(lst_word1)}")
      print("\n" + f"Unsorted List of Unique Prime Numbers for {word2}: {lst_word2}")
      print(f"Sorted List of Unique Prime Numbers for {word2}: {radix_sort(lst_word2)}")
  # If the user enters a symbol or number, print error.
  else:
      print("Invalid input! Please enter words containing only the alphabets.")


main()
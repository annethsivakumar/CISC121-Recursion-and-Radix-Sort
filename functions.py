def char_prime(my_char):
  """ 
  ------------------------------------------------------- 
  Converts an uppercase letter to a unique prime number
  Based on the conversion given in the footnote
  ------------------------------------------------------- 
  Parameters: 
    my_char - a char in ABCDEFGHIJKLMNOPQRSTUVWXYZ (char)
  Returns:
    prime_int = a prime number unique to the letter
  -------------------------------------------------------
  """
  # Hard code of the mapping between letters and unique primes.
  primes = {'A': 2, 'B': 3, 'C': 5, 'D': 7, 
            'E': 11, 'F': 13, 'G': 17, 'H': 19, 
            'I': 23, 'J': 29, 'K': 31, 'L': 37, 
            'M': 41, 'N': 43, 'O': 47, 'P': 53, 
            'Q': 59, 'R': 61, 'S': 67, 'T': 71, 
            'U': 73, 'V': 79, 'W': 83, 'X': 89, 
            'Y': 97, 'Z': 101}
  # Create a variable prime_int to return value of given letter.
  prime_int = primes[my_char]
  return prime_int


def primeify(my_string):
  """
  ------------------------------------------------------- 
  RECURSIVELY gives the product of primes corresponding to the letters 
  in the string
  ------------------------------------------------------- 
  Parameters:
    my_string - any string (str)
  Returns: 
    prime_product = the product of all primes for each letter 
  -------------------------------------------------------
  """
  # Base case - if the word is empty (0), return 1.
  if len(my_string) == 0:
    return 1
  # Recursive case - multiply the prime of the first letter, to the primes of the rest of the word.
  else:
    prime_product = char_prime(my_string[0]) * primeify(my_string[1:])
    return prime_product
    

def is_anagram(string1, string2):
  """
  -------------------------------------------------------
  Determines if two strings are anagrams of each other
  -------------------------------------------------------
  Parameters:
    string1, string2 - any two strings (str)
  Returns:
    is_anagram = whether or not they are anagrams (Boolean)
  -------------------------------------------------------
  """
  # Return True if both strings product of prime's are equal.
  # Otherwise return false.
  return primeify(string1) == primeify(string2)


def radix_sort(list_of_primes):
  """
  -------------------------------------------------------
  Recursively sorts a list of integers from least to greatest
  -------------------------------------------------------
  Parameters:
    list_of_primes - a list of prime numbers associated with a word
  Returns:
    list_of_primes = the list of prime numbers sorted by ascending order
  -------------------------------------------------------
  """
  # Get the maximum value in the list.
  max_value = max(list_of_primes)
  # Call recursive radix sort with base 1 and max value.
  return recursive_radix_sort(list_of_primes, 1, max_value)


def recursive_radix_sort(list_of_primes, significant_digit, max_value):
  """
  -------------------------------------------------------
  Sorts a list of integers using radix sort algorithm with recursion.
  -------------------------------------------------------
  Parameters:
    list_of_primes - a list of prime numbers associated with a word
    significant_digit - The base of the current digit being sorted
    max_value - The maximum value in the input list
  Returns:
    list_of_primes = the list of prime numbers sorted by ascending order
  -------------------------------------------------------
  """
  # Base case - if the list is empty or has only one digit, return same list. Already sorted.
  if max_value <= 1:
    return list_of_primes
  # Create buckets for each digit (0-9).
  buckets = []
  for i in range(10):
    buckets.append([])
  # Divide each number into buckets based on the significant digit at given significant_digit.
  for num in list_of_primes:
    digit = (num // significant_digit) % 10
    buckets[digit].append(num)
  # Append the sorted values back into a single list.
  list_of_primes = []
  for bucket in buckets:
    for num in bucket:
        list_of_primes.append(num)
  # Recursively call radix sort on the next significant digit.
  return recursive_radix_sort(list_of_primes, significant_digit * 10, max_value // 10)

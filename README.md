Question 1: 
------------
In your functions.py file, write the following functions:
- char_prime will map each letter to a unique prime number by writing a function that takes
a single character and outputs the unique prime that you assign to that character. [HINT:
you should hard code the mapping between letters and primes in this function so that
your map is consistent].
- Primeify. A recursive function that computes the product of the character primes for a
given string. This must be a recursive function! You can use the previous function
(char_prime). Consider how to build the prime value for BANANA if you already know the
prime function for NANA
- is _anagram. This function takes in two strings, and computes their product of primes by
‘primeify’ing each string. If the values are equal, then they must be anagrams.

In your main function, called a4_q1.py Ask the user for two strings that contain only upper-case
letters. You should confirm that these are in fact strings, and should check this input. However,
you may choose to give an error, or clean the code however you wish. There are no
requirements here other than that you make certain the user input is a valid string of only upper
case letters with no spaces. Then, call the function is_anagram, and give the user a message
based on this output.


Question 2:
------------
Using the strings we entered from Question 1 (ie. string1 and string2 that may or may not be
anagrams), we notice that we have both a string or a list of primes. We will now sort this string, 
by applying a new sort to the list of primes. (Be sure you create this list of primes if it does not
already exist).

Radix sort is a recursive sorting algorithm that segments the lists into “buckets.” This can be
done in a variety of capacities, but the most common is through position within an integer.

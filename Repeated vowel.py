
from collections import Counter
text="atdyiiiigyt"
vowels='aeiou'
repeated_vowel=[char for char,count in Counter(text).items() if char in vowels and count > 1]
print("Repeated Vowels: ",repeated_vowel)
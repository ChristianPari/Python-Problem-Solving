# Translated the provided string into Pig Latin, begins with a consonant or cluster move to end of string and add "ay" to th end, ends in vowel add "way" to the end

def pig(word):
  # vowel check
  vowels = ["a", "e", "i", "o", "u"]
  for vowel in vowels:
    if (word[0] == vowel):
      return word + "way"

  first_vowel = None

  # consonat converting
  for vowel in vowels:
    first_vowel = word.find(vowel)
    if first_vowel > -1:
      break

  cons = word[0:first_vowel]
  new_word = word[first_vowel:] + cons + "ay"

  return new_word

print(pig("california"))
print(pig("eight"))
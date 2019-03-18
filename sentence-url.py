from random import choice, sample

vowels = {'a', 'e', 'i', 'o', 'u'}

with open("adjectives.txt") as adjs_file:
  adjectives = adjs_file.read().split()
with open("words.txt") as words_file:
  nouns = words_file.read().split()

class SentenceURL:

    def __init__(self, *args, **kwargs):
        pass

    def generate(word_count = 3, capitalize = True, seperator = ''):
      """Generates readable URLs like Twitch's clips"""

      if word_count < 2:
        raise ValueError('Minimum value expected: 2')
      elif word_count > 10:
        raise ValueError('Maximum value expected: 10')

      noun = choice(nouns)
      word_list = []

      if word_count > 3:
        if noun in vowels:
          word_list = ['an']
        else:
          word_list = [choice(('a', 'the'))]

      word_list.extend(sample(adjectives, k = word_count-1))

      if word_count > 4:
        word_list.insert(2, 'and')

      word_list.append(noun)

      if capitalize:
        word_list = map(str.title, word_list)

      return seperator.join(word_list)

def is_anagram(word_one,word_two):
    return (sorted(word_one)==sorted(word_two))
print(is_anagram('anagram','nagaran'))

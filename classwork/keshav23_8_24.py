# Path to the text file
path = r"C:\Python\classwork\file.txt"

# Reading the text file
with open(path, 'r') as f:
    text = f.read()

# Function to count words
def count_words(text):
    words = text.split()
    return len(words)

# Function to count sentences
def count_sentences(text):
    sentence_endings = '.!?'
    sentence_count = 0
    for char in text:
        if char in sentence_endings:
            sentence_count += 1
    return sentence_count

# Function to count syllables in a word
def count_syllables(word):
    word = word.lower()
    syllable_count = 0
    vowels = "aeiou"
    silent_vowel_endings = ['es', 'ed', 'e']
    
    # First count vowels
    for i in range(len(word)):
        if word[i] in vowels:
            # Avoid counting diphthongs (like 'oo', 'ie', etc.)
            if i == 0 or word[i - 1] not in vowels:
                syllable_count += 1

    # Subtract 1 for silent vowels (like a silent 'e' at the end of the word)
    if len(word) > 2 and word.endswith('e'):
        syllable_count -= 1

    return max(syllable_count, 1)  # Ensure at least 1 syllable

# Function to count all syllables in the text
def total_syllables(text):
    words = text.split()
    syllables = 0
    for word in words:
        syllables += count_syllables(word)
    return syllables

# Function to calculate Flesch Reading Ease Index
def flesch_index(words, sentences, syllables):
    return 206.835 - 1.015 * (words / sentences) - 84.6 * (syllables / words)

# Function to calculate Flesch-Kincaid Grade Level
def grade_level(words, sentences, syllables):
    return 0.39 * (words / sentences) + 11.8 * (syllables / words) - 15.59

# Counting words, sentences, and syllables
word_count = count_words(text)
sentence_count = count_sentences(text)
syllable_count_total = total_syllables(text)

# Calculating Flesch Index and Grade Level
flesch_score = flesch_index(word_count, sentence_count, syllable_count_total)
grade_level_score = grade_level(word_count, sentence_count, syllable_count_total)

# Output the results
print(f"Words: {word_count}")
print(f"Sentences: {sentence_count}")
print(f"Syllables: {syllable_count_total}")
print(f"Flesch Reading Ease Index: {flesch_score:.2f}")
print(f"Grade Level: {grade_level_score:.2f}")

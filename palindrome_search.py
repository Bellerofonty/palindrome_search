"""
Checks text from text.txt (utf-8) for palindrome sentences
(containing more than one word)
"""
import re


palindromes = []
punctuation_marks = ['?', '.', '!', '/', ';', ':', ',', '-', '–', '—', '\n', '"', "'", '«', '»', '*', '(', ')']


def line_to_sentences(line):
    """
    Divides a line to sentences by punctuation marks
    ... ? ! . …

    Clears each sentence of other punctuation marks,
    saves it together with the original to a list
    sentences_cleared = [{'orig': orig, 'cleared': cleared}, ]
    Returns the list sentences_cleared
    """
    line = line.strip()
    sentences = re.split('\.\.\.|\?|!|\. |…', line)
    sentences_cleared = []
    for sent in sentences:
        # Delete punctuation marks
        cleared = ''.join(list(filter(lambda ch: ch not in punctuation_marks, sent)))
        cleared = cleared.strip()
        if cleared:
            sentences_cleared.append({'orig': sent, 'cleared': cleared})
    return sentences_cleared


def reverse_str(s):
    """
    Returns the reversed string
    """
    rev_word = ''
    for letter in reversed(s):
        rev_word += letter
    return rev_word


def check_palindrome(sentence):
    """
    Checks if a sentence is a palindrome and is longer than one word
    If both true, returns 1
    """
    words = sentence['cleared'].split()
    if len(words) > 1:
        words_joined = ''.join(words).lower()
        words_rev = reverse_str(words_joined)
        if words_joined == words_rev:
            return 1


def main():
    with open('text.txt', 'r', encoding='utf-8') as file:
        for line in file:
            sentences = line_to_sentences(line)
            for sentence in sentences:
                result = check_palindrome(sentence)
                if result:
                    palindromes.append(sentence['orig'])

    if palindromes:
        with open('palindromes_found.txt', 'w', encoding='utf-8') as file:
            print('Palindromes:')
            for pal in palindromes:
                print(pal)
                file.write(pal + '\n')
            print('Result saved to palindromes_found.txt')
    else:
        print('Palindromes not found')


if __name__ == '__main__':
    main()

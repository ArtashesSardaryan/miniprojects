'''
About Programm : Word Frequency Counter: Write a program that analyzes a text file and counts the
frequency of each word. Remove common stop words and punctuation marks to
get more accurate results. Display the top N most frequent words and their
frequencies.
Version : 1.0
Author : Artash
'''
import string
from collections import Counter

def remove_punctuation(text):
    '''Function To remove punctuation'''
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)

def word_frequency(text, stop_words, top_n):
    '''Function word frequency take 3 arguments'''
    words = text.lower().split()
    words = [remove_punctuation(word) for word in words if word not in stop_words]
    word_count = Counter(words)
    return word_count.most_common(top_n)

def main():
    '''Function main'''
    with open('input.txt', 'r' ) as file:
        text = file.read()

    # Common stop words or ussingg module to find stop words in english
    stop_words = set([
        'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours',
        'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers',
        'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves',
        'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are',
        'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does',
        'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until',
        'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into',
        'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down',
        'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here',
        'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more',
        'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so',
        'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now'
    ])

    top_n = 10
    top_words = word_frequency(text, stop_words, top_n)

    print("Top", top_n, "most frequent words:")
    for word, freq in top_words:
        print(word, "-", freq)

if __name__ == "__main__":
    main()

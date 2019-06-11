'''You have a new professor of graph theory and he speaks very quickly. You come up with the following plan to keep up with his lecture and make notes.

You know two languages, and the professor is giving the lecture in the first one. The words in both languages consist of lowercase English characters, each language consists of several words. For each language, all words are distinct, i.e. they are spelled differently. Moreover, the words of these languages have a one-to-one correspondence, that is, for each word in each language, there exists exactly one word in the other language having has the same meaning.

You can write down every word the professor says in either the first language or the second language. Of course, during the lecture you write down each word in the language in which the word is shorter. In case of equal lengths of the corresponding words you prefer the word of the first language.

You are given the text of the lecture the professor is going to read. Find out how the lecture will be recorded in your notes.
Input

The first line contains two integers, n and m (1 ≤ n ≤ 3000, 1 ≤ m ≤ 3000) — the number of words in the professor's lecture and the number of words in each of these languages.

The following m lines contain the words. The i-th line contains two strings ai, bi meaning that the word ai belongs to the first language, the word bi belongs to the second language, and these two words have the same meaning. It is guaranteed that no word occurs in both languages, and each word occurs in its language exactly once.

The next line contains n space-separated strings c1, c2, ..., cn — the text of the lecture. It is guaranteed that each of the strings ci belongs to the set of strings {a1, a2, ... am}.

All the strings in the input are non-empty, each consisting of no more than 10 lowercase English letters.
Output

Output exactly n words: how you will record the lecture in your notebook. Output the words of the lecture in the same order as in the input.
'''

def lecture(language_mapper, lecture_list):
    final_languages = []
    for language in lecture_list:
        if language in language_mapper:
            if len(language) <= len(language_mapper[language]):
                final_languages.append(language)
            elif len(language) > len(language_mapper[language]):
                final_languages.append(language_mapper[language])
    
            else:
                pass
    return final_languages
    
if __name__ == '__main__':
    X = str(input()) 
    n, m = X.split(' ') #number of words in lecture || #count of map of words from one lang to another
    language_mapper = {}
    for i in range(int(m)):
        L = str(input())
        lang1, lang2 = L.split(' ')
        lang1, lang2 = lang1.lower(), lang2.lower()
        language_mapper[str(lang1)] = str(lang2)
    
    lecture_list = []
    LL = str(input())
    lecture_list = LL.split(' ')
    '''
    for k,v in language_mapper.items():
        print(k, v)
    
    for word in lecture_list:
        print(word, end = ' ')
    '''
    
    lecture_list = [lang.lower() for lang in lecture_list]
    final = lecture(language_mapper, lecture_list)
    for lang in final:
        print(lang, end = ' ')
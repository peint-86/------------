import numpy as np
def lec_word_matrix(courses, vocab):
    lec_word=np.zeros((len(courses),len(vocab)),dtype=int)
    for i in range(len(courses)):
        for j in range(len(vocab)):
            if vocab[j] in courses:
                lec_word[i][j]=1
    print(lec_word)
courses = list(open("course_list.csv"))
vocab = list(open("keyword_list.csv"))
lec_word_matrix(courses, vocab)
    
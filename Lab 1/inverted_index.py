# Inverted Index program using 4 documents for text 

import pandas as pd
import numpy as np

# file = open('file_name','mode') opens the file in read, append or write mode
# file.read()

file = open('doc1.txt','r')
doc1 = file.read()
# print(doc1)     #checking if the reading is going ok
file.close()

file = open('doc2.txt','r')
doc2 = file.read()
# print(doc2)     
file.close()

file = open('doc3.txt','r')
doc3 = file.read()
# print(doc3)     
file.close()

file = open('doc4.txt','r')
doc4 = file.read()
# print(doc4)     
file.close()

#making a list from the files :
docs = [doc1,doc2,doc3,doc4]
print(docs,"\n")

#making set of all individual words :
words =     { term for doc in docs for term in doc.split() }
print("All words used in the docs (unique) : ")
for word in words :
    print(word)

# Incerted Index (in form of  dictionary ):
inverted_index = {}

for i,doc in enumerate(docs):
    for term in doc.split():
        if term in inverted_index:
            inverted_index[term].add(i)
        else:
            inverted_index[term] = {i}

print("\nInverted_index : ")
for key in inverted_index:
    values = inverted_index[key]
    print(key," : ",values)

# Term document Matrix (in form of dictionary) :
term_document_matrix = {}

for term in words :
    #setting the unique words as the keys and empty list as the value
    term_document_matrix[term] = []
    
    for doc in docs:
        #if the term is in the doc then 1 else 0 
        if term in doc:
            term_document_matrix[term].append(1)
        else:
            term_document_matrix[term].append(0)

print("\nTerm Document Matrix : ")
for word in term_document_matrix:
    valueslist = term_document_matrix[word]
    print(word," : ",valueslist)



# Boolean Retrival Model for solving Boolean queries 
# making a numpy array from the docs list
docs_array = np.array(docs, dtype="object")

# 1. schizophrenia AND drug
# getting the 0,1 list of values from the Term Document Matrix and making it into a numpy array
# for the words schizonphrenia and drug
statement1 = np.array(term_document_matrix['schizophrenia'])
statement2 = np.array(term_document_matrix['drug'])

print("\nBoolean of 'schizophrenia' AND 'drug' : ")
print(statement1," ---> 'schizophrenia'")
print(statement2, " ---> 'drug'")
print('-----------')
result_statement = statement1 & statement2
print(result_statement, " ---> Result")

# 2. for AND NOT (drug OR approach)
print("\nBoolean - for AND NOT (drug OR approach) : ")
s1 =np.array(term_document_matrix['for'])
s2 =np.array(term_document_matrix['drug'])
s3 =np.array(term_document_matrix['approach'])

print(s1, " ---> 'for'")
print(s2, " ---> 'drug'")
print(s3, " ---> 'approach'")

result = s1 & ~(s2 | s3)
print(result," ---> Result")
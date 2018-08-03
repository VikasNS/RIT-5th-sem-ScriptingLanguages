import nltk
from nltk import NaiveBayesClassifier
data=[({'lastchar':word[-1]},'male') for word in nltk.corpus.names.words('male.txt')]
data+=[({'lastchar':word[-1]},'female')for word in nltk.corpus.names.words('female.txt')]
import random
random.shuffle(data)

count=len(data)

train_count=int(0.8*count)

train_data=data[:train_count]
test_data=data[train_count:]

classifier=NaiveBayesClassifier.train(train_data)
print(nltk.classify.accuracy(classifier,test_data))

#raju
print(classifier.classify({'lastchar':'u'}))

#watson
print(classifier.classify({'lastchar':'n'}))

#Ramya
print(classifier.classify({'lastchar':'a'}))



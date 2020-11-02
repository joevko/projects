# encoding: utf-8
import nltk
from nltk.probability import ConditionalFreqDist, ConditionalProbDist, MLEProbDist

with open("norne.txt", encoding="utf8") as f:
    mylist = [nltk.tag.str2tuple(t, sep='_') for t in f.read().split()]

# string = " ".join(["_".join(t) for t in mylist])
# with open('sushi-txt', 'x') as f:
#     f.write(string)

print(mylist)
#
# word = []
# tag = []

# print("-----LENGHT-----", len(mylist))
#
# cfd = ConditionalFreqDist()
#
# w = []
# t = []
# for token,tag in mylist:
#     cfd[tag][token] += 1
#
# cpd = ConditionalProbDist(cfd, MLEProbDist)
# print(cpd['AT'].prob('the'))

#self.transition = ConditionalProbDist(cfd_t, MLEProbDist)
# filen = open("norne.txt", encoding="utf8")
# setningene = filen.read().split("\n")

# filen = open("norne.txt", encoding="utf8")
# for line in filen:
#     print(line)
#setningene = filen.read().split("\n")

# abc = []
# for t in filen.split():
#     abc.append(nltk.tag.str2tuple(t))
#     print(t)

# sushi = [nltk.tag.str2tuple(t) for t in filen.split()]
# print(sushi)

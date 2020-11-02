# -*- coding: utf-8 -*-

import nltk
import sys
from nltk.corpus import brown
from nltk.probability import ConditionalFreqDist, ConditionalProbDist, MLEProbDist

#########
# Oppgave 1:

#conditional frequency distribution
#tar inn en liste av par, der første elementet blir betingelsen.

#en dictionary der hver tagg er en nøkkel og hver verdi er en dictionary på formen {ord:frekvens}. Feks {NN:{bil:2,tre:3,gutt:4,..}, VB:{skyte:1,løpe:3,..}}


# # #######
# # # emission probabilities:
# # # P(w_i | t_i)

with open("norne.txt", encoding="utf8") as f:
    mylist = [nltk.tag.str2tuple(t, sep='_') for t in f.read().split()]

#brown_ord_tagger = brown.tagged_words()
brown_tagger_ord = [ (tag, word) for (word, tag) in mylist ]


# # frekvensdistribusjon
cfd_tagger_ord = nltk.ConditionalFreqDist(brown_tagger_ord)

# max_nn = cfd_tagger_ord['NN'].most_common()[0]
# f_nn = cfd_tagger_ord['NN']['linguist']
# max_jj = cfd_tagger_ord['JJ'].most_common()[0]
#
# print("Oppgave 1:")
# print("1.2 (a) Mest frekvente substantivet:", max_nn)
# print("1.2 (b) Antall forekomster av 'linguist':", f_nn)
# print("1.2 (c) Mest frekvente adjektivet:", max_jj)


# # sannsynlighetsdistribusjon
cpd_tagger_ord = nltk.ConditionalProbDist(cfd_tagger_ord, nltk.MLEProbDist)
#print("Mest sannsynlige adjektivet:", cpd_tagger_ord['JJ'].max())
#print("Sannsynligheten for new gitt JJ:", cpd_tagger_ord['JJ'].prob("new"))


# # ########
# # # transition probabilities:
# # # P(t_i | t_{i-1})

# # bigram over tagger
brown_tagger = [tag for (word, tag) in mylist]
brown_tagg_par = nltk.bigrams(brown_tagger)


# # frekvensdistribusjon over bigrammene
cfd_tagger= nltk.ConditionalFreqDist(brown_tagg_par)
print("BLAAAAAAAA",cfd_tagger['NOUN'])

#print(cfd_tagger.conditions())
max_etter_nn = cfd_tagger['NOUN'].most_common()[0]
f_dtnn = cfd_tagger['ADJ']['NOUN']

print("1.5 (a) Taggen som oftest etterfolger NN er:", max_etter_nn)
print("1.5 (b) Antall forekomster av bigrammet 'DT NN' er:", f_dtnn)

# # sannsynlighetsdistribusjon over taggbigram
cpd_tagger = nltk.ConditionalProbDist(cfd_tagger, nltk.MLEProbDist)

print("1.6 Sannsynligheten for NOUN gitt ADJ er:", cpd_tagger["ADJ"].prob("NOUN"))

# # ############
# # Oppgave 2

# # # #emission probabilities
w1a = cpd_tagger_ord['NOUN'].prob("taler")
w2a = cpd_tagger_ord['VERB'].prob("taler")
w3a = cpd_tagger_ord['ADJ'].prob("flere")

print("Oppgave 4b):")
print("P(taler|NOUN):", w1a)
print("P(taler|VERB):", w2a)
print("P(flere|ADJ):", w3a)

# w1b = cpd_tagger_ord['PPO'].prob("her")
# w2b = cpd_tagger_ord['VB'].prob("duck")
#
# print("P(her|PPO):", w1b)
# print("P(duck|VB):", w2b)


# # # #transition probabilities
t1a = cpd_tagger["ADJ"].prob("NOUN")
t2a = cpd_tagger["ADJ"].prob("VERB")

print("P(NOUN|ADJ):", t1a)
print("P(VERB|ADJ):", t2a)

# t1b = cpd_tagger["VBD"].prob("PPO")
# t2b = cpd_tagger["PPO"].prob("VB")
#
# print("P(PPO|VBD):", t1b)
# print("P(VB|PPO):", t2b)

#Oppgave 4c)
first = w1a * t1a
second = w2a * t2a

print(" SVARET First: ", first)
print("Second: ", second)

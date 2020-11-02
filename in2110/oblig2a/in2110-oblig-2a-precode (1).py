# encoding: utf-8
import nltk
from nltk.probability import ConditionalFreqDist, ConditionalProbDist, MLEProbDist

TRAIN_DATA = "norne.txt"
#DEV_DATA = "no_bokmaal-ud-dev.tt"

def read_dataset(filename):
    """Read dataset from file and return a list of sentences, each
    sentence a list of words, and a list of the corresponding pos
    tags.
    """

    filen = open(filename, encoding="utf8")
    setningene = filen.read().split("\n")
    # i = 0
    # for s in setningene:
    #     print("__________________________")
    #     print(i)
    #     print(s)
    #     print("__________________________")
    #     i = i+1

    sentences = []
    labels = []

    for s in setningene:
        if s != "":
            ordene_tagene = s.split(" ")
            o = []
            t = []
            for o_t in ordene_tagene:
                l = o_t.split("([^_ ]+)")
                o.append(l[0])
                #t.append(l[1])
            sentences.append(o)
            #labels.append(t)


    print(sentences)


#train_sents, train_labels = read_dataset(TRAIN_DATA)
#dev_sents, dev_labels = read_dataset(DEV_DATA)
#test_sent, test_labels = read_dataset("eisner.tt")

# def bigrams(sequence):
#     """Return a sequence of bigrams from input sequence."""
#
#     bgs = []
#
#     s = ["<s>"] + sequence
#
#     i = 0
#     j = 1
#
#     while j != len(s):
#         bgs.append([s[i]] + [s[j]])
#         i += 1
#         j += 1
#
#     return bgs
#
# class SmoothProbDist(MLEProbDist):
#     """Probability distribution with simple smoothing."""
#
#     def prob(self, key):
#         """Return probability for key. Add smoothing to zero values."""
#
#         value = super(SmoothProbDist, self).prob(key)
#
#         if value == 0:
#             return 1e-20
#         else:
#             return value
#
# class PosTagger(object):
#     """Pos tagger."""
#
#     def __init__(self):
#         self.transition = {}
#         self.emission = {}
#         self.tagger = []
#
#     def transform(self, sentences):
#
#         labels = []
#
#         for s in sentences:
#             l = self.viterbi(s)
#             labels.append(l)
#
#         return labels
#
#     def viterbi(self, ordene):
#
#         #initialiserer V
#         viterbi = [{}]
#         for st in self.tagger:
#             viterbi[0][st] = {"prob" : self.transition["<s>"].prob(st) * self.emission[st].prob(ordene[0]), "prev" : None}
#
#         #rekursion steget, finner de hoyeste probabilitene
#         for t in range(1, len(ordene)):
#             viterbi.append({})
#             for st in self.tagger:
#                 max_tr_prob = viterbi[t-1][self.tagger[0]]["prob"]*self.transition[self.tagger[0]].prob(st)
#                 prev_st_selected = self.tagger[0]
#                 for prev_st in self.tagger[1:]:
#                     tr_prob = viterbi[t-1][prev_st]["prob"]*self.transition[prev_st].prob(st)
#                     if tr_prob > max_tr_prob:
#                         max_tr_prob = tr_prob
#                         prev_st_selected = prev_st
#                 max_prob = max_tr_prob * self.emission[st].prob(ordene[t])
#                 viterbi[t][st] = {"prob" : max_prob, "prev": prev_st_selected}
#
#
#         path = []
#         max_prob = max(value["prob"] for value in viterbi[-1].values())
#         previous = None
#
#         #finner det første (siste) tagget
#         for tag, data in viterbi[-1].items():
#             if data["prob"] == max_prob:
#                 path.append(tag)
#                 previous = tag
#
#         #gaar bakover for aa lagre den mest sannsynlig sekvensen
#         for t in range(len(viterbi) - 2, -1, -1):
#             path.insert(0, viterbi[t + 1][previous]["prev"])
#             previous = viterbi[t + 1][previous]["prev"]
#
#         return path
#
#     def fit(self, sentences, labels):
#         """Fit pos tagger to training data."""
#
#         cfd_e = ConditionalFreqDist()
#         i = 0
#         while i < len(sentences):
#             j = 0
#             while j < len(sentences[i]):
#                 cfd_e[labels[i][j]][sentences[i][j]] += 1
#                 if labels[i][j] not in self.tagger:
#                     self.tagger.append(labels[i][j])
#                 j += 1
#             i += 1
#
#         self.emission = ConditionalProbDist(cfd_e, SmoothProbDist)
#
#         cfd_t = ConditionalFreqDist()
#         for s in labels:
#             t_b = bigrams(s)
#             for b in t_b:
#                 cfd_t[b[0]][b[1]] += 1
#
#         self.transition = ConditionalProbDist(cfd_t, MLEProbDist)
#
# pt = PosTagger()
# pt.fit(train_sents, train_labels)
#
# def accuracy(true, pred):
#     """Return accuracy score for predictions."""
#
#     true_positives = 0.0
#     total = 0.0
#
#     for i in range(len(true)):
#         for j in range(len(true[i])):
#             total += 1.0
#             if true[i][j] == pred[i][j]:
#                 true_positives += 1.0
#
#     return true_positives/total
#
# """
# Accuracy with MLEProbDist: 0.545794495312
# Accuracy with SmoothProbDist: 0.911545547032
# """
# print (">>> train_sents[8634]\n", train_sents[8634])
# print (">>> train_labels[8634]\n", train_labels[8634])
# print( ">>> bigrams(['vi','vil','ikke','ha','det','normale','.'])\n", bigrams(['vi','vil','ikke','ha','det','normale','.']))
# print (">>> pt.transition['NOUN'].prob('VERB')\n", pt.transition["NOUN"].prob("VERB"))
# print (">>> pt.emission['NOUN'].prob('hest')\n", pt.emission["NOUN"].prob("hest"))
# print (">>> pt.transform([['vi','vil','ikke','ha','det','normale','.']])\n", pt.transform([['vi','vil','ikke','ha','det','normale','.']]))
# print (">>> accuracy(train_labels, pt.transform(train_sents))\n", accuracy(train_labels, pt.transform(train_sents)))
# print (">>> pt.emission['VERB'].prob('tæsje')\n", pt.emission['VERB'].prob("tæsje"))
# print (">>> accuracy(dev_labels, pt.transform(dev_sents))\n", accuracy(dev_labels, pt.transform(dev_sents)))
read_dataset(TRAIN_DATA)

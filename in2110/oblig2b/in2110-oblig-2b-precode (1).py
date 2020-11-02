import spacy
from spacy import displacy

from in2110.oblig2b import plot_learning_curve
from in2110.conllu import ConlluDoc

def accuracy(true, pred):
    true_positives = 0.0
    total = 0.0

    for i in range(len(true)):
        for j in range(len(true[i])):
            total += 1.0
            if true[i][j] == pred[i][j]:
                true_positives += 1.0

    return true_positives/total

def attachment_score(true, pred):
    words_with_correct_head = 0
    words = 0
    words_w_cor_head_dep = 0

    for i in range(len(true)):
        for j in range(len(true[i])):
            words += 1
            a = true[i][j].head
            b = pred[i][j].head
            if a.text == b.text:
                words_with_correct_head += 1
                if true[i][j].dep_ == pred[i][j].dep_:
                    words_w_cor_head_dep += 1
    las = words_with_correct_head/words
    uas = words_w_cor_head_dep/words

    return uas, las

nb = spacy.load("my-model/model-best")

#POS tagging
conllu_dev = ConlluDoc.from_file("no_bokmaal-ud-dev.conllu")
dev_docs = conllu_dev.to_spacy(nb) #gold standard, doc objects
dev_docs_unlabeled = conllu_dev.to_spacy(nb, keep_labels=False) #train data, spacy objects

true = []
pred = []
for i in range(len(dev_docs)):
    nb.tagger(dev_docs_unlabeled[i])
    t = [token.tag_ for token in dev_docs[i]]
    true.append(t)
    p = [token.tag_ for token in dev_docs_unlabeled[i]]
    pred.append(p)

acc = accuracy(true, pred) #0.9674997937804174

#Parsing
antall_setninger = 0
for i in range(len(dev_docs)):
    antall_setninger += 1
    nb.parser(dev_docs_unlabeled[i])

att = attachment_score(dev_docs, dev_docs_unlabeled) #UAS = 0,7721136132420467 LAS = 0,8679919711842503

doc = nb("Å være i familie involverer ikke nødvendigvis ubetinget kjærlighet.")
displacy.serve(doc, style="dep", options={"fine_grained": True})

"""
a = [0.967, 0.916, 0.892, 0.852, 0.780, 0.692, 0.539]
a.reverse()
b = [0.772, 0.615, 0.537, 0.426, 0.270, 0.148, 0.052]
b.reverse()
c = [0.868, 0.746, 0.686, 0.605, 0.492, 0.398, 0.194]
c.reverse()
plot_learning_curve([0.015625, 0.03125, 0.0625, 0.125, 0.25, 0.5, 1.0], a, "Accuracy")
plot_learning_curve([0.015625, 0.03125, 0.0625, 0.125, 0.25, 0.5, 1.0], b, "UAS")
plot_learning_curve([0.015625, 0.03125, 0.0625, 0.125, 0.25, 0.5, 1.0], c, "LAS")"""

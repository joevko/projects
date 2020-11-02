from collections import Counter

from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

from in2110.corpora import norec
from in2110.oblig1 import scatter_plot
from nltk import word_tokenize

from sklearn.preprocessing import StandardScaler


def prepare_data(documents):
    data = []
    labels = []

    for doc in documents:
        if doc.metadata['category'] in ("restaurants", "games", "literature"):
            data.append(doc.text)
            labels.append(doc.metadata['category'])

    return data, labels


def tokenize(doc):
    return [t.lower() for t in word_tokenize(doc)]


class Vectorizer:
    def __init__(self):
        self.vectorizer = CountVectorizer(tokenizer=tokenize, max_features=5000)
        self.tfidf = TfidfTransformer()

    def vec_train(self, data):
        vec = self.vectorizer.fit_transform(data)
        vec_tfidf = self.tfidf.fit_transform(vec)

        return vec, vec_tfidf

    def vec_test(self, data):
        vec = self.vectorizer.transform(data)

        return vec, self.tfidf.transform(vec)


def create_knn_classifier(vec, labels, k):
    clf = KNeighborsClassifier(k)
    clf.fit(vec, labels)

    return clf


# Innlesing av data
print("Reading data")
train_data, train_labels = prepare_data(norec.train_set())
dev_data, dev_labels = prepare_data(norec.dev_set())
test_data, test_labels = prepare_data(norec.test_set())

# Testing av tokenisering
for label, fn in (("split", str.split),
                  ("tokenize", word_tokenize),
                  ("tokenize+downcase", lambda s: [t.lower()
                                                   for t in word_tokenize(s)])):
    data, _ = prepare_data(norec.train_set())

    tokens = [t for s in data
              for t in fn(s)]
    types = set(tokens)

    print("Tokens and types for {}".format(label))
    print("Tokens: {}".format(len(tokens)))
    print("Types: {}".format(len(types)))

print()

# Statistikk
categories = Counter(train_labels)

print("Category distribution:")
for category, count in categories.items():
    print("{}: {}".format(category, count))

print()

# Vektorisering
vectorizer = Vectorizer()

print("Vectorizing training data")
vec, vec_tfidf = vectorizer.vec_train(train_data)

print("Plotting")
scatter_plot(vec, train_labels)
scatter_plot(vec_tfidf, train_labels)

print("Vecorizing dev data")
dev_vec, dev_vec_tfidf = vectorizer.vec_test(dev_data)

for k in range(1, 16):
    clf = create_knn_classifier(vec, train_labels, k)

    acc = accuracy_score(dev_labels, clf.predict(dev_vec))

    clf = create_knn_classifier(vec_tfidf, train_labels, k)
    acc_tfidf = accuracy_score(dev_labels, clf.predict(dev_vec_tfidf))

    print("k={}, raw: {}, tf-idf: {}".format(k, acc, acc_tfidf))

clf = create_knn_classifier(vec_tfidf, train_labels, 12)

print("Vecorizing test data")
test_vec, test_vec_tfidf = vectorizer.vec_test(test_data)

print("Test accuracy: {}".format(accuracy_score(test_labels,
                                                clf.predict(test_vec_tfidf))))

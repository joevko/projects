# coding=utf-8
# IN2110 Oblig 1 pre-kode
import nltk
from nltk import word_tokenize
# Klasser og funksjoner fra scikit-learn som vi skal bruke i obligen
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

from udtk import Model
# Norec dataset
from in2110.corpora import norec

# Hjelpefunksjoner for visualisering
from in2110.oblig1 import scatter_plot

def categories(labels):
    rest = 0
    games = 0
    lit = 0
    for item in labels:
        if item == "restaurants":
            rest = rest +1
        elif item == "games":
            games = games+1
        else:
            lit = lit+1

    print("Total: ", len(labels))
    print("Restaurants: ", rest, "\nGames: ", games, "\nLiterature: ", lit)

    print("Restaurants: ", rest/len(labels)*100, "%")
    print("Games: ", games/len(labels)*100, "%")
    print("Literature: ", lit/len(labels)*100, "%")

def prepare_data(documents):
    """Tar inn en iterator (kan være en liste) over dokumenter fra norec
    og returnerer to lister:

    - data   : En liste over dokument-tekstene.
    - labels : En liste over hvilken kategori dokumentet tilhører.

    Begge listene skal være like lange og for dokumentet i data[i]
    skal vi kunne finne kategorien i labels[i].
    """

    # Din kode her

    data = []
    labels = []
    for item in documents:
        cat = item.metadata.get("category")
        if cat == "games" or cat == "restaurants" or cat == "literature":
            data.append(item.text)
            labels.append(cat)


    return data, labels

def tokenize(text):
    doc = [item.lower() for item in word_tokenize(text)]
    return doc

def tokenize_pluss_info(text):
    """Tar inn en streng med tekst og returnerer en liste med tokens."""

    # Å splitte på mellomrom er fattigmanns tokenisering. Endre til noe
    # bedre!
    split_funksjon = text.split()
    print(".split()   Tokens: ", len(split_funksjon), " types: ", len(set(split_funksjon)))

    doc2 = word_tokenize(text)
    print("word_tokenize()    Tokens: ", len(doc2), "types: ", len(set(doc2)))

    doc3 = [item.lower() for item in word_tokenize(text)]
    print("lower()    Tokens: ", len(doc3), "types: ", len(set(doc3)))

    m = Model("norwegian-bokmaal")
    doc4 = m.tokenize(text)
    print("m.tokenize()    Tokens: ", len(doc4), "types: ", len(set(doc4)))

class Vectorizer():
    def __init__(self):
        """Konstruktør som tar inn antall klasser som argument."""

        self.count_vectorizer = CountVectorizer(max_features=5000, tokenizer=tokenize, lowercase=False)
        self.tfidf = TfidfTransformer()

    def train(self, data):
        """Tilpass vektorisereren til data. Returner de vektoriserte
        treningsdataene med og uten tfidf-vekting.

        """

        # Din kode her

        # Tips: Bruk fit_transform() for å spare kjøretid.

        vec = self.count_vectorizer.fit_transform(data)
        vec_tfidf = self.tfidf.fit_transform(vec)

        return vec, vec_tfidf

    def vectorize(self, data):
        """Vektoriser dokumentene i data. Returner vektorer med og uten
        tfidf-vekting.

        """
        # Din kode her
        vec = self.count_vectorizer.transform(data)
        vec_tfidf = self.tfidf.transform(vec)

        return vec, vec_tfidf

def create_knn_classifier(vec, labels, k):
    """Lag en k-NN-klassifikator, tren den med vec og labels, og returner
    den.

tokenize_pluss_info(train_data[0])
    """

    clf = KNeighborsClassifier(k)
    clf.fit(vec, labels)

    return clf

# Treningsdata
train_data, train_labels = prepare_data(norec.train_set())

# Valideringsdata
dev_data, dev_labels = prepare_data(norec.dev_set())

# Testdata
test_data, test_labels = prepare_data(norec.test_set())

# Din kode her

vec = Vectorizer()
mat, matTF = vec.train(train_data)

scatter_plot(mat, train_labels)
scatter_plot(matTF, train_labels)

mat2, matTF2 = vec.vectorize(dev_data)

mat3, matTF2 = vec.vectorize(test_data)

classifier = create_knn_classifier(matTF, train_labels, 10)

knn = classifier.predict(mat3)

print(accuracy_score(test_labels, knn))

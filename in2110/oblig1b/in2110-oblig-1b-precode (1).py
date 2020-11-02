from in2110.oblig1b import visualize_word_vectors
from in2110.corpora import aviskorpus_10_nn
import re
import math

def preprocess(sentences):
    """Return list of preprocessed tokens."""

    korpus = []
    for item in sentences:
        sentence = item.split(" ")
        korpus.append(sentence)

    return korpus

def preprocess_downcase(sentences):
    korpus = []
    for item in sentences:
        sentence = [i.lower() for i in item.split(" ")]
        korpus.append(sentence)

    return korpus

def preprocess_special_symbols(sentences):
    korpus = []
    for item in sentences:
        sentence = [i for i in item.split(" ") if re.match(r"[a-zA-Z]+", i)]
        korpus.append(sentence)

    return korpus

def preprocess_all_in(sentences):
    korpus = []
    for item in sentences:
        sentence = [i.lower() for i in item.split(" ") if re.match(r"[a-z]+", i)]
        korpus.append(sentence)

    return korpus

def context_window(sent, pos, size):
    """Return context window for word at pos of given size."""
    start_a = pos+1
    end_a = pos+size+1
    start_b = pos-size

    if start_b < 0:
        cont_window = sent[0:pos] + sent[start_a:end_a]
    else:
        cont_window = sent[start_b:pos] + sent[start_a:end_a]
    return cont_window

class WordVectorizer(object):
    """Word vectorizer with sklearn-compatible interface."""

    def __init__(self, max_features, window_size, normalize=False):
        self.max_features = max_features
        self.window_size = window_size
        self.normalize = normalize
        self.matrix = None
        self.is_normalized = False

    def fit(self, sentences):
        """Fit vectorizer to sentences."""
        #finner de mest frekvente
        dict = {}
        for item in sentences:
            for i in item:
                if i in dict.keys():
                    dict[i] = dict[i] + 1
                else:
                    dict[i] = 1

        sorted_d = sorted((value, key) for (key, value) in dict.items())
        sorted_d.reverse()

        d = sorted_d[0:self.max_features]
        s = set([key for (value, key) in d])
        
        #lager matrisen
        self.matrix = {el:{} for el in s}
        
        #utfyller matrisen
        for senten in sentences:
            i = 0
            for word in senten:
                if word in s:
                    c_w = context_window(senten, i, self.window_size)
                    for w in c_w:
                        if w in s:
                            if w in self.matrix[word].keys():
                                self.matrix[word][w] = self.matrix[word][w] + 1
                            else:
                                self.matrix[word][w] = 1
                i = i + 1

        if self.normalize:
            self.normalize_vectors()
            self.is_normalized = True

    def transform(self, words):
        """Return vectors for each word in words."""

        return [self.matrix[w] for w in words]

    def vector_norm(self, word):
        """Compute vector norm for word."""
        vector = self.matrix[word]
        norm_vector = 0
        for w in vector:
            norm_vector = norm_vector + vector[w]**2
        
        return math.sqrt(norm_vector)

    def normalize_vectors(self):
        """Normalize vectors."""

        for key, value in self.matrix.items():
            a = self.vector_norm(key)
            for k, v in value.items():
                self.matrix[key][k] = v/a

    def euclidean_distance(self, w1, w2):
        """Compute euclidean distance between w1 and w2."""

        p = self.matrix[w1]
        q = self.matrix[w2]
        
        eu_dist = 0

        for key, value in p.items():
            if key in q.keys():
                eu_dist = eu_dist + (value-q[key])**2
            else:
                eu_dist = eu_dist + (value-0)**2

        for key, value in q.items():
            if key not in p.keys():
                eu_dist = eu_dist + (0-value)**2

        return math.sqrt(eu_dist)                
    
    def cosine_similarity(self, w1, w2):
        """Compute cosine similarity between w1 and w2."""

        p = self.matrix[w1]
        q = self.matrix[w2]

        sim = 0
        
        for key, value in p.items():
            if key in q.keys():
                sim = sim + (value*q[key])

        if self.is_normalized:
            return sim
        else:
            return sim/((self.vector_norm(w1))*(self.vector_norm(w2)))

    def nearest_neighbors(self, w, k):
        """Return list of the k nearest neighbors to w."""

        l = sorted([self.cosine_similarity(key, w), key] for key, value in self.matrix[w].items())
        l.reverse()
        return l[0:k]

sentences = list(aviskorpus_10_nn.sentences())
p = preprocess_special_symbols(sentences)
ww = WordVectorizer(5000, 5)
ww.fit(p)



visualize_word_vectors(ww, ["nynorsk", "bokmål", "aktuelt", "akseptert"])

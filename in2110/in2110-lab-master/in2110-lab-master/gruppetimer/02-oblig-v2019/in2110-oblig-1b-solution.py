import math
import heapq

from collections import Counter, defaultdict

from in2110.oblig1b import visualize_word_vectors

from in2110.corpora import aviskorpus_10_nn

def preprocess(sentences):
    return list(([t.lower() for t in sent.split()] for sent in sentences))

def context_window(sent, pos, size):
    return sent[max(pos-size, 0):pos] + sent[pos+1:pos+1+size]

class WordVectorizer(object):
    def __init__(self, max_features, window_size, normalize=False):
        self.max_features = max_features
        self.window_size = window_size
        self.normalize = normalize
        self.matrix = defaultdict(Counter)
        self.is_normalized = False

    def fit(self, sentences):
        # Count word frequencies in order to use only the most
        # frequent words as features.
        freqs = Counter(t for s in sentences for t in s)

        # Create vocabulary form the most frequent words
        self.vocab = set(w for w,c in freqs.most_common(self.max_features))

        # Iterate over sentences to build co-occurence matrix
        for sent in sentences:
            for i in range(len(sent)):
                t = sent[i]
                if t in self.vocab:
                    context = context_window(sent, i, self.window_size)

                    for ct in context:
                        if ct in self.vocab:
                            self.matrix[t][ct] += 1

        if self.normalize:
            self.normalize_vectors()

    def transform(self, words):
        vecs = []
        for w in words:
            assert w in self.matrix
            vecs.append(self.matrix[w])
        return vecs

    def vector_norm(self, word):
        vec = self.matrix[word]
        return math.sqrt(sum(v**2 for v in vec.values()))

    def normalize_vectors(self):
        for w, vec in self.matrix.items():
            norm = self.vector_norm(w)

            for key in vec:
                vec[key] /= norm

        self.is_normalized = True

    def euclidean_distance(self, w1, w2):
        vec1, vec2 = self.transform((w1, w2))

        # Save computation by only computing values for features that
        # are active in one of the vectors.
        union = vec1.keys() | vec2.keys()

        return math.sqrt(sum((vec1[key] - vec2[key])**2
                             for key in union))

    def cosine_similarity(self, w1, w2):
        vec1, vec2 = self.transform((w1, w2))

        # Save computatoin by only computing values for features that
        # are active in both vectors
        intersect = set(vec1.keys()).intersection(vec2.keys())

        dot_product = sum(vec1[key]*vec2[key] for key in intersect)

        # Return dot product for normalized vectors
        if self.is_normalized:
            return dot_product
        else:
            return dot_product / (self.vector_norm(w1)*self.vector_norm(w2))

    def nearest_neighbors(self, w, k=5):
        if w in self.vocab:
            # Use heapq to efficienctly find the top k neighbors.
            return heapq.nlargest(k,
                                  ((other, self.cosine_similarity(w, other))
                                   for other in self.matrix if other != w),
                                  key=lambda x : x[1])

print("Loading corpus...")
sentences = preprocess(aviskorpus_10_nn.sentences())

vec = WordVectorizer(5000, 5)
vec.fit(sentences)

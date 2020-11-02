# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

"""The file contains two implementations:
1) A method to compute BLEU scores
2) A retrieval-based chatbot based on TF-IDF. 
"""


import collections
import math
import numpy as np


def get_sentences(text_file):
    """Given a text file with one (tokenised) sentence per line, returns a list 
    of sentences , where each sentence is itself represented as a list of tokens.
    The tokens are all converted into lowercase.
    """
    
    sentences = []
    fd = open(text_file)
    for sentence_line in fd:
        
        # We convert everything to lowercase
        sentence_line = sentence_line.rstrip("\n").lower()
        
        # We also replace special &apos; characters with '
        sentence_line = sentence_line.replace("&apos;", "'")
        
        sentences.append(sentence_line.split())
    fd.close()
    
    return sentences
    


def compute_precision(reference_file, output_file, ngram_order):
    """
    Computes the precision score for a given N-gram order. The first file contains the 
    reference translations, while the second file contains the translations actually
    produced by the system. ngram_order is 1 to compute the precision over unigrams, 
    2 for the precision over bigrams, and so forth.   
    """
    
    ref_sentences = get_sentences(reference_file)
    output_sentences = get_sentences(output_file)
    
    raise NotImplementedException()


def compute_brevity_penalty(reference_file, output_file):
    """Computes the brevity penalty."""
    
    ref_sentences = get_sentences(reference_file)
    output_sentences = get_sentences(output_file)
    
    raise NotImplementedException()

    
def compute_bleu(reference_file, output_file, max_order=4):
    """
    Given a reference file, an output file from the translation system, and a 
    maximum order for the N-grams, computes the BLEU score for the translations 
    in the output file.
    """
   
    precision_product = 1
    for i in range(1, max_order+1):
        precision_product *= compute_precision(reference_file, output_file, i) 
    
    brevity_penalty = compute_brevity_penalty(reference_file, output_file)
    
    bleu = brevity_penalty * math.pow(precision_product, 1/max_order)
    return bleu




class RetrievalChatbot:
    """Retrieval-based chatbot using TF-IDF vectors"""
    
    def __init__(self, dialogue_file):
        """Given a corpus of dialoge utterances (one per line), computes the
        document frequencies and TF-IDF vectors for each utterance"""
        
        # We store all utterances (as lists of lowercased tokens)
        self.utterances = []
        fd = open(dialogue_file)
        for line in fd:
            utterance = self._tokenise(line.rstrip("\n"))
            self.utterances.append(utterance)
        fd.close()
        
        self.doc_freqs = self._compute_doc_frequencies()
        self.tf_idfs = [self.get_tf_idf(utterance) for utterance in self.utterances]

        
    def _tokenise(self, utterance):
        """Convert an utterance to lowercase and tokenise it by splitting on space"""
        return utterance.strip().lower().split()

    
    def _compute_doc_frequencies(self):
        """Compute the document frequencies (necessary for IDF)"""
        
        doc_freqs = {}
        for utterance in self.utterances:
            for word in set(utterance):
                doc_freqs[word] = doc_freqs.get(word, 0) + 1
        return doc_freqs

    
    def get_tf_idf(self, utterance):
        """Compute the TF-IDF vector of an utterance. The vector can be represented 
        as a dictionary mapping words to TF-IDF scores. The utterance is a list of 
        (lowercased) tokens. """
        
        raise NotImplementedException()

    
    def _get_norm(self, tf_idf):
        """Compute the vector norm"""
        
        return math.sqrt(sum([v**2 for v in tf_idf.values()]))

    
    def get_response(self, query):
        """
        Finds out the utterance in the corpus that is closed to the query
        (based on cosine similarity with TF-IDF vectors) and returns the 
        utterance following it. 
        """

        # If the query is a string, we first tokenise it
        if type(query)==str:
            query = self._tokenise(query)
        
        raise NotImplementedException()
        
    
    def compute_cosine(self, tf_idf1, tf_idf2):
        """Computes the cosine similarity between two vectors"""
        
        raise NotImplementedException()
    

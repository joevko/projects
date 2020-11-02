Python 3.6.4 (default, Jan 25 2018, 13:11:40)
[GCC 4.8.5 20150623 (Red Hat 4.8.5-16)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import nltk
>>> dataset = nltk.corpus.brown.tagged_words()
s>>> dataset
[('The', 'AT'), ('Fulton', 'NP-TL'), ...]
>>> len(dataset)
1161192
>>> from nltk.probability import ConditionalFreqDist
>>> cfd = ConditionalFreqDist()
>>> for token,tag in dataset:
...     cfd[tag][token] += 1
...
>>> cfd
<ConditionalFreqDist with 472 conditions>
>>> cfd['AT']
FreqDist({'the': 62288, 'a': 21824, 'The': 6725, 'an': 3518, 'no': 1575, 'A': 1119, 'every': 434, 'No': 230, 'An': 188, 'Every': 56, ...})
>>> from nltk.probability import MLEProbDist
>>> from nltk.probability import ConditionalProbDist
>>> cpd = ConditionalProbDist(cfd, MLEProbDist)
>>> cpd
<ConditionalProbDist with 472 conditions>
>>> cpd['AT']
<MLEProbDist based on 97959 samples>
>>> cpd['AT'].prob('the')
0.6358578589001521
>>> cpd['AT'].logprob('the')
-0.6532237966397387
>>> cpd['AT'].logprob('The')
-3.8645718736556733
>>> cpd['AT'].prob('The')
0.06865117038761115
>>> cpd['NP-TL'].prob('Fulton')
0.002488181139586962
>>> cpd['AT'].prob('The')*cpd['NP-TL'].prob('Fulton')
0.000170816547369025
>>> import math
>>> 2**(cpd['AT'].logprob('The')+cpd['NP-TL'].logprob('Fulton'))
0.00017081654736902482
>>> cpd['AT'].prob('The')*cpd['NP-TL'].prob('Fulton')
0.000170816547369025
>>> 2**(cpd['AT'].logprob('The')+cpd['NP-TL'].logprob('Fulton'))
0.00017081654736902482
>>> cpd['AT'].prob('google')
0.0
>>> cpd['AT'].prob('The')*cpd['NP-TL'].prob('google')
0.0
>>> smoothing = 1e-20
1e-20
>>> cpd['AT'].prob('The')*smoothing
6.865117038761114e-22

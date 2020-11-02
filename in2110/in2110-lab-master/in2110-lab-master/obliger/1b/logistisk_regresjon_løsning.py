import urllib.request
import pandas, re, random
import numpy as np
import sklearn.linear_model, sklearn.metrics, sklearn.model_selection

ordfiler = {"norsk":"https://github.com/open-dict-data/ipa-dict/blob/master/data/nb.txt?raw=true",
        "arabisk":"https://raw.githubusercontent.com/open-dict-data/ipa-dict/master/data/ar.txt?raw=true",
        "finsk":"https://raw.githubusercontent.com/open-dict-data/ipa-dict/master/data/fi.txt?raw=true",
        "patwa":"https://raw.githubusercontent.com/open-dict-data/ipa-dict/master/data/jam.txt?raw=true",
        "farsi":"https://raw.githubusercontent.com/open-dict-data/ipa-dict/master/data/fa.txt?raw=true",
        "tysk":"https://raw.githubusercontent.com/open-dict-data/ipa-dict/master/data/de.txt?raw=true",
        "engelsk":"https://raw.githubusercontent.com/open-dict-data/ipa-dict/master/data/en_UK.txt?raw=true",
        "rumensk":"https://raw.githubusercontent.com/open-dict-data/ipa-dict/master/data/ro.txt?raw=true",
        "khmer":"https://raw.githubusercontent.com/open-dict-data/ipa-dict/master/data/km.txt?raw=true",
        "fransk":"https://raw.githubusercontent.com/open-dict-data/ipa-dict/master/data/fr_FR.txt?raw=true",
        "japansk":"https://raw.githubusercontent.com/open-dict-data/ipa-dict/master/data/ja.txt?raw=true",
        "spansk":"https://raw.githubusercontent.com/open-dict-data/ipa-dict/master/data/es_ES.txt?raw=true",
         "svensk":"https://raw.githubusercontent.com/open-dict-data/ipa-dict/master/data/sv.txt?raw?true",
         "koreansk":"https://raw.githubusercontent.com/open-dict-data/ipa-dict/master/data/ko.txt?raw?true",
         "swahilisk":"https://raw.githubusercontent.com/open-dict-data/ipa-dict/master/data/sw.txt?raw?true",
         "vietnamesisk":"https://raw.githubusercontent.com/open-dict-data/ipa-dict/master/data/vi_C.txt?raw?true",
        "mandarin":"https://raw.githubusercontent.com/open-dict-data/ipa-dict/master/data/zh_hans.txt?raw?true",
        "malayisk":"https://raw.githubusercontent.com/open-dict-data/ipa-dict/master/data/ma.txt?raw?true",
        "kantonesisk":"https://raw.githubusercontent.com/open-dict-data/ipa-dict/master/data/yue.txt?raw?true",
         "islandsk":"https://raw.githubusercontent.com/open-dict-data/ipa-dict/master/data/is.txt?raw=true"}

def extract_wordlist(max_nb_words_per_language=20000):
    """
    Laster ned fra Github en rekke ordlister med ord og deres phonetiske transkripsjoner i flere språk.
    Ordlistene er deretter satt sammen i en pandas DataFrame, og delt i en treningsett og en testsett.
    """

    wordlist = []
    for lang, wordfile in ordfiler.items():
        print("Nedlasting av ordisten for", lang, end="... ")
        data = urllib.request.urlopen(wordfile)
        wordlist_for_language = []
        for linje in data:
            linje = linje.decode("utf8").rstrip("\n")
            word, transcription = linje.split("\t")

            # vi tar den første transkripsjon (hvis det finnes flere)
            # og fjerner slashtegnene ved start og slutten
            match = re.match("/(.+?)/", transcription)
            if not match:
                continue
            transcription = match.group(1)
            wordlist_for_language.append({"ord":word, "IPA":transcription, "språk":lang})
        data.close()
        random.shuffle(wordlist_for_language)
        wordlist += wordlist_for_language[:max_nb_words_per_language]
        print("ferdig!")

    # Nå bygger vi en DataFrame med alle ordene
    wordlist = pandas.DataFrame.from_records(wordlist)

    # Og vi blander sammen ordene i tilfeldig rekkefølge
    wordlist = wordlist.sample(frac=1)

    # Lage et treningssett og en testsett (med 10% av data)
    wordlist_train, wordlist_test = sklearn.model_selection.train_test_split(wordlist, test_size=0.1)
    print("Treningsett: %i eksempler, testsett: %i eksempler"%(len(wordlist_train), len(wordlist_test)))

    return wordlist_train, wordlist_test


class LanguageIdentifier:
    """Logistisk regresjonsmodell som tar IPA transkripsjoner av ord som input,
    og predikerer hvilke språkene disse ordene hører til."""

    def __init__(self):
        """Initialisere modellen"""
        self.model = sklearn.linear_model.LogisticRegression(solver="lbfgs", multi_class='ovr', n_jobs=-1)
        #self.model = sklearn.linear_model.SGDClassifier(loss="log", n_jobs=-1)
        self.symbols = []
        self.languages =[]

    def train(self, transcriptions, languages):
        """Gitt en rekke med IPA transkripsjoner og en rekke med språknavn, trene
        den logistisk regresjonsmodellen. De to rekkene må ha samme lendgen"""

        self.symbols = self._extract_unique_symbols(transcriptions)

        feats = self._extract_feats(transcriptions)

        # Vi ekstrahere en liste over alle mulige språknavn
        self.languages = sorted(set(languages))
        # Vi konvertere liste over språk til heltall
        outputs = [self.languages.index(lang) for lang in languages]

        print("Starte trening", end="... ")
        self.model.fit(feats, outputs)
        print("ferdig")

    def _extract_unique_symbols(self, transcriptions, min_nb_occurrences=10):
        """Gitt en rekke med IPA fonetiske transkripsjoner, ektrahere en liste med alle IPA
        symboler som finnes i transkripsjonene og forekommer minst min_nb_occurrences."""
        # Vi må først finne ut hvilke IPA symboler skal brukes som features

        print("Starte preprocessering", end="... ")
        symbols = {}
        for transcription in transcriptions:
            for symbol in transcription:
                symbols[symbol] = symbols.get(symbol, 0) + 1
        print("ferdig")

        # Vi tar bare symboler som forekommer mer enn 10 ganger
        symbols = sorted([p for p,c in symbols.items() if c > 10])
        return symbols

    def _extract_feats(self, transcriptions):
        """Gitt en rekke med IP transkripsjoner, ekstrahere en matrise av størrelse |T|x|F|,
        hvor |T| er antall transkripsjoner, og |F| er antall features brukt i modellen."""

        print("Starte featureekstrahering", end="... ")
        feats = np.zeros((len(transcriptions), len(self.symbols)))
        symbol_indices = {p:i for i, p in enumerate(self.symbols)}
        for i, transcription in enumerate(transcriptions):
            for p in transcription:
                if p in symbol_indices:
                    feats[i, symbol_indices[p]] = 1
        print("ferdig")
        return feats

    def predict(self, transcriptions):
        """Gitt en rekke med IPA transkripsjoner, finne ut den mest sansynnlige språk
        for hver transkripsjon. Rekken som returneres må ha samme lengden som inputrekken"""

        feats = self._extract_feats(transcriptions)
        outputs = self.model.predict(feats)
        outputs = [self.languages[i] for i in outputs]
        return outputs

    def evaluate(self, transcriptions, languages):
        """Gitt en rekke med IPA transkripsjoner og en rekke med språknavn, evaluere hvor godt
        modellen fungerer ved å beregne:
        1) accuracy
        2) precision, recall og F1 for hvert språk
        3) micro- og macro-averaged F1.
        """

        predictions = self.predict(transcriptions)
        accuracy = sklearn.metrics.accuracy_score(languages, predictions)
        print("Global accuracy:", accuracy)

        scores_per_language = sklearn.metrics.precision_recall_fscore_support(languages, predictions, average=None)
        scores_per_language = pandas.DataFrame(scores_per_language).T
        scores_per_language.index = self.languages
        scores_per_language.columns = ["precision", "recall", "f1", "support"]
        print("Scores per language:\n", scores_per_language[["precision", "recall", "f1"]])

        micro_f1 = sklearn.metrics.f1_score(languages, predictions, average="micro")
        macro_f1 = sklearn.metrics.f1_score(languages, predictions, average="macro")
        print("Micro F1: %.8f, Macro F1: %.3f"%(micro_f1, macro_f1))
        print("Micro precision", sklearn.metrics.precision_score(languages,predictions, average="micro"))
        print("Micro recall", sklearn.metrics.recall_score(languages, predictions, average="micro"))

#######################
# Brukseksempel:
#######################
if __name__ == "__main__":

    # Vi laster ned dataene (vi trenger kun å gjøre det én gang)
    train_data, test_data = extract_wordlist()

    # Vi teller antall ord per språk
    print("Statistikk over språkene i treningsett:")
    print(train_data.språk.value_counts())
    print("Første 30 ord:")
    print(train_data[:30])

    # Vi bygge og trene modellen
    model = LanguageIdentifier()
    transcriptions = train_data.IPA.values
    languages = train_data.språk.values
    model.train(transcriptions, languages)

    # Vi kan nå test modellen på nye data
    predicted_langs = model.predict(["konstituˈθjon", "ɡrʉnlɔʋ", "stjourtnar̥skrauːɪn", "bʊndɛsvɛɾfaszʊŋ"])
    print("Mest sansynnlige språk for ordene:", predicted_langs)

    # Til slutt kan vi evaluere hvor godt modellen fungerer på testsett
    model.evaluate(test_data.IPA.values, test_data.språk.values)

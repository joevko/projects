# Lab 1 – Oppvarming

## Utviklingsmiljø

Det ligger et ferdig utviklingsmiljø på IFI-klyngen. Dette kan brukes på IFI sine Linux-terminaler, eller via ssh på 
login.ifi.uio.no. Det kan også installeres på egen maskin, men dette er kun anbefalt for de som har erfaring med Linux fra før.
Koden for å sette opp eget miljø ligger her: https://github.uio.no/IN2110/in2110-shared

For å starte miljøet, kjør:

```
$ ~henraskj/IN2110/in2110-shared/in2110-shell
```

Nå er du inne i IN2110-miljøet og kan starte Python:

```
$ python
```

Her har du tilgang til en rekke Python-moduler for NLP og datasett på både Norsk og engelsk.

## Oppgave 1 – Tokenisering
> *NB: Om du kjører utviklingsmiljøet på egen maskin og får en error kan du kjøre denne kommandoen for å installere punkt i NLTK:*
>
> ```
> $ python -m nltk.downloader punkt
> ```

Før vi kan prosessere tekst er det viktig at den er pre-prossesert. Det finnes mange grader av pre-prossesering, men vi vil
stort sett alltid ønske å tokenisere teksten. Start med å hente ut et dokument fra NoReC (sentimentdatasett utviklet her på IFI
av språkgruppen):

```python
from in2110.corpora import norec

doc = norec.get_document("105812.txt")
```

### a) Splitte på mellomrom

Den enkleste formen for tokenisering er å splitte på mellomrom. Tokeniser `doc` med denne metoden. Ser du noen problemer?

### b) NLTK

NLTK kommer med en egen tokenizer. Denne er utviklet for engelsk, men kan også brukes på norsk. Eksempel:

```python
from nltk import word_tokenize

word_tokenize(doc)
```

Tokeniser `doc` med `word_tokenize()`. Hvor bra fungerer den for norsk?

### c) UDTK

UDPipe er et verktøy for å trene modeller for tokenisering, lemmatisering, POS-tagging og dependensparsing. Grensesnittet
er dessverre ikke veldig brukervenlig, men vi har laget en enkel tokeniserer basert på UDPipe som dere kan bruke. Denne er
trent på norske versjonen av Universal Dependencies. Eksempel:

```python
from udtk import Model
m = Model("norwegian-bokmaal")

m.tokenize(doc)
```

Hvordan fungerer denne?

### d) Setningssegmentering

Noen ganger vil vi også dele opp teksten i setninger. For dette finnes det en pakke i NLTK som har en modell for norsk:

```python
import nltk.data
segmenter = nltk.data.load("tokenizers/punkt/norwegian.pickle")

segmenter.tokenize(doc)
```


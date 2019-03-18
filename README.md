# Capitain Corpus Reader

## What is it?

An NLTK-like corpus readers that works with TEI XML files compatible with the 
[Capitains Tool Suite](http://capitains.org/pages/guidelines).

This reader is designed to work together with the rest of the awesome stuff of the [CLTK](http://cltk.org/). It
allows users to load the latest XML files from the Perseus Project and the 
[1st 1000 Years of Greek](https://github.com/OpenGreekAndLatin/First1KGreek). It provides access to the usual methods and properties of an [NLTK Corpus reader](http://www.nltk.org/howto/corpus.html).

Moreover, it allows users to access both words *and canonical citations*!

```python
>>> from capitain_corpus_reader.reader import CapitainCorpusReader
>>> root = "~/cltk_data/greek/text/canonical-greekLit-master/data"
>>> corpus = CapitainCorpusReader(root, "tlg0003/tlg001/.*\-grc2.xml")
>>> corpus.fileids() # Thuc, Historiae...
['tlg0003/tlg001/tlg0003.tlg001.perseus-grc2.xml']
>>> corpus.cite_words('tlg0003/tlg001/tlg0003.tlg001.perseus-grc2.xml')
('1.1.1', 'Θουκυδίδης'),
 ('1.1.1', 'Ἀθηναῖος'),
 ('1.1.1', 'ξυνέγραψε'),
 ...
>>> cite_sents = corpus.cite_sents('tlg0003/tlg001/tlg0003.tlg001.perseus-grc2.xml')
>>> cite_sents[1]
[('1.1.2', 'κίνησις'),
 ('1.1.2', 'γὰρ'),
 ('1.1.2', 'αὕτη'),
 ('1.1.2', 'μεγίστη'),
...
 ('1.1.2', 'ἀνθρώπων'),
 ('1.1.2', '.')]


```

Note that the corpus reader is heavily inspired (not to say I did a lot of copy/paste) by the `tei.py` [script](https://github.com/cltk/cltk/blob/c44eb1810c5a85b0409a2537177862468987bd13/cltk/corpus/greek/tei.py) in CLTK.

The readers does pretty much the same things, but: a. reads the original TEI XML files, instead of converting them to txt b. implements a couple of new methods to get citable words and citable sentences (as in the sample code above).

## Requirements

Python 3! I tested it with 3.4 and 3.6.

It also requires (as specified in the `setup.py`) NLTK and MyCapitain.

## Install

Clone this project to a local folder, then:

```bash
cd <your-local-folder>
pip install .

```

Or you can try to install it directly from GitHub:

```bash
pip install git+https://github.com/francescomambrini/capitain_corpus_reader.git

```

I suggest you use a `virtualenv` to test the package.

## Tests

I wrote only a couple of very simple tests, which use the included sample file (Aristotle, **Historia Animalium**, 
from the 1st1kYearsGreek). You'll need `pytest` to run them.

The easiest way to run them is to download/clone the project, then launch the test file from within the `tests` directory:

```bash
pip install pytest # in case you need it...
cd <root-of-project>/capitain_corpus_reader/tests
pytest --verbose test_capitain_reader.py

```

## Known limitations

In general, I work more on Greek than Latin, thus I tested the reader primarily with Greek texts. 
It shouldn't have any problem with Latin texts, but the default options of the class constructors may be rahter biased...

A couple of warnings:
1. it **only** works with RegexpTokenizers, as I didn't find any better way to keep citations and tokens in sync than to use the spans and span tokenizers...
2. it **only** works with fully Capitains-compliant texts, those that pass [Capitains' Hook Tests](http://capitains.org/pages/tools#testing-resources--hook); that means: some (but not all!) of the newest Perseus XML files; all (afaIk) of the 1stkYeasrsOfGreek and Open Greek and Latin. That's why you should checkout the latest version of Perseus Latin and Greek lib from Github before you try it.

Do keep in mind that I am only an amateur that likes working with Python, Greek and Latin! Any observation, report and everything that can improve my poor code is more than welcome!

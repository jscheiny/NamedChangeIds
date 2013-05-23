changeIdName.py
===============

Provides useful and funny names for your git / whatever change ID (or really any
long hex string that you need to refer to). Names for change IDs are given as
adjective noun phrases.

## Usage

Working on a good CLI, but for the moment, just import changeIdName and use one
of the following methods `changeIdPhraseStandard` or `moreFrequentChangeIdPhrase`.

Both give good results. The first function will give a name that may be less
frequent (in terms of the English language) but is less likely to collide wit
the names of other change IDs. The second method will give a name with more
frequently used english words, but it is more likely to collide with the names
of other change IDs. I don't think collisions are super likely, but they are
pretty possible.

## Resources

To make it work you'll need the resources folder with only three of the included
files: `adjectives-sub.dawg`, `nouns-sub.dawg`, and `noun-adj-freqs.txt`

The other resources may be useful to you, and are as follows:

+ `adjectives-sub.dawg` -- The .dawg file computed from `adjectives-sub.txt`
+ `adjectives-sub.txt` -- The subset of adjectives for which I had frequency data
+ `adjectives.dawg` -- The .dawg file computed from `adjectives.txt`
+ `adjectives.txt` -- A list of adjectives in the English language
+ `noun-adj-freqs.txt` -- A list of all the nouns and adjectives with their frequencies
+ `nouns-sub.dawg` -- The .dawg file computed from `nouns-sub.txt`
+ `nouns-sub.txt` -- The subset of nouns for which I had frequency data
+ `nouns.dawg` -- The .dawg file computed from `nouns.txt`
+ `nouns.txt` -- A list of nouns in the English language
+ `twl06.dawg` -- The .dawg file computed from `twl06.txt`
+ `twl06.txt` -- The 2006 Tournament Word List, complete Scrabble word list
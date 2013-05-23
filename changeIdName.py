#!/usr/bin/python

import re
import sys
from Dawg import *

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

ADJECTIVES = Dawg('resources/adjectives-sub.dawg')
NOUNS = Dawg('resources/nouns-sub.dawg')
FREQS = {w:int(f) for (w,f) in (l.split(' ') for l in open('resources/noun-adj-freqs.txt'))}

def convert26(h):
  """
  hex -> base 26 (letters only)
  """
  d = int(h, 16)
  l = []
  while d > 0:
    l.append(ALPHABET[d % 26])
    d /= 26
  return ''.join(l[::-1])

class LongestWordTracker:
  def __init__(self):
    self.word = ''

  def update(self, word):
    if len(word) > len(self.word):
      self.word = word;

def findLongestWordSubseq(search, dawg):
  """
  Returns the longest subsequence of the search string that is a member of the
  langauge defined by the contents of the dawg.
  """
  def findLongestWordSubseqHelper(search, prefix, root, tracker):
    if root.hasChild(Dawg.Node.EOW):
      tracker.update(prefix)
    visited = set([])
    for i in range(len(search)):
      letter = search[i]
      if letter not in visited:
        visited.add(letter)
        if root.hasChild(letter):
          findLongestWordSubseqHelper(search[i + 1:], prefix + letter, \
                                      root.getChild(letter), tracker)
  tracker = LongestWordTracker()
  findLongestWordSubseqHelper(search, '', dawg.root, tracker)
  return tracker.word

def rotations(s, n=len(ALPHABET)):
  """
  Returns a generator which iterates through all the rotations of the given
  alphabetic string, starting with the original string.
  """
  rotations.rotateChar = lambda c: ALPHABET[(ALPHABET.index(c) + 1) % len(ALPHABET)]
  rotations.rotate = lambda s: ''.join(rotations.rotateChar(c) for c in s)
  for i in range(n):
    yield s
    s = rotations.rotate(s)

def changeIdPhrase(changeIdBase26):
  """
  Returns the change ID name for a given change ID thats already been converted
  to base
  """
  adj = findLongestWordSubseq(changeIdBase26, ADJECTIVES)
  noun = findLongestWordSubseq(changeIdBase26, NOUNS)
  return adj + ' ' + noun

def changeIdPhraseStandard(changeId):
  """
  Returns a name for the given change ID which is an adjective noun phrase.
  """
  if changeId[0] == 'I':
    changeId = changeId[1:]
  b26 = convert26(changeId)
  return changeIdPhrase(convert26(changeId))

def moreFrequentChangeIdPhrase(changeId):
  """
  Returns a name for the given change ID which is an adjective noun phrase with
  slightly higher English frequency.
  """
  if changeId[0] == 'I':
    changeId = changeId[1:]
  b26 = convert26(changeId)
  bestPhrase = ''
  bestPhraseFreq = -1
  for rot in rotations(b26):
    phrase = changeIdPhrase(rot)
    freq = sum(FREQS[w] for w in phrase.split(' '))
    if freq > bestPhraseFreq:
      bestPhrase = phrase
      bestPhraseFreq = freq
  return bestPhrase

def main():
  changeIdPattern = re.compile('I?[0-9a-fA-f]{40}$')
  for arg in sys.argv[1:]:
    if re.match(changeIdPattern, arg) != None:
      print arg + ':'
      print '\t' + changeIdPhraseStandard(arg)
      print '\t' + moreFrequentChangeIdPhrase(arg)

if __name__ == '__main__':
  main()

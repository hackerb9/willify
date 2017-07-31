#!/usr/bin/python

# George F. Will is known for high-falutin words.
# Is he a human thesaurus or does he use a program like this? :-)
#
# This script replaces word with synonyms in a text document.


# Usage:
#
#     ./willify.py [ filename.txt ... ]
#
# You can also read from stdin

# hackerb9 2017
# GPL 3+

import dictclient
import re
import fileinput
import sys
from random import choice

# If you have dictd installed on your localhost, use this:
dictd = dictclient.Connection()

# If you don't have dictd, you can try connecting to an online dictionary:
#dictd = dictclient.Connection('dictd.org')


def wnsyns(word):
    result=[word]
    for definition in dictd.define('wn', word):
        s = definition.getdefstr()
        s = re.sub('-\n', '-', s)
        s = re.sub('\n', ' ', s)
        for synonyms in re.findall('\[syn: [^]]*\]', s):
            result.extend(re.findall('(?:{([^}]*)})', synonyms))
    return result

def mobysyns(word):
    result=[word]
    for definition in dictd.define('moby-thesaurus', word):
        s = definition.getdefstr()
        s = s.strip()
        s = re.sub('[^:]*:\n', '', s)
        s = re.sub('\n', ' ', s)
        result.extend(re.split(', ', s))
    return result

def synonyms(word):
    if len(word) <= 2:
        return [word]
    a=wnsyns(word)
    a.extend(mobysyns(word))
    a = list(set(a))
    a.sort()
    return a


def pickbest(syns):
    '''Given a list of synonyms, return just the "best" one'''
    # Maybe pick most sesquipedalian?
    # For now, just pick a random synonym.
    return choice(syns)


# Main

for line in fileinput.input():
    for (nonword, word) in re.findall('(\W*)(\w*)', line):
        sys.stdout.write(nonword)
        syns = synonyms(word)   # All possible synonyms
        sys.stdout.write(pickbest(syns))



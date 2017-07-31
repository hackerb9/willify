# Willify
Given boring words, output exciting, George F. Will-quality words.

*Granted ho-hum language, yield blue blood,
George (atomic number 9) Will-calibre lyrics.*

## Usage

    ./willify.py filename.txt

## Requirements

You'll need python dictclient: `apt-get install python-dictclient`.


## Optional

If you don't want to connect to dict.org, you can run dictd on your
own machine. This is pretty simple: `apt-get install dictd dict-wn
dict-moby-thesaurus`. Then change this line:

    dictd = dictclient.Connection('dict.org')

to

    dictd = dictclient.Connection()

## BUGS

None! Those are features!

## FUTURE 

Well, since this is just a joke, I'm probably not going to actually do
anything better with this, but the next logical steps would be:

1. Use word frequency charts to pick the least common synonym and
   replace it directly in the text instead of offering a ton of
   synonyms. (Alternately, use the most common word).

2. Output a web page that shows the text, but allows one to click on
   any word to select a synonym.

3. Read from a URL, so this can act as a filter.

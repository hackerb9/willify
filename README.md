# Willify
Given boring words, output exciting, George F. Will-quality words.
[Willified: *Granted ho-hum language, yield blue blood, George (atomic number 9) Will-calibre lyrics.*]

____

[George F. Will](https://www.washingtonpost.com/people/george-f-will/) is known for high-falutin words. | Here's an actual example of his writing from an editorial he wrote in the [Washington Post](https://www.washingtonpost.com/opinions/what-the-freedom-caucus-stands-for/2017/04/12/7477a632-1ee8-11e7-a0a7-8b2a45e3dc84_story.html):
-|-
![George F. Will's Head](README.md.d/bigwill.png) | *With a mellifluous name suggesting bucolic tranquility, Rep. Mark Meadows, a North Carolina Republican, is an unlikely object of the caterwauling recently directed at him and the House Freedom Caucus he leads. The vituperation was occasioned by the HFC’s role rescuing Republicans from embracing an unpopular first draft of legislation to replace Obamacare.*

Is he a human thesaurus or does he use a program like this? :-)


## Usage

    ./willify.py filename.txt

## Requirements

You'll need python dictclient: `apt-get install python-dictclient`.

## Example

Original | Willified
---------|----------
*Come down, Dick.*                | Enter downward, Private eye.
*Come and see.*                   | Move along and back.
*See the big, big mother.*        | Inspect the great, excellent agent.
*See the funny little baby.*      | Come to the jocose exiguous nestling.
*Puff is my baby.*                | Flatulency is my preemie.
*Puff is my funny little baby.*   | Inhale is my fishy constricted mewling infant.
*I see the big mother.*           | I establish the cloyed fuss.
*I see the little baby.*          | I consider the immaterial honey.
*Look Jane.*                      | Spot Jane.
*See the big father.*             | Find out the exalted something.



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

# -*- coding: utf-8 -*-

import nltk
from nltk import *

# File opener
with open ("grammar.cfg", "r") as grammar_file:
    grammarText = grammar_file.read()

with open('text.txt', 'r') as content_file:
    story = content_file.read()

print('\n' + story)

# Text Modifier
def conjonction_replacer(story):
    conjonctions = [', mais',', car',', par contre',', mais']
    for conjonction in conjonctions:
        story = story.replace(conjonction, '.')
    return story

def negation_replacer(story):
    return story

# Story Analyser
grammar = grammar.FeatureGrammar.fromstring(grammarText)
parser = nltk.ChartParser(grammar)

story = conjonction_replacer(story)

sentences = story.split('.')
subject = ""

for sentence in sentences:
    sentence = sentence.replace('il', subject)
    print(sentence)
    tokens = sentence.split()
    parser = parse.FeatureEarleyChartParser(grammar)
    trees = parser.parse(tokens)
    for tree in trees:
        print(tree)
        #nltk.draw.tree.draw_trees(tree)
        s = str(tree.label()['SEM'])
        print(s + '\n')
        subject = s[s.index('subject(') + 8: s.index(')')]
        #print(subject)
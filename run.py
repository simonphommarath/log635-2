# -*- coding: utf-8 -*-

import nltk
from nltk import *

with open ("grammar.cfg", "r") as myfile:
    grammaireText=myfile.read()

with open('text.txt', 'r') as content_file:
    content = content_file.read()

grammar = grammar.FeatureGrammar.fromstring(grammaireText)
parser = nltk.ChartParser(grammar)


content = content.replace(', mais', '.')
#content = content.replace('il', 'Le corps')
subject = ""

for phrase in content.split('.'):
    phrase = phrase.replace('il', subject)
    print(phrase)
    tokens = phrase.split()
    parser = parse.FeatureEarleyChartParser(grammar)
    trees = parser.parse(tokens)
    for tree in trees:
        print(tree)
        #nltk.draw.tree.draw_trees(tree)
        s = str(tree.label()['SEM'])
        print(s)
        subject = s[s.index('subject(') + 8: s.index(')')]
        print(subject)


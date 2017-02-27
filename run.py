# -*- coding: utf-8 -*-

import nltk
from nltk import *

with open ("grammar-final.cfg", "r") as myfile:
    grammaireText=myfile.read()

grammar = grammar.FeatureGrammar.fromstring(grammaireText)
parser = nltk.ChartParser(grammar)


for phrase in "Le corps est brulé. Han était sur Naboo.".split('.'):
    tokens = phrase.split()
    parser = parse.FeatureEarleyChartParser(grammar)
    trees = parser.parse(tokens)
    for tree in trees:
        print(tree)
        nltk.draw.tree.draw_trees(tree)
        print(tree.label()['SEM'])

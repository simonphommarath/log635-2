# -*- coding: utf-8 -*-

import nltk
from nltk import *

# File opener
with open ("grammar.cfg", encoding='utf-8', mode="r") as grammar_file:
    grammarText = grammar_file.read()

with open('text.txt', encoding='utf-8', mode='r') as content_file:
    story = content_file.read()

print('\n' + story)

# Text Modifier
def conjonction_replacer(story):
    conjonctions = [', mais ',', car ',', par contre ',' et ']
    for conjonction in conjonctions:
        story = story.replace(conjonction, '. ')
    return story

def negation_replacer(story):
    return story

# Story Analyser
grammar = grammar.FeatureGrammar.fromstring(grammarText)
parser = nltk.ChartParser(grammar)

story = conjonction_replacer(story)

sentences = story.split('.')
subject = ""
jess = "(deffact fact \n"

for sentence in sentences:
    sentence = sentence.replace(' il ', subject+ ' ')
    print(sentence)
    tokens = sentence.split()
    parser = parse.FeatureEarleyChartParser(grammar)
    
    sent = ['#NUM#' if i.isdigit() else i for i in tokens]
    numbers = [i for i in tokens if i.isdigit()]
    
    trees = parser.parse(sent)

    for tree in trees:
        print(tree)
        nltk.draw.tree.draw_trees(tree)
        s = str(tree.label()['SEM']) 
        for n in numbers:
            s = s.replace('#NUM#', n, 1)
        print(s + '\n')
	#JessReformat
        facts = s[:len(s)-2].split('&')
        fact = facts[1].split("(")
        jess += "\t(" + fact[0] + " " + fact[1] + ")\n"
        subject = s[s.index('subject(') + 8: s.index(')')]
        print(subject + '\n')
        break
jess += ")"
with open('fact.clp','w') as f:
    f.write(jess)

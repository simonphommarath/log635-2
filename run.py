# -*- coding: utf-8 -*-

import nltk
from nltk import *

# File opener
with open ("grammar.cfg", encoding='utf-8', mode="r") as grammar_file:
    grammarText = grammar_file.read()

with open('text.txt', encoding='utf-8', mode='r') as content_file:
    story = content_file.read()

print('\n' + story + '\n')

# Text Modifier
def conjonction_replacer(story):
    conjonctions = [', mais ',', car ',', par contre ',' et ']
    for conjonction in conjonctions:
        story = story.replace(conjonction, '. ')
    return story

def relationClause_splitter(sentences):
    RP = 'qui'
    for index, sentence in enumerate(sentences):
        if RP in sentence:
            subSentence = sentence.split(', ')
            newSentence1 = subSentence[0] + ' ' + subSentence[2]
            newSentence2 = subSentence[1].replace(RP, subSentence[0])
            sentences.extend([newSentence1, newSentence2])
            del sentences[index]
    return sentences

# Story Analyser
grammar = grammar.FeatureGrammar.fromstring(grammarText)
parser = nltk.ChartParser(grammar)

story = conjonction_replacer(story)

sentences = story.split('.')
sentences = relationClause_splitter(sentences)

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
jess += ")"
with open('fact.clp','w') as f:
    f.write(jess)

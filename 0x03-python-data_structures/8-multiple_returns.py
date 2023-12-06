#!/usr/bin/python3

def multiple_returns(sentence):
    g = len(sentence)
    return g, sentence[0] if g > 0 else None

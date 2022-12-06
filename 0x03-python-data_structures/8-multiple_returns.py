#!/usr/bin/python3
def multiple_returns(sentence):
    len_str = len(sentence)
    return (len_str, sentence[0] if len_str > 0 else None)

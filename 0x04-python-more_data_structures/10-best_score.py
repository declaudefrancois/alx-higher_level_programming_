#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return (None)

    score_tuples = [(a_dictionary[k], k) for k, a in a_dictionary.items()]
    score_tuples = sorted(score_tuples, key=lambda s: s[0])
    return (score_tuples[len(score_tuples) - 1][1] if len(score_tuples) > 0
            else None)

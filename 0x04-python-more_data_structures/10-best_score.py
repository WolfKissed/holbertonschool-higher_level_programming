#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
         m = a_dictionary.keys[0]
        for i in a_dictionary.items:
            if i > m:
                m = i
        return m

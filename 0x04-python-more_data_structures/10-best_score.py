#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        i = list(a_dictionary.keys())[0]
         m = a_dictionary[i]
        for j, k in a_dictionary.items():
            if k > m:
                m = k
                i = j
        return i

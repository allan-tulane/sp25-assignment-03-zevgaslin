import math, queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'),
              ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'),
              ('relev--ant', '-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]


def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions
    if (S == ""):
        return (len(T))
    elif (T == ""):
        return (len(S))
    else:
        if (S[0] == T[0]):
            return (MED(S[1:], T[1:]))
        else:
            return (1 + min(MED(S, T[1:]), MED(S[1:], T)))


def fast_MED(S, T, MED={}):
    # TODO -  implement top-down memoization
    if (S, T) in MED:
        return MED[(S, T)]

    if not S:
        return len(T)
    if not T:
        return len(S)

    if S[0] == T[0]:
        MED[(S, T)] = fast_MED(S[1:], T[1:], MED)
    else:
        insert = fast_MED(S, T[1:], MED) + 1
        delete = fast_MED(S[1:], T, MED) + 1

        MED[(S, T)] = min(insert, delete)

    return MED[(S, T)]


def fast_align_MED(S, T, MED=None):
    if MED is None:
        MED = {}
    if (S, T) in MED:
        return MED[(S, T)]

    # Base cases
    if S == "":
        alignment = ("-" * len(T), T)
        MED[(S, T)] = alignment
        return alignment
    if T == "":
        alignment = (S, "-" * len(S))
        MED[(S, T)] = alignment
        return alignment

    if S[0] == T[0]:
        align_S, align_T = fast_align_MED(S[1:], T[1:], MED)
        result = (S[0] + align_S, T[0] + align_T)
        MED[(S, T)] = result
        return result

    insert_S, insert_T = fast_align_MED(S, T[1:], MED)
    insert_result = ("-" + insert_S, T[0] + insert_T)
    insert_cost = 1 + sum(a != b
                          for a, b in zip(*insert_result))

    delete_S, delete_T = fast_align_MED(S[1:], T, MED)
    delete_result = (S[0] + delete_S, "-" + delete_T)
    delete_cost = 1 + sum(a != b
                          for a, b in zip(*delete_result))

    sub_S, sub_T = fast_align_MED(S[1:], T[1:], MED)
    sub_result = (T[0] + sub_S, T[0] + sub_T)
    sub_cost = (1 if S[0] != T[0] else 0) + sum(
        a != b for a, b in zip(*sub_result))  

    # Choose the min cost
    best_result = min([(insert_cost, insert_result),
                       (delete_cost, delete_result), (sub_cost, sub_result)],
                      key=lambda x: x[0])[1]

    MED[(S, T)] = best_result
    return best_result

#!/bin/python3

# you can write to stdout for debugging purposes, e.g.
# ADDITIONAL COMPARISON EXAMPLES
# -----------------------, -------
#
# 4249 >  3132
# 1299 >  6788
# 1122 >  9987
# 4446 <  5553
# 4554 == 5544
# 9911 >  8877
# 3799 <  4144


def as_list(str):
    """get a list from"""

    return [*str]


def count_cards(p):
    """return number of pairs in p"""

    uniq_cards = set(p)
    c_occ = {}
    for c in uniq_cards:
        c_occ[c] = p.count(c)

    return c_occ


def get_winner(p1, p2):
    """get winner"""

    def swap_k_v(d):
        # print(f"D: {d.items()}")
        return [(v, k) for k, v in d.items()]

    def swap_sort(l):
        l.sort(key=lambda a: (a[0], a[1]), reverse=True)
        return l

    p1_hands = count_cards(as_list(str(p1)))
    p2_hands = count_cards(as_list(str(p2)))
    print(f"p1_hand {p1_hands} p2_hand {p2_hands}")

    p1_hands_v_k = swap_k_v(p1_hands)
    # print(p1_hands_v_k)
    p2_hands_v_k = swap_k_v(p2_hands)
    # print(p2_hands_v_k)

    print("swap_sort")
    p1_hands_v_k_swap = swap_sort(p1_hands_v_k)
    # print(p1_hands_v_k_swap)
    p2_hands_v_k_swap = swap_sort(p2_hands_v_k)
    # print(p2_hands_v_k_swap)

    res1 = p1_hands_v_k_swap
    res2 = p2_hands_v_k_swap

    if res1 == res2:
        return "DRAW"
    if res1 > res2:
        return p1
    if res2 > res1:
        return p2


def simple_poker(p1: int, p2: int):
    """doc
    simple_poker

    """
    res = get_winner(p1, p2)
    print(f"winner is  {res}")


# test
print(simple_poker(4554, 5544))
print(simple_poker(4446, 5553))
print(simple_poker(9911, 8877))

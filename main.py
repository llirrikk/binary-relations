from typing import Callable
import utils
from detect_relation_types import *


def main(M: tuple, tau: Callable[[int, int], bool]) -> None:
    utils.new_section("M", need_first_nl=False)
    print(M)

    utils.new_section("M * M")
    for i in range(len(M)):
        for j in range(len(M)):
            print(f"({M[i]},{M[j]})", end="\t")
        print()

    utils.new_section("M * M (with tau)")
    taus = set()
    for i in range(len(M)):
        for j in range(len(M)):
            if tau(M[i], M[j]):
                taus.add(Pair(x=M[i], y=M[j]))
                print(f"({M[i]},{M[j]})", end="\t")
            else:
                print("-", end="\t")
        print()

    utils.new_section("properties of binary relations")
    which_relation = WhichRelation(
        reflexive_relation=is_reflexive_relation(M, taus),
        symmetric_relation=is_symmetric_relation(M, taus),
        antisymmetric_relation=is_antisymmetric_relation(M, taus),
        transitive_relation=is_transitive_relation(M, taus),
    )

    for relation in which_relation._fields:
        if getattr(which_relation, relation).is_belong_to_type:
            print(f"{relation}\t+")
        else:
            print(f"{relation}\t-\t{getattr(which_relation, relation).message}")

    utils.new_section("types of binary relations")
    print(f"equivalence relation\t{'+' if is_equivalence_relation(which_relation) else '-'}")
    print(f"order relation\t\t{'+' if is_order_relation(which_relation) else '-'}")


if __name__ == "__main__":
    M = (1, 2, 3, 4)
    tau = lambda x, y: (x + y) % 2 == 0
    main(M, tau)

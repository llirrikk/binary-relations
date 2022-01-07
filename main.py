from typing import Callable, NamedTuple
from dataclasses import dataclass
import utils


class Pair(NamedTuple):
    x: int
    y: int


@dataclass
class Relation:
    is_belong_to_type: bool = True
    message: str = ""


class WhichRelation(NamedTuple):
    reflexive_relation: Relation
    symmetric_relation: Relation
    antisymmetric_relation: Relation
    transitive_relation: Relation


def is_reflexive_relation(M: tuple, taus: set) -> Relation:
    relation = Relation()
    for x in M:
        if Pair(x=x, y=x) not in taus:
            relation.is_belong_to_type = False
            relation.message = f"({x},{x}) not in taus"
            break
    return relation


def is_symmetric_relation(M: tuple, taus: set) -> Relation:
    relation = Relation()
    for x in M:
        for y in M:
            if Pair(x=x, y=y) in taus:
                if Pair(x=y, y=x) not in taus:
                    relation.is_belong_to_type = False
                    relation.message = f"({x},{y}) in taus, but ({y},{x}) not in taus"
                    break
    return relation


def is_antisymmetric_relation(M: tuple, taus: set) -> Relation:
    relation = Relation()
    for x in M:
        for y in M:
            if Pair(x=x, y=y) in taus and Pair(x=y, y=x) in taus:
                if (x == y) == False:
                    relation.is_belong_to_type = False
                    relation.message = (
                        f"({x},{y}) in taus, and ({y},{x}) in taus, but {x} != {y}"
                    )
                    break
    return relation


def is_transitive_relation(M: tuple, taus: set) -> Relation:
    relation = Relation()
    for x in M:
        for y in M:
            for z in M:
                if Pair(x=x, y=y) in taus and Pair(x=y, y=z) in taus:
                    if Pair(x=x, y=z) not in taus:
                        relation.is_belong_to_type = False
                        relation.message = f"({x},{y}) in taus, and ({y},{z}) in taus, but ({x},{z}) not in taus"
                        break
    return relation


def main(M: tuple, tau: Callable[[int, int], bool]) -> None:
    utils.new_section("M")
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

    utils.new_section("binary relations")
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


if __name__ == "__main__":
    M = (1, 2, 3, 4)
    tau = lambda x, y: (x - y) == 0 or (x - y > 0 and (x - y) % 3 == 0)
    main(M, tau)

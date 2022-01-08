from dataclasses import dataclass
from typing import NamedTuple


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


def is_equivalence_relation(wr: WhichRelation) -> bool:
    return wr.reflexive_relation.is_belong_to_type and \
           wr.symmetric_relation.is_belong_to_type and \
           wr.transitive_relation.is_belong_to_type


def is_order_relation(wr: WhichRelation) -> bool:
    return wr.reflexive_relation.is_belong_to_type and \
           wr.antisymmetric_relation.is_belong_to_type and \
           wr.transitive_relation.is_belong_to_type

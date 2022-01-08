# Checking Binary Relations by Definition

## What is Binary Relation

[Binary relation](https://en.wikipedia.org/wiki/Binary_relation) over sets X and Y is a new set of ordered pairs (x, y)
consisting of elements x in X and y in Y.

Let <img src="https://render.githubusercontent.com/render/math?math=\bbox[white]{(x, y) \in \tau \equiv x \tau y}">

Сhecking of belonging to:

- [Reflexive relation](https://en.wikipedia.org/wiki/Reflexive_relation):
  <img src="https://render.githubusercontent.com/render/math?math=\bbox[white]{\forall x \in M: x \tau x}">
- [Symmetric relation](https://en.wikipedia.org/wiki/Symmetric_relation):
  <img src="https://render.githubusercontent.com/render/math?math=\bbox[white]{\forall x, y \in M: x \tau y \Rightarrow y \tau x}">
- [Antisymmetric relation](https://en.wikipedia.org/wiki/Antisymmetric_relation):
  <img src="https://render.githubusercontent.com/render/math?math=\bbox[white]{\forall x, y \in M: x \tau y, y \tau x \Rightarrow x = y}">
- [Transitive relation](https://en.wikipedia.org/wiki/Transitive_relation):
  <img src="https://render.githubusercontent.com/render/math?math=\bbox[white]{\forall x, y, z \in M: x \tau y, y \tau z \Rightarrow x \tau z}">


- [Equivalence relation](https://en.wikipedia.org/wiki/Equivalence_relation): if Binary Relation is Reflexive, Symmetric
  and Transitive
- [Order relation](https://ru.wikipedia.org/wiki/%D0%9E%D1%82%D0%BD%D0%BE%D1%88%D0%B5%D0%BD%D0%B8%D0%B5_%D0%BF%D0%BE%D1%80%D1%8F%D0%B4%D0%BA%D0%B0):
  if Binary Relation is Reflexive, Antisymmetric and Transitive

## Example

If <img src="https://render.githubusercontent.com/render/math?math=\bbox[white]{M = \{ 1, 2, 3, 4 \}}">
and <img src="https://render.githubusercontent.com/render/math?math=\bbox[white]{x \tau y \Leftrightarrow \text{(x %2B y is even sum)}}">

```
----------M-------------------------------------------------------------------------------
(1, 2, 3, 4)

----------M * M---------------------------------------------------------------------------
(1,1)   (1,2)   (1,3)   (1,4)
(2,1)   (2,2)   (2,3)   (2,4)
(3,1)   (3,2)   (3,3)   (3,4)
(4,1)   (4,2)   (4,3)   (4,4)

----------M * M (with tau)----------------------------------------------------------------
(1,1)   -       (1,3)   -
-       (2,2)   -       (2,4)
(3,1)   -       (3,3)   -
-       (4,2)   -       (4,4)

----------properties of binary relations--------------------------------------------------
reflexive_relation      +
symmetric_relation      +
antisymmetric_relation  -       (4,2) in taus, and (2,4) in taus, but 4 != 2
transitive_relation     +

----------types of binary relations-------------------------------------------------------
equivalence relation    +
order relation          -
```
# Category Theory Basics

## Objects and Morphisms

The basic building blocks of Category Theory are objects and morphisms (also called arrows).

### Morphisms

are a relationship between Objects, it can be a mapping like a function but it doesn't have to be. A counter example is `>=` which also can be a valid Morphism (in a specific category).

Morphisms are also sometimes called arrows and are also written like a arrow `->`. This is probably where the lambda arrow comes from in languages like java and javascript.

### Objects

Serves as the ends of a Morphism and are quite uninteresting in them selves. Usually a Object serves as a container for multiple value with in a specific classification but can also be concrete and mean a specific value.

Objects are written like a circle or a dot like this `.`.

## Categories

For something to count as a Category it needs to follow some simple rules.

### Composition

If you have to Morphisms that share a common Object, one that is the endpoint of one and start of the other then there must be one (or possible to create one) that is the composition of both.

`A->B->C` there bust be one `A->C`.

### Identity

Every Object needs to have a Morphism that has it self as both the beginning and the end, `A->A`.

This Morphism should also work as a unit under composition. Which means that if you compose any Morphism (that is valid to compose with) with a Identity Morphism you should get the other one back. `A->A->B = A->B` and `A->B->B = B->B`.





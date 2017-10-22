
## Some basic Category Theory jargon

A category are described with two concepts Objects and Morphisms. Objects are writen as a dot or circle and Morphism (also called arrows) are writen as a arrow.

`O -> O`

A Morphism is one way relationship between Objects. In programming they are usually a function between types. As a example toString on a Integer would be a Morphism between Integer and String, `(Integer) -> (String)`. There is always a Morphism between a Object and it self which is called the Identity. Also there is always a Morphism (or it is possible to construct a Morphism) that is the composition between two Morphisms that share a Object in between them, like this:

```
A -g-> B
B -f-> C
A -g.f-> C
```

In java this would correspond to that if you can do toString on a number and take the length of a String then you can write a function that first takes a Number and return the length of its toString.

Well done, you now know the basics of Category Theory!
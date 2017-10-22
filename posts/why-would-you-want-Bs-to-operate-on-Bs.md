# Why would you want B to operate on Bs?

That is a valid question!

This all started with a tweet by @jbrains and his quora answer to ["Does TDD
 make sense in a functional language?"](https://www.quora.com/Does-TDD-make-sense-in-a-functional-language/answer/J-B-Rainsberger)
 and me answering "Thanks for the good read. With typed fp I also see more of the unittests implemented in types instead, like the contracts."
 
 And then a small discussion (Monologue) about the Java type system continued. At some point I was not able to keep up with the small amount of text that tweets allows and I promised a blog post, this is that blog post.

 After complaining that its impossible to define a interface that returns (and receives) something of the `this` type in its methods, but showing a workaround i got the question why i would like to do that.

 ```java
 interface A<T> {
    T add(T other);
 }
 
 class B implements A<B> {
    B add(B other) {
        return null;
    }
 }
 ```

 I answered "it is a Monoid, like List or numbers."

# What is a Monoid and why would you want one?

Monoid is one (not the one) of the simplest type of categories from category theory. It appears everywhere in our daily life as programmers.

It might be good to have a grasps of [Category Theory Basics](../wiki/category-theory-basics.md) before proceeding, don't worry it's realy not that hard.


## So what does a Monoid category look like.

Its a category that has only one Object and all arrows that exist are between it and it self. And because of the rules of a Category it also need a arrow that does noting. And composition must hold, which translates to associativity.

This is maybe why multiplication and addition feels similar (if you ever felt that). Both are monoids togeather with numbers.
# I do not know why my code do not work

This is a common feeling and a common issue both for beginners and professionals. The difference is that most professionals have learnt from there mistakes (the ones you are making right now) and are using tools and habits to help them.

In this blog post I'll try to introduce some concepts and give some quick fixes to help you with the problem at hand.

## Lesson 1: Version Control

Version control is a simple concept. It is like the super version of `ctrl + z`. If you haven't learnt [git](https://git-scm.com/) yet or any other version control tool I highly recommend it. That is however a bit too much to go through for to day.
 
So what is the _now_ option? Folders. When you are trying to fix your programming assignment (due tomorrow) or fixing performance issues in your hobby project. Copy the source folder and give it a name like `2017-10-19-21:34-working-asssignment-3-done` or `2017-10-20-23:56-broken-fiddeling-with-padding`. This will help you greatly in being able to take large (uncomfortable) steps without loosing working versions. So now you can always revert your work to a known working state and answer "when did I change this?".

One last note, save and make versions often. You will se that it also helps you think about your changes and why you do them.

## Lesson 2: Library and Program.

Now that we have our safety belt ready (git or version folders) we can start to make changes.

The first change we will make is to how we the structure of your code. There are a lot of fancy words for this technique, and it can be done with more or less precision and granularity. These techniques are commonly referred to as principals and or design patterns. As with git this is a huge subject, and I will only give you tha most basic introduction. If you would like to read more about this, look up `Law of Demeter`, `the SOLID pricipals`, and `Ports and Adapters` where the later is the pattern I'll introduce to you, though a shortened version of it.

Many of these patterns are imposed on you if you write in strict functional languages like Haskell. So learning new languages usually teach you new ways of ordering problems and code. 

The gist of `Ports and Adapters` is to separate the core logic of your program from the rest of the world. The more descriptive way of saying this is:

> put all logic in a library and leave the interactions in the program.

Lets have a example:
```python
raw_age = input("what is your age?")
age = int(raw_age)
if age > 25:
    age -= 5
else:
    age += 5
print("Oh! I thought you where", age, "old!")
```

This is one of the first programs I built around `1995`, then it was written in BASIC and not python, ah the memories.

First make sure we can import this file without running the program:

```python
if __name__ == "__main__":
    raw_age = input("what is your age?")
    age = int(raw_age)
    if age > 25:
        age -= 5
    else:
        age += 5
    print("Oh! I thought you where", age, "old!")
```

Then lets extract every thing that is pure (that does not ask the user or write anything) logic.

```python
def complimenting_age(age):
    if age > 25:
        age -= 5
    else:
        age += 5
    return age

if __name__ == "__main__":
    raw_age = input("what is your age?")
    age = int(raw_age)
    age = complimenting_age(age)
    print("Oh! I thought you where", age, "old!")
```

If this was a bigger program I would move the functions into separate files.

Some interesting things happens when you do this. We get a place to name the logic `complimenting_age`. The code in the function is easier to reason about and easier to show to others. The code in the main if statement also change into something different. It looks more like a table of contents, a list of what to be done.

## Lesson 3: Writing tests

This is probably how you currently work:

1. write some code
2. run the program
3. see if the program now do what you want
4. repeat

You probably also change other parts of the code then the code you are writing. Use comments as a way to skip parts of the program that you know works. Change values of constants so that things trigger quicker.

Why do a guess these things? Cause I have done them, and I still do sometimes.

Testing in essence is to automate these processes and make it both quicker and more reliable. To make sure that what you believe work does work, and what you believe does not work does not work.

A test is a version of your program that is testing a part or parts of your library. There are also tests that tests the whole program as is but generally this is more costly and don't give you as good feedback.

The absolute simplest way to test the example program we have would be to write a new file `tests.py` that imports the  `program.py` file with the code we rewrote in [Lesson 2](#lesson-2:-library-and-program.).

```python
# program.py
def complimenting_age(age):
    if age > 25:
        age -= 5
    else:
        age += 5
    return age

if __name__ == "__main__":
    raw_age = input("what is your age?")
    age = int(raw_age)
    age = complimenting_age(age)
    print("Oh! I thought you where", age, "old!")
#test.py
#import program

assert complimenting_age(20) == 25
assert complimenting_age(24) == 29
assert complimenting_age(25) == 20
assert complimenting_age(26) == 21

```

If you would run this file you would not need to run through the whole program to find out that the program do not handle age `25` correctly. What we wanted was that it prompts `20` but it will prompt `30`.

There are of course tools for this that make things easier, especially when you have more than one function to test. 

My favorite two tools for this is doctest and py.test. I'll show you doctest, since it is part of a normal python installation. I recommend you to look at py.test when you have the time.

### Doctest

Using doctest is super easy if you already followed [Lesson 2](#lesson-2:-library-and-program.). The only thing you have to do is add a example in the doc-string of the function you want to test

```python
def complimenting_age(age):
    """
    >>> complimenting_age(24)
    29
    >>> complimenting_age(25)
    20
    >>> complimenting_age(26)
    21
    """
    if age > 25:
        age -= 5
    else:
        age += 5
    return age
    
if __name__ == "__main__":
    raw_age = input("what is your age?")
    age = int(raw_age)
    age = complimenting_age(age)
    print("Oh! I thought you where", age, "old!")
```

And then run the doctest module on the file `python -m doctest program.py`. This would be the output:

```
File "program.py", line 5, in program.complimenting_age
Failed example:
    complimenting_age(25)
Expected:
    20
Got:
    30
**********************************************************************
1 items had failures:
   1 of   3 in program.complimenting_age
***Test Failed*** 1 failures.
```

## Lesson 4: Fix it then Refactor

So let's fix the code by changing `>` to `>=`:

```python
def complimenting_age(age):
    """
    >>> complimenting_age(24)
    29
    >>> complimenting_age(25)
    20
    >>> complimenting_age(26)
    21
    """
    if age >= 25:
        age -= 5
    else:
        age += 5
    return age
    
if __name__ == "__main__":
    raw_age = input("what is your age?")
    age = int(raw_age)
    age = complimenting_age(age)
    print("Oh! I thought you where", age, "old!")
```

Running the doctest does not give any output, so that is good! Let us add a `-v` flag to get a bit more verbose output.

```
$ python -m doctest -v program.py
Trying:
    complimenting_age(24)
Expecting:
    29
ok
Trying:
    complimenting_age(25)
Expecting:
    20
ok
Trying:
    complimenting_age(26)
Expecting:
    21
ok
1 items had no tests:
    program
1 items passed all tests:
   3 tests in program.complimenting_age
3 tests in 2 items.
3 passed and 0 failed.
Test passed.
```

Seams like everything works so let's save it (using git or folders). Now we can clean up the mess we made.

let us add a blank line between the function and the if statement, this is mandatory according to [pep8](https://www.python.org/dev/peps/pep-0008/)

```python
def complimenting_age(age):
    """
    >>> complimenting_age(24)
    29
    >>> complimenting_age(25)
    20
    >>> complimenting_age(26)
    21
    """
    if age >= 25:
        age -= 5
    else:
        age += 5
    return age


if __name__ == "__main__":
    raw_age = input("what is your age?")
    age = int(raw_age)
    age = complimenting_age(age)
    print("Oh! I thought you where", age, "old!")
```

Run the test and make sure they pass. For a small change like this we would not have bothered to start the application and test all the ages. But now that testing is almost free we can do it all the time.

### Refactor

let us remove mutation. In programming state is your enemy, if you can do something without mutating or share state then its almost always better.
```python
def complimenting_age(age):
    """
    >>> complimenting_age(24)
    29
    >>> complimenting_age(25)
    20
    >>> complimenting_age(26)
    21
    """
    if age >= 25:
        return age - 5
    else:
        return age + 5


if __name__ == "__main__":
    raw_age = input("what is your age?")
    int_age = int(raw_age)
    new_age = complimenting_age(int_age)
    print("Oh! I thought you where", new_age, "old!")
```

I'm quite happy with that.

## If you liked this

You can find me on twitter [@neppord](https://twitter.com/neppord) and [youtube](https://www.youtube.com/channel/UCgWtfN4QMkZq_zizqQh9dfw).

Please say hi! and tell me if this was useful / entertaining. I have some other lessons on the subject that did not fit into this blog post about type hints and debugging. Let me know if it sounds interesting.

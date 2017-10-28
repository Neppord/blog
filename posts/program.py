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
    print("Oh! i thought you where", new_age, "old!")

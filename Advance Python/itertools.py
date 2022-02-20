import itertools

def testFunction(x):

    """
    testFunction(x) --> Doesn't really do anything, just checks 
    if x is smaller than 40 or not

    Parameters:
    x: A number
    """
    return x < 40


def main():
    # TODO: cycle iterator can be used to cycle over a collection
    seq1 = ["Joe", "John", "Mike"]
    # cycle1 = itertools.cycle(seq1)
    # print(next(cycle1))
    # print(next(cycle1))
    # print(next(cycle1))
    # print(next(cycle1))

    # TODO: use count to create a simple counter
    count1 = itertools.count(100, 10)
    # print(next(count1))
    # print(next(count1))
    # print(next(count1))
    # print(next(count1))

    # TODO: accumulate create an iterator that accumulates values
    vals = [10, 20, 30, -40, 50, 40, 30, 0, 333]
    # acc = itertools.accumulate(vals)
    # acc = itertools.accumulate(vals, min)
    # print(list(acc))

    # TODO: use chain to connect sequences together
    # x = itertools.chain("ABCD", "1234")
    # print(list(x))

    # TODO: dropwhile and takewhile will return values untill
    # a certain condition is met that stops them
    print(list(itertools.dropwhile(testFunction, vals)))
    print(list(itertools.takewhile(testFunction, vals)))
    print(testFunction.__doc__)
if __name__ == "__main__":
    main()
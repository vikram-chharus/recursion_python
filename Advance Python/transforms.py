def filterFunc(x):
    if x % 2 == 0:
        return False
    else:
        return True
    
def filterLower(x):
    if x.islower():
        return True
    else:
        return False


def toGrade(x):
    if (x >= 90):
        return 'A'
    elif (x >= 80 and x < 90):
        return 'B'
    elif (x >=70 and x < 80):
        return 'C'
    elif (x >=65 and x < 70):
        return 'D'
    return 'F'


def squareFunc(x):
    return x** 2

def main():
    nums = (1, 8, 4, 5, 13, 26, 381, 410, 47)
    chars = "abcDeFGHijklmnop"
    grades = (81, 89, 94, 78, 61, 66, 99, 74)

    # TODO: use filter to remove items from a list
    # odds = list(filter(filterFunc, nums))
    # print(odds)

    # TODO: user filter on non-numeric sequence
    # lower = list(filter(filterLower, chars))
    # print(lower)

    # TODO: use map to create a new sequence of values
    # squares = list(map(squareFunc, nums))
    # print(squares)

    # TODO: use sorted and map to change the numbers to grades
    grades = sorted(grades)
    letters = list(map(toGrade, grades))
    print(letters)

if __name__ == "__main__":
    main() 
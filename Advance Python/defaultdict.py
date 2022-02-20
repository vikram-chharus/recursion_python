from collections import defaultdict, namedtuple

def main():
    fruits = ["apple", "banana", "apple", "orange", "tomato", 
    "grapes", "tomato", "banana"]
    fruitCounter = defaultdict(int)
    Fruit = namedtuple("Fruit", "key value")
    for i in fruits:
        fruitCounter[i]+=1
    
    # for (k,v) in fruitCounter.items():
    #     q = Fruit(k,v)
    #     print(q.key+" : "+str(q.value))

    # i = iter(fruitCounter)

    # print(next(i, None))
    # print(next(i, None))
    # print(next(i, None))
    # print(next(i, None))
    # print(next(i, None))
    for K, V in zip(fruitCounter, [ fruitCounter[a] for a in fruitCounter.keys()] ):
        print(K, V)


if __name__ == "__main__":
    main()
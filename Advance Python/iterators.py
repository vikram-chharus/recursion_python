def main():
    days = ["SUN", "TUE","MON", "WED", "THU", "FRI", "SAT"]   
    # i = iter(days)
    # for i in iter(days):
    #     print(i)
    
    # for i,m in enumerate(days, start=1):
    #     print(i,m)

    # for m in zip(days, range(7)):
    #     print(m)

    for i, m in enumerate(zip(days, range(7)), start=1):
        print(i, m[0]," = ", m[1], " range value")

if __name__ == "__main__":
    main()

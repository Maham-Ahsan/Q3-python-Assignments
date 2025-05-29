class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def show_count(cLs):
        print(f"Total Object Created: {cLs.count}")

c1 = Counter()
c2 = Counter()
c3 = Counter()
Counter.show_count()
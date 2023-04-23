class Foo:
    def __init__(self):
        self.s = 1


    def first(self, printFirst: 'Callable[[], None]') -> None:
        while self.s!=1:
            continue
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.s+=1


    def second(self, printSecond: 'Callable[[], None]') -> None:
        while self.s!=2:
            continue
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.s+=1


    def third(self, printThird: 'Callable[[], None]') -> None:
        while self.s!=3:
            continue
        # printThird() outputs "third". Do not change or remove this line.
        printThird()

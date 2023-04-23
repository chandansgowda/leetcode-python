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

        
        
from threading import Barrier

class Foo:
    def __init__(self):
        self.first_barrier = Barrier(2)
        self.second_barrier = Barrier(2)


    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.first_barrier.wait()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.first_barrier.wait()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.second_barrier.wait()


    def third(self, printThird: 'Callable[[], None]') -> None:
        self.second_barrier.wait()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()

from threading import Lock


class FooBar:
    def __init__(self, n):
        self.n = n
        self.fl = Lock()
        self.bl = Lock()
        self.bl.acquire()


    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.fl.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.bl.release()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.bl.acquire()
            # printBar() outputs "bar". Do not change or remove this line.      
            printBar()
            self.fl.release()

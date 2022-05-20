from defer import (
    defers_collector,
    defer,
    panic,
    recover
)


@defers_collector
def func():
    f = open('file.txt', 'w')
    
    defer(lambda: f.close())

    defer(lambda : print("Defer called!"))

    def my_defer():
        recover()

    defer(lambda: my_defer())

    print("Ok )")
    panic("WTF?")

    print("Never printed (((")



if __name__ == "__main__":
    func()
    print("Recovered!")


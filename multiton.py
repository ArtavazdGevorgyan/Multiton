class Multiton:
    _counter = 0
    _instances = [None, None, None]

    def __new__(cls):
        if not cls._instances[cls._counter % 3]:
            cls._instances[cls._counter % 3] = super().__new__(cls)
        cls._counter += 1
        return cls._instances[(cls._counter - 1) % 3]


for i in range(10):
    print(i, Multiton())
class Singleton:
    indicator = None

    def __new__(cls):
        if cls.indicator == None:
            cls.indicator = super().__new__(cls)
        return cls.indicator


a = Singleton()
b = Singleton()
print(a is b)
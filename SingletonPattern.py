class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

singleton = Singleton()
new_singelton = Singleton()

singleton is new_singelton #True
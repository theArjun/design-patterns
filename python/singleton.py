''' Implement singleton design pattern '''


class Singleton:
    ''' Singleton class that allows to create a single object. '''

    # Create private property of class.
    __instance = None

    def __init__(self):
        ''' Virtually private constructor. '''
        if Singleton.__instance is not None:
            # Check if the instance is None i.e. check some object
            # has already been instantiated or not, changing __instance
            # to self from None.
            raise Exception('This class is a Singleton.')
        else:
            Singleton.__instance = self

    @staticmethod
    def get_instance():
        ''' Static access method. '''
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance


if __name__ == '__main__':
    # We're just creating an object. Doesn't matter we
    # first call the get_instance method or directly
    # instantiate the object, we're getting same object
    # eveytime.
    obj1 = Singleton()
    print(obj1)

    # Everytime we call the static get_instance method,
    # We get the same result.
    obj2 = Singleton.get_instance()
    print(obj2)

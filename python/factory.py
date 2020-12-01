''' Implement factory design pattern. '''
from abc import (
    ABC,
    abstractmethod,
)


class OS(ABC):
    ''' Abstract class OS. '''
    @abstractmethod
    def spec(self):
        pass


class Android(OS):
    ''' Android class that implement abstract class OS. '''

    def spec(self):
        print('Most Powerful OS')


class IOS(OS):
    ''' IOS class that implement abstract class OS. '''

    def spec(self):
        print('Most Secure OS')


class Windows(OS):
    ''' Windows class that implement abstract class OS. '''

    def spec(self):
        print('Desktop OS')


class OSFactory():
    ''' Factory class to create object of various OS types. '''

    @classmethod
    def get_instance(cls, os_type):
        ''' Return the instance of various OS types. '''
        if os_type == 'android':
            return Android()
        elif os_type == 'ios':
            return IOS()
        elif os_type == 'windows':
            return Windows()
        else:
            return None


if __name__ == '__main__':
    # Driver Code
    os_type = input('Enter OS type : ').strip()
    obj = OSFactory.get_instance(os_type)
    if obj:
        obj.spec()
    else:
        print('Can\'t create object of given type.')

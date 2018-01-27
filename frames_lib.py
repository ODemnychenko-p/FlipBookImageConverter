class Singleton(type):

    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

class Frames(metaclass=Singleton):
    def __init__(self):
        self._all = []
        self._framesCountX = 1
        self._framesCountY = 1
        self._frameSizeX = 0
        self._frameSizeY = 0

    @property
    def frameSizeX(self):
        return self._frameSizeX

    @frameSizeX.setter
    def frameSizeX(self, value):
        self._frameSizeX = value

    @property
    def frameSizeY(self):
        return self._frameSizeY

    @frameSizeY.setter
    def frameSizeY(self, value):
        self._frameSizeY = value

    @property
    def framesList(self):
        """Get all created frames"""
        return self._all

    @framesList.setter
    def framesList(self, value):
        """Add frames into a list"""
        self._all.append(value)
        print("Frame({0}): {1} was added!".format(len(self._all), value))

    @framesList.deleter
    def framesList(self):
        """Clear list of frames"""
        self._all.clear()
        print("Frames is deleted!")

    @property
    def framesCountX(self):
        """Get horizontal frame count"""
        return self._framesCountX

    @framesCountX.setter
    def framesCountX(self, value):
        """Set horizontal frame count"""
        self._framesCountX = abs(self._int(value))
        print("Frames count X: {0}".format(self._framesCountX))

    @property
    def framesCountY(self):
        """Get vertical frame count"""
        return self._framesCountY

    @framesCountY.setter
    def framesCountY(self, value):
        """Set vertical frame count"""
        self._framesCountY =  abs(self._int(value))
        print("Frames count Y: {0}".format(self._framesCountY))

    def _int(self, value):
        """Check, if number consist of a letter return 0, else return value"""
        try:
            return int(value)
        except ValueError:
            print("The number must not be consist of a letter!")
            return 0


class Frames:
    def __init__(self):
        self._all = []
        self._count = [1, 1]
        self._width, self._height = 1, 1
        self.outMosaic = None

    def __del__(self):
        self._all.clear()

    def __len__(self):
        """Get frames length"""
        return len(self._all)

    def __getitem__(self, key):
        """Get a frame by index"""
        if isinstance(key, int):
            return self._all[key]
        raise TypeError('Cannot get key {0}'.format(key))

    @property
    def frameSize(self):
        return self._width, self._height

    @frameSize.setter
    def frameSize(self, value):
        self._width, self._height = map(lambda x: x[1] / x[0], zip(self._count, value))

    @property
    def framesList(self):
        """Get all created frames"""
        return self._all

    @framesList.setter
    def framesList(self, value):
        """Add frames into a list"""
        self._all.append(value)
        print("Frame({0}): {1} was added!".format(len(self._all), value))

    @property
    def framesCount(self):
        """Get frames count, vertical and horizontal"""
        return self._count

    @framesCount.setter
    def framesCount(self, value):
        self._count = value

    @property
    def outMosaic(self):
        return self._out_mosaic

    @outMosaic.setter
    def outMosaic(self, val):
        self._out_mosaic = val


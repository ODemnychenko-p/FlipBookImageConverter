from PIL import Image
import os

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
        self._frameSizeX = 1
        self._frameSizeY = 1

    @property
    def frameSizeX(self):
        return self._frameSizeX

    @frameSizeX.setter
    def frameSizeX(self, value):
        # self._frameSizeX = round(value / self.framesCountX)
        self._frameSizeX = value / self.framesCountX
        print(self._frameSizeX)

    @property
    def frameSizeY(self):
        return self._frameSizeY

    @frameSizeY.setter
    def frameSizeY(self, value):
        # self._frameSizeY = round(value / self.framesCountY)
        self._frameSizeY = value / self.framesCountY
        print(self._frameSizeY)

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

class FlipbookConverter(metaclass=Singleton):
    def __init__(self):
        self._frames = Frames()
        self.sourceImg = None
        self.imgName = ""
        self.imgMode = ""
        self.imgFormat = ""
        self.imgSizePX = []
        self.imgSizeMb = ""

    def save(self, r1, r2, path, ext):
        if self._frames.framesList:
            for i in range(r1-1, r2):
                img = self._frames.framesList[i]
                img.save("{0}/frame_{1}.{2}".format(path, i+1, ext))
                print("frame_{0} was saved".format(i+1))

    def saveAll(self, path, ext):
        if self._frames.framesList:
            for i in range(0, len(self._frames.framesList)):
                img = self._frames.framesList[i]
                img.save("{0}/frame_{1}.{2}".format(path, i+1, ext))
                print("frame_{0} was saved".format(i+1))

    def getImage(self, path):
        try:
            self.sourceImg = Image.open(path)
        except FileNotFoundError:
            return False
        else:
            self.imgName, self.imgFormat = os.path.splitext(os.path.basename(self.sourceImg.filename))
            self.imgMode = self.sourceImg.mode
            self.imgSizePX = self.sourceImg.width, self.sourceImg.height
            self.imgSizeMb = "{0}".format(os.path.getsize(path) / 1000)
            return True

    def getImgData(self, img = 0):

        if not img:
            img = self.sourceImg
        if max(img.size) >= 512:
            k = max(img.size) / 512
            w = int(img.width / k)
            h = int(img.height / k)
            img = img.resize((w, h), Image.ANTIALIAS)
        if img.mode == "RGB":
            r, g, b = img.split()
            img = Image.merge("RGB", (b, g, r))
        elif img.mode == "RGBA":
            r, g, b, a = img.split()
            img = Image.merge("RGBA", (b, g, r, a))
        elif img.mode == "L":
            img = img.convert("RGBA")

        img = img.convert("RGBA")
        return img.tobytes("raw", "RGBA"), img.size

    def imageSizeCompensation(self):
        kx = 1 - (self.imgSizePX[0] / self._frames.framesCountX)%1
        print("kx: {0}".format(kx))
        ky = 1 - (self.imgSizePX[1] / self._frames.framesCountY)%1
        print("ky: {0}".format(ky))
        k = kx * self._frames.framesCountX, ky * self._frames.framesCountY
        print("k: {0}".format(k))
        new_size = int(k[0] + self.imgSizePX[0]), int(k[1] + self.imgSizePX[1])
        self.sourceImg = self.sourceImg.resize(new_size, Image.ANTIALIAS)
        print("New source image size: {0}".format(str(self.sourceImg.size)))
        return self.sourceImg.size

    def reverseConvertSubUV(self):
        left = 0
        top = 0
        right = self._frames.frameSizeX
        bottom = self._frames.frameSizeY
        print("right = {0}\n bottom = {1}".format(type(right), type(bottom)))
        for j in range(1, self._frames.framesCountY + 1):
            if j >= 2:
                top = bottom
                bottom = self._frames.frameSizeY * j
            for i in range(1, self._frames.framesCountX+ 1):
                if i >= 2:
                    left = right
                    right = self._frames.frameSizeX * i
                self._frames.framesList = self.sourceImg.crop((left, top, right, bottom))
            left = 0
            right = self._frames.frameSizeX

    # def convertInToSubUV(self):
    #     frame_index_w = 0
    #     frame_index_h = 0
    #     background_size = int(self._frames.framesCountX * self._frames.frameSizeX), int(self._frames.framesCountY * self._frames.frameSizeY)
    #     print(background_size)
    #     background_img = Image.new('RGB', background_size, (0, 0, 0, 0))
    #     for obj in self._frames.framesList:
    #         background_img.paste(obj, (int(frame_index_w * self._frames.frameSizeX), int(frame_index_h * self._frames.frameSizeY)))
    #         frame_index_w += 1
    #         if frame_index_w == self._frames.framesCountX:
    #             frame_index_h += 1
    #             frame_index_w = 0
    #     background_img.save("{0}/{1}".format("./test", "test.tga"))

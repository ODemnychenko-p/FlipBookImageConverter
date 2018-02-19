from PIL import Image, ImageDraw, ImageFont
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
        self._frames_count = 1, 1
        self._frames_size = 1, 1

    def __len__(self):
        """Get frames length"""
        return len(self._all)

    def __getitem__(self, key):
        """Get a frame by index"""
        if isinstance(key, int):
            return self._all[key]
        raise TypeError('Cannot get key {0}'.format(key))

    def __del__(self):
        """Clear frames list"""
        self._all.clear()
        print("Frames is deleted!")

    @property
    def frameSize(self):
        return self._frames_size

    @frameSize.setter
    def frameSize(self, value):
        self._frames_size = value[0] / self._frames_count[0], value[1] / self._frames_count[1],
        print("Frame size is : {0}".format(self._frames_size))

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
        return self._frames_count

    @framesCount.setter
    def framesCount(self, value):
        """Set vframes count, vertical and horizontal"""
        self._frames_count = value
        print("Frames count X, Y {0}".format(self._frames_count))

class FlipbookConverter(metaclass=Singleton):
    def __init__(self):
        self._frames = Frames()
        self.source_image = None
        # self.label_image_info = Image.new('RGBA', (512, 512), (255, 255, 255, 0))
        # self.label_background = Image.new('RGBA', (512, 512), (30, 30, 30, 0))
        self.image_path = ""
        self.image_name = ""
        self.image_mode = ""
        self.image_format = ""
        self.image_size_px = []
        self.image_size_mb = ""

    def render(self, args, cur_id=0, path="", ext="TGA", filename="frame"):
        if args:
            start, end, inc = args
            if start <= end:
                for i in range(start-1, end, inc):
                    self._frames[i].save("{0}/{1}_{2}.{3}".format(path, filename, i, ext))
                    print("{0}_{1} was saved".format(filename, i))
            else:
                print("Frame range is incorrect!")
        else:
            if cur_id:
                self._frames[cur_id-1].save("{0}/{1}_{2}.{3}".format(path, filename, cur_id-1, ext))
                print("{0}_{1} was saved".format(filename, cur_id-1))
            else:
                print("Frame is not selected!")

    def get_image(self, path):
        try:
            self.source_image = Image.open(path)
        except FileNotFoundError:
            return False
        else:
            self.image_name, self.image_format = os.path.splitext(os.path.basename(self.source_image.filename))
            self.image_mode = self.source_image.mode
            self.image_size_px = self.source_image.size
            self.image_size_mb = "{0}".format(os.path.getsize(path) / 1000)
            self.image_path = os.path.dirname(self.source_image.filename)
            return True

    # def create_label_info(self):
    #     pad = 15
    #     txt = "Info:\n" \
    #           "Path: {0}\n" \
    #           "Name: {1}\n" \
    #           "Format: {2}\n" \
    #           "Mode: {3}\n" \
    #           "Size(px): {4}\n" \
    #           "Size(Mb): {5}".format(self.image_path,
    #                                  self.image_name,
    #                                  self.image_format,
    #                                  self.image_mode,
    #                                  self.image_size_px,
    #                                  self.image_size_mb)
    #     draw = ImageDraw.Draw(self.label_image_info)
    #     width, height = draw.textsize(txt)
    #     draw.rectangle(((10, 10), width + pad, height + pad), fill=(50, 50, 50, 50))
    #     draw.text((15, 15), txt, font=ImageFont.load_default(), fill=(0, 0, 0, 255))

    def get_image_data(self, img=0):

        if not img:
            img = self.source_image
        if max(img.size) >= 512:
            k = max(img.size) / 512
            w = int(img.width / k)
            h = int(img.height / k)
            img = img.resize((w, h), Image.ANTIALIAS)

        # offset = (round((512 - img.width) / 2), round((512 - img.height) / 2))
        # self.label_background.paste(img, offset)
        # self.create_label_info()
        # img = Image.alpha_composite(self.label_background, self.label_image_info )

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

    def image_size_compensation(self):

        width, height = map(
            lambda x: int(((1 - (x[0]/x[1] % 1)) * x[1]) + x[0]),
            zip(self.image_size_px, self._frames.framesCount)
        )
        self.source_image = self.source_image.resize((width, height), Image.ANTIALIAS)
        print("New source image size: {0} X {1}".format(width, height))
        return width, height

    def reverse_convert(self):
        left = 0
        top = 0
        right, bottom = self._frames.frameSize
        for j in range(1, self._frames.framesCount[1] + 1):
            if j >= 2:
                top = bottom
                bottom = self._frames.frameSize[1] * j
            for i in range(1, self._frames.framesCount[0] + 1):
                if i >= 2:
                    left = right
                    right = self._frames.frameSize[0] * i
                self._frames.framesList = self.source_image.crop((left, top, right, bottom))
            left = 0
            right = self._frames.frameSize[0]

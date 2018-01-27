from PIL import Image
from frames_lib import Frames

class FlipbookConverter:
    def __init__(self):
        self._frames = Frames()

    def reverseConvertSubUV(self, frameSize, framesCountX, framesCountY, img):
        left = 0
        top = 0
        right = frameSize[0]
        bottom = frameSize[1]
        for j in range(1, framesCountY + 1):
            if j >= 2:
                top = bottom
                bottom = frameSize[1] * j
            for i in range(1, framesCountX + 1):
                if i >= 2:
                    left = right
                    right = frameSize[0] * i
                self._frames.framesList = img.crop((left, top, right, bottom))
            left = 0
            right = frameSize[0]

    def convertInToSubUV(self):
        frame_index_w = 0
        frame_index_h = 0
        background_size = int(self._frames.framesCountX * self._frames.frameSizeX), int(self._frames.framesCountY * self._frames.frameSizeY)
        print(background_size)
        background_img = Image.new('RGB', background_size, (0, 0, 0, 0))
        for obj in self._frames.framesList:
            background_img.paste(obj, (int(frame_index_w * self._frames.frameSizeX), int(frame_index_h * self._frames.frameSizeY)))
            frame_index_w += 1
            if frame_index_w == self._frames.framesCountX:
                frame_index_h += 1
                frame_index_w = 0
        background_img.save("{0}/{1}".format("./test", "test.tga"))


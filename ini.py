import os
import math
from PIL import Image

# image = Image.open("test.jpg")
# imageWidth, imageHeight = image.size
# horizontLine = 8
# verticalLine = 4
# frameSizeWidth = imageWidth/horizontLine
# frameSizeHeight = imageHeight/verticalLine
#
# left = 0
# top = 0
# frameIndex = 0
# right = frameSizeWidth
# bottom = frameSizeHeight
#
# for j in range(1, verticalLine + 1):
#     if j >= 2:
#         top = bottom
#         bottom = frameSizeHeight * j
#     for i in range(1, horizontLine + 1):
#         frameIndex += 1
#         if i >= 2:
#             left = right
#             right = frameSizeWidth * i
#         cropImage = image.crop((left, top, right, bottom))
#         cropImage.save("test{0}{1}.jpg".format(j, i))
#     left = 0
#     right = frameSizeWidth
# print("Frame Index: {0}".format(frameIndex))
# cropImage.show()
class SubUVImage:
    def __init__(self, horizontal = 0, vertical = 0, image_path = "", temp_path = "", out_directory = ""):
        self._horizontal = horizontal
        self._vertical = vertical
        self._image = self._getImage(image_path)
        self._temp_path = temp_path
        self._out_directory = out_directory
        self._frameSize = self._getframeSize(self._image.size)
        self._texture_name = os.path.basename(text_path)
    def _getImage(self, image_path):
        try:
            return Image.open(image_path)
        except FileNotFoundError as error:
            print(error)
        except FileExistsError as error:
            print(error)

    def _getframeSize(self, img_size):
        try:
            return img_size[0]/self._horizontal, img_size[1]/self._vertical
        except ZeroDivisionError as error:
            print(error)

    def _getFrameList(self):
        frame_list = os.listdir(self._temp_path)
        return frame_list.remove(".DS_Store") if ".DS_Store" in frame_list else frame_list

    def _sortByNum(self, imgName = ""):
        baseName = imgName.partition(".")
        alpha, num = baseName[0].split("_")
        return int(num)

    def convertInToSubUV(self):
        frame_index_w = 0
        frame_index_h = 0
        frame_list = sorted(self._getFrameList(), key=self._sortByNum)
        frame_count = len(frame_list)
        frames_per_line = math.floor(math.sqrt(frame_count))
        frame_img = self._getImage("{0}/{1}".format(self._temp_path, frame_list[0]))
        frame_img_size = frame_img.size
        background_img_size = frames_per_line * frame_img_size[0], math.ceil(frame_count/frames_per_line) * frame_img_size[1]
        background_img = Image.new('RGB', background_img_size, (0, 0, 0, 0))
        for frame_name in frame_list:
            frame_img = self._getImage("{0}/{1}".format(self._temp_path, frame_name))
            background_img.paste(frame_img, (frame_index_w * frame_img_size[0], frame_index_h * frame_img_size[1]))
            frame_index_w += 1
            if frame_index_w == frames_per_line:
                frame_index_h += 1
                frame_index_w = 0
        background_img.save("{0}/{1}".format(self._out_directory, self._texture_name))

    def reverseConvertSubUV(self):
        counter = 1
        left = 0
        top = 0
        right = self._frameSize[0]
        bottom = self._frameSize[1]
        for j in range(1, self._vertical + 1):
            if j >= 2:
                top = bottom
                bottom = self._frameSize[1] * j
            for i in range(1, self._horizontal + 1):
                if i >= 2:
                    left = right
                    right = self._frameSize[0] * i
                if counter % 2 != 0:
                    cropImage = self._image.crop((left, top, right, bottom))
                    cropImage.save("{0}/temp_{1}.tga".format(self._temp_path, counter))
                counter += 1
            left = 0
            right = self._frameSize[0]

text_path = r"D:\Demnichenko\Tasks\LiS\Texture Optimize\TX_GermanExpressionistMovie_10x14_A.TGA"
out_path = r"D:\Demnichenko\Tasks\LiS\Texture Optimize\out"
temp_path = r"D:\Demnichenko\Tasks\LiS\Texture Optimize\temp"
horizontal_count = 10
vertical_count = 14
test = SubUVImage(horizontal= horizontal_count,
                  vertical= vertical_count,
                  image_path = text_path,
                  temp_path = temp_path,
                  out_directory = out_path)
test.reverseConvertSubUV()
test.convertInToSubUV()
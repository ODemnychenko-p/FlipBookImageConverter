import sys
import os
from PIL import Image, ImageDraw, ImageFont
from PyQt5.QtWidgets import*
from PyQt5.QtGui import*
from PyQt5.QtCore import *

from frame import Frames

if os.name == 'posix':
    from UI import flipbook_UI_IOS as UI
elif os.name == 'nt':
    from UI import flipbook_UI_WINDOWS_ver2 as UI

class Flipbook(UI.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(Flipbook, self).__init__()
        self.setupUi(self)

        self.img = None
        self.frames = None

        self.tabWidget.setCurrentWidget(self.tab)

        self.btn_image_path.clicked.connect(lambda: self.click_btn_image_path())
        self.btn_frames_path.clicked.connect(lambda: self.click_btn_frames_path())
        self.btn_out_path.clicked.connect(lambda: self.click_btn_outpath())
        self.btn_save.clicked.connect(lambda: self.click_btn_render())

        self.sb_vertical_line.valueChanged.connect(lambda: self.changed_sb_frames_count())
        self.sb_horizontal_line.valueChanged.connect(lambda: self.changed_sb_frames_count())
        self.sl_frame.valueChanged.connect(lambda: self.changed_sl_frame())
        self.cb_valid_frame_range.currentIndexChanged.connect(lambda: self.valid_frame_range_changed())


    def valid_frame_range_changed(self):
        bool_ = True if self.cb_valid_frame_range.currentIndex() == 1 else 0
        self.sb_start_value.setEnabled(bool_)
        self.sb_end_value.setEnabled(bool_)
        self.sb_inc_value.setEnabled(bool_)

    def click_btn_frames_path(self):
        pass

    def click_btn_outpath(self):
        path = QFileDialog.getExistingDirectory(self, "Out Directory", "")
        if path:
            self.fld_out_path.setText(path)
        else:
            self.statusbar.showMessage("Output directory is not selected!", 5000)

    def click_btn_render(self):
        if self.fld_out_path.text():
            self.render()
        else:
            self.statusbar.showMessage("Please, select the output directory!")

    def click_btn_image_path(self):
        path, ext = QFileDialog.getOpenFileName(self, "Select Image", "", 'Images(*.png *.jpg *.jpeg *.tga *.psd)')
        if path:
            self.fld_image_path.setText(path)
            try:
                self.img = Image.open(path)
            except FileNotFoundError:
                self.statusbar.showMessage("Image is not found!", 5000)
                return False
            else:
                self.l_t_path.setText(os.path.dirname(self.img.filename))
                self.l_t_name.setText(os.path.basename(self.img.filename))
                self.l_t_format.setText(self.img.format)
                self.l_t_mode.setText(self.img.mode)
                self.l_t_size_px.setText(str(self.img.size))
                self.l_t_size_mb.setText(str(os.path.getsize(path) / 1000))

                self.sb_horizontal_line.setValue(1)
                self.sb_vertical_line.setValue(1)
                self.l_t_current_frame_id.setText("0")
                self.changed_sb_frames_count()
        else:
            self.statusbar.showMessage("Image is not selected! Please, select an image!", 5000)

    def changed_sl_frame(self):
        self.update_preview(self.frames[self.sl_frame.value()])

    def changed_sb_frames_count(self):

        if self.img:
            self.size_compensation()
            self.frames = Frames(
                (self.sb_vertical_line.value(), self.sb_horizontal_line.value()),
                self.img
            )
            self.divide_image(self.frames,
                              self.img
                              )
            self.sl_frame.setMaximum(len(self.frames) - 1)
            self.l_t_total_frames_count.setText(str(len(self.frames)))
            self.l_t_frame_size_px.setText(str(self.frames[self.sl_frame.value()].size))
            self.sb_start_value.setMaximum(len(self.frames)-1)
            self.sb_end_value.setMaximum(len(self.frames)-1)
            self.update_preview(self.frames[self.sl_frame.value()])
        else:
            self.statusbar.showMessage("Image is not selected! Please, select an image!", 5000)

    def size_compensation(self):

        w, h = map(lambda x: int(((1 - (x[0]/x[1] % 1)) * x[1]) + x[0]) if x[0]/x[1] % 1 != 0 else x[0],
                   zip(self.img.size, (self.sb_vertical_line.value(), self.sb_horizontal_line.value())))
        self.img = self.img.resize((w, h), Image.ANTIALIAS)

    def divide_image(self, fr, img):

        left = 0
        top = 0
        right, bottom = fr.frameSize
        for j in range(1, fr.framesCount[1] + 1):
            if j >= 2:
                top = bottom
                bottom = fr.frameSize[1] * j
            for i in range(1, fr.framesCount[0] + 1):
                if i >= 2:
                    left = right
                    right = fr.frameSize[0] * i
                fr.framesList = img.crop((left, top, right, bottom))
            left = 0
            right = fr.frameSize[0]

    def update_preview(self, img):

        txt = "Total frames count: {0}\n" \
              "Current frame ID: {1}\n" \
              "Frame size(px): {2}".format(self.l_t_total_frames_count.text(),
                                           self.l_t_current_frame_id.text(),
                                           self.l_t_frame_size_px.text()
                                           )
        background = Image.new('RGBA', (512, 512), (255, 255, 255, 0))
        info = Image.new('RGBA', (512, 512), (255, 255, 255, 0))
        img = img.resize(([x for x in map(lambda x: int(x / (max(img.size) / 512)), img.size)]), Image.ANTIALIAS)
        background.paste(img, [x for x in map(lambda x: round((x[0] - x[1]) / 2), zip(background.size, img.size))])
        draw = ImageDraw.Draw(info)
        txt_size = draw.textsize(txt)
        draw.rectangle(((5, 5), txt_size[0] + 17, txt_size[1] + 17), fill=(50, 50, 50, 100))
        draw.text((12, 12), txt, font=ImageFont.load_default(), fill=(244, 168, 6, 255))
        img = Image.alpha_composite(background, info)

        if img.mode == "RGB":
            r, g, b = img.split()
            img = Image.merge("RGB", (b, g, r))
        elif img.mode == "RGBA":
            r, g, b, a = img.split()
            img = Image.merge("RGBA", (b, g, r, a))
        elif img.mode == "L":
            img = img.convert("RGBA")
        img = img.convert("RGBA")

        data = img.tobytes("raw", "RGBA")
        qim = QImage(data, img.width, img.height, QImage.Format_ARGB32)
        pix = QPixmap.fromImage(qim)
        self.l_preview_image.setPixmap(pix)

    def render(self):
        filename = self.fld_filename.text() if self.fld_filename.text() else "frame"
        if self.sb_start_value.isEnabled():
            if self.sb_start_value.value() <= self.sb_end_value.value():
                for i in range(self.sb_start_value.value(), self.sb_end_value.value()+1, self.sb_inc_value.value()+1):
                    self.frames[i].save("{0}/{1}_{2}.{3}".format(
                        self.fld_out_path.text(),
                        filename,
                        i,
                        self.cb_image_format.currentText()
                    ))
                    print("{0}_{1} was saved".format(filename, i))
            else:
                self.statusbar.showMessage("Frame range is incorrect!", 5000)
        else:
            self.frames[self.sl_frame.value()].save("{0}/{1}_{2}.{3}".format(
                self.fld_out_path.text(),
                filename,
                self.sl_frame.value(),
                self.cb_image_format.currentText()
            ))
            print("{0}_{1} was saved".format(filename, self.sl_frame.value()))

if __name__ == "__main__":
    qapp = QApplication(sys.argv)
    flipbook = Flipbook()
    flipbook.show()
    qapp.exec_()
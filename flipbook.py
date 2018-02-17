import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from lib import Frames, FlipbookConverter

if os.name == 'posix':
    from UI import flipbook_UI_IOS as UI
elif os.name == 'nt':
    from UI import flipbook_UI_WINDOWS as UI

class Flipbook(UI.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(Flipbook, self).__init__()
        self.setupUi(self)
        self.setFocus()
        self.comboBox.addItems(("TGA", "PNG", "JPG", "JPEG"))
        self.frames = Frames()
        self.flipbook = FlipbookConverter()
        self.sl_frame.setMaximum(0)
        self.sb_range_vertical.setMaximum(1)
        self.sb_range_horizontal.setMaximum(1)
        self.btn_path.clicked.connect(lambda: self.click_btn_path())
        self.btn_out_path.clicked.connect(lambda: self.click_btn_outpath())
        self.sb_vertical_line.valueChanged.connect(lambda: self.changed_sb_frames_count())
        self.sb_horizontal_line.valueChanged.connect(lambda: self.changed_sb_frames_count())
        self.sl_frame.valueChanged.connect(lambda: self.changed_sl_frame())
        self.btn_save.clicked.connect(lambda: self.click_btn_save())
        self.btn_saveall.clicked.connect(lambda: self.click_btn_saveall())

    def click_btn_outpath(self):
        path = QFileDialog.getExistingDirectory(self, "Out Directory", "")
        if path:
            self.fld_out_path.setText(path)
        else:
            print("Output directory is not selected!")

    def click_btn_save(self):
        if self.fld_out_path.text():
            self.flipbook.save(
                self.sb_range_horizontal.value(),
                self.sb_range_vertical.value(),
                self.fld_out_path.text(),
                self.comboBox.currentText()
            )
        else:
            print("Please, select the output directory!")


    def click_btn_saveall(self):
        if self.fld_out_path.text():
            self.flipbook.save_all(
                self.fld_out_path.text(),
                self.comboBox.currentText()
            )
        else:
            print("Please, select the output directory!")

    def click_btn_path(self):
        path, ext = QFileDialog.getOpenFileName(self, "Select Image", "", 'Images(*.png *.jpg *.jpeg *.tga *.psd)')
        if path:
            self.fld_path.setText(path)
            if self.flipbook.get_image(path):
                self.frames.__del__()
                self.sb_vertical_line.setValue(1)
                self.sb_horizontal_line.setValue(1)
                self.sl_frame.setMaximum(0)
                self.l_t_name.setText(self.flipbook.image_name)
                self.l_t_format.setText(self.flipbook.image_format)
                self.l_t_mode.setText(self.flipbook.image_mode)
                self.l_t_size_mb.setText(self.flipbook.image_size_mb)
                self.l_t_size_px.setText("{0} X {1}".format(*self.flipbook.image_size_px))
                self.label.setText(str(self.sl_frame.value()))
                self.label_2.setText("0")
                self.label_3.setText("{0} X {1}".format(*self.flipbook.image_size_px))
                self.set_preview_img()
            else:
                print("Image is not selected!")
        else:
            print("Image is not selected! Please, select an image!")

    def changed_sl_frame(self):
        if self.sl_frame.value() > 0:
                self.set_preview_img(self.frames[self.sl_frame.value()-1])
                self.label_3.setText("{0} X {1}".format(*self.frames[self.sl_frame.value()-1].size))
        else:
            self.label_3.setText("{0} X {1}".format(*self.flipbook.image_size_px))
            self.set_preview_img()

    def changed_sb_frames_count(self):
        if self.flipbook.source_image:
            self.frames.__del__()
            self.frames.framesCount = self.sb_vertical_line.value(), self.sb_horizontal_line.value()
            self.frames.frameSize = self.flipbook.image_size_compensation()
            self.flipbook.reverse_convert()
            self.sl_frame.setMaximum(len(self.frames))
            self.sb_range_horizontal.setMaximum(len(self.frames))
            self.sb_range_vertical.setMaximum(len(self.frames))
            self.label_2.setText(str(len(self.frames)))
            if self.sl_frame.value() != 0:
                self.set_preview_img(self.frames[self.sl_frame.value()-1])
        else:
            print("Image is not selected! Please, select an image!")

    def set_preview_img(self, img=0):
        data, size = self.flipbook.get_image_data(img)
        qim = QImage(data, size[0], size[1], QImage.Format_ARGB32)
        pix = QPixmap.fromImage(qim)
        self.l_preview_image.setPixmap(pix)

if __name__ == "__main__":
    qapp = QApplication(sys.argv)
    flipbook = Flipbook()
    flipbook.show()
    qapp.exec_()


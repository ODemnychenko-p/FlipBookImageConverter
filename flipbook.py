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
        if self.frames.framesList:
            r1 = self.sb_range_horizontal.value()
            r2 = self.sb_range_vertical.value()
            if self.fld_out_path.text():
                if r1 == r2 or r1 <= r2:
                    self.flipbook.save(r1, r2, self.fld_out_path.text(), self.comboBox.currentText())
                else:
                    print("Selected range is incorrect!")
            else:
                print("Please, select the output directory!")
        else:
            print("Frames list is empty!")

    def click_btn_saveall(self):
        if self.frames.framesList:
            if self.fld_out_path.text():
                self.flipbook.saveAll(self.fld_out_path.text(), self.comboBox.currentText())
            else:
                print("Please, select the output directory!")
        else:
            print("Frames list is empty!")

    def click_btn_path(self):
        path, ext = QFileDialog.getOpenFileName(self, "Select Image", "", 'Images(*.png *.jpg *.jpeg *.tga *.psd)')
        if path:
            self.fld_path.setText(path)
            if self.flipbook.getImage(path):
                del(self.frames.framesList)
                self.sb_vertical_line.setValue(1)
                self.sb_horizontal_line.setValue(1)
                self.sl_frame.setMaximum(0)
                self.l_t_name.setText(self.flipbook.imgName)
                self.l_t_format.setText(self.flipbook.imgFormat)
                self.l_t_mode.setText(self.flipbook.imgMode)
                self.l_t_size_mb.setText(self.flipbook.imgSizeMb)
                self.l_t_size_px.setText("{0} X {1}".format(self.flipbook.imgSizePX[0], self.flipbook.imgSizePX[1]))
                self.label.setText(str(self.sl_frame.value()))
                self.label_2.setText("0")
                self.label_3.setText("{0} X {1}".format(self.flipbook.imgSizePX[0], self.flipbook.imgSizePX[1]))
                self.set_preview_img()
            else:
                self.statusbar.showMessage("", 5000)
        else:
            print("Image is not selected! Please, select an image!")

    def changed_sl_frame(self):
        if self.sl_frame.value() > 0:
            if self.frames.framesList:
                self.set_preview_img(self.frames.framesList[self.sl_frame.value()-1])
                self.label_3.setText("{0} X {1}".format(
                    self.frames.framesList[self.sl_frame.value()-1].width,
                                               self.frames.framesList[self.sl_frame.value() - 1].height))
            else:
                print("Frames list is empty!")
        else:
            self.label_3.setText("{0} X {1}".format(self.flipbook.imgSizePX[0], self.flipbook.imgSizePX[1]))
            self.set_preview_img()

    def changed_sb_frames_count(self):
        if self.flipbook.sourceImg:
            del(self.frames.framesList)
            self.frames.framesCountX = self.sb_vertical_line.value()
            self.frames.framesCountY = self.sb_horizontal_line.value()
            self.frames.frameSizeX, self.frames.frameSizeY = self.flipbook.imageSizeCompensation()
            self.flipbook.reverseConvertSubUV()
            self.sl_frame.setMaximum(len(self.frames.framesList))
            self.sb_range_horizontal.setMaximum(len(self.frames.framesList))
            self.sb_range_vertical.setMaximum(len(self.frames.framesList))
            self.label_2.setText(str(len(self.frames.framesList)))
        else:
            print("Image is not selected! Please, select an image!")

    def set_preview_img(self, img = 0):
        data, size = self.flipbook.getImgData(img)
        qim = QImage(data, size[0], size[1], QImage.Format_ARGB32)
        pix = QPixmap.fromImage(qim)
        self.l_preview_image.setPixmap(pix)

if __name__ == "__main__":
    qapp = QApplication(sys.argv)
    flipbook = Flipbook()
    flipbook.show()
    qapp.exec_()


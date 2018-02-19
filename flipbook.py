import sys
import os
from PyQt5.QtWidgets import*
from PyQt5.QtGui import*
from lib import Frames, FlipbookConverter

if os.name == 'posix':
    from UI import flipbook_UI_IOS as UI
elif os.name == 'nt':
    from UI import flipbook_UI_WINDOWS_ver2 as UI

class Flipbook(UI.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(Flipbook, self).__init__()
        self.setupUi(self)
        self.tabWidget.setCurrentWidget(self.tab)

        self.sb_start_value.setMinimum(1)
        self.sb_end_value.setMinimum(1)
        self.sb_inc_value.setMinimum(1)

        self.frames = Frames()
        self.flipbook = FlipbookConverter()
        self.sl_frame.setMaximum(0)
        self.bool_ = False

        self.btn_image_path.clicked.connect(lambda: self.click_btn_image_path())
        self.btn_out_path.clicked.connect(lambda: self.click_btn_outpath())
        self.sb_vertical_line.valueChanged.connect(lambda: self.changed_sb_frames_count())
        self.sb_horizontal_line.valueChanged.connect(lambda: self.changed_sb_frames_count())
        self.sl_frame.valueChanged.connect(lambda: self.changed_sl_frame())
        self.btn_save.clicked.connect(lambda: self.click_btn_render())
        self.cb_valid_frame_range.currentIndexChanged.connect(lambda: self.valid_frame_range_changed())

    def valid_frame_range_changed(self):
            self.bool_ = True if self.cb_valid_frame_range.currentIndex() == 1 else 0
            self.sb_start_value.setEnabled(self.bool_)
            self.sb_end_value.setEnabled(self.bool_)
            self.sb_inc_value.setEnabled(self.bool_)

    def click_btn_outpath(self):
        path = QFileDialog.getExistingDirectory(self, "Out Directory", "")
        if path:
            self.fld_out_path.setText(path)
        else:
            print("Output directory is not selected!")

    def click_btn_render(self):
        if self.fld_out_path.text():
            if len(self.frames):
                if self.fld_filename.text():
                    filename = self.fld_filename.text()
                else:
                    filename = "frame"
                if self.bool_:
                    frame_id = 0
                    args = (self.sb_start_value.value(),
                            self.sb_end_value.value(),
                            self.sb_inc_value.value()
                            )
                else:
                    args = ()
                    frame_id = self.sl_frame.value()
                self.flipbook.render(args,
                                     cur_id=frame_id,
                                     path=self.fld_out_path.text(),
                                     ext=self.cb_image_format.currentText(),
                                     filename=filename
                                     )
            else:
                print("Frames list is empty!")
        else:
            print("Please, select the output directory!")

    def click_btn_image_path(self):
        path, ext = QFileDialog.getOpenFileName(self, "Select Image", "", 'Images(*.png *.jpg *.jpeg *.tga *.psd)')
        if path:
            self.fld_image_path.setText(path)
            if self.flipbook.get_image(path):
                self.frames.__del__()
                self.sb_vertical_line.setValue(1)
                self.sb_horizontal_line.setValue(1)
                self.sl_frame.setMaximum(0)
                self.l_t_name.setText(self.flipbook.image_name)
                self.l_t_format.setText(self.flipbook.image_format)
                self.l_t_mode.setText(self.flipbook.image_mode)
                self.l_t_size_mb.setText(self.flipbook.image_size_mb)
                self.l_t_path.setText(self.flipbook.image_path)
                self.l_t_path.setToolTip(self.flipbook.image_path)
                self.l_t_size_px.setText("{0} X {1}".format(*self.flipbook.image_size_px))
                self.l_t_current_frame_id.setText(str(self.sl_frame.value()))
                self.l_t_total_frames_count.setText("0")
                self.l_t_frame_size_px.setText("{0} X {1}".format(*self.flipbook.image_size_px))
                self.set_preview_img()
            else:
                print("Image is not selected!")
        else:
            print("Image is not selected! Please, select an image!")

    def changed_sl_frame(self):
        if self.sl_frame.value() > 0:
                self.set_preview_img(self.frames[self.sl_frame.value()-1])
                self.l_t_frame_size_px.setText("{0} X {1}".format(*self.frames[self.sl_frame.value()-1].size))
        else:
            self.l_t_frame_size_px.setText("{0} X {1}".format(*self.flipbook.image_size_px))
            self.set_preview_img()

    def changed_sb_frames_count(self):
        if self.flipbook.source_image:
            self.frames.__del__()
            self.frames.framesCount = self.sb_vertical_line.value(), self.sb_horizontal_line.value()
            self.frames.frameSize = self.flipbook.image_size_compensation()
            self.flipbook.reverse_convert()
            self.sl_frame.setMaximum(len(self.frames))

            self.sb_start_value.setMaximum(len(self.frames))
            self.sb_end_value.setMaximum(len(self.frames))
            self.sb_inc_value.setMaximum(len(self.frames))

            self.l_t_total_frames_count.setText(str(len(self.frames)))
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


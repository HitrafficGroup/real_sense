import sys
import cv2
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import  QImage, QPixmap
from PySide6.QtCore import Qt, QThread, Signal, Slot
from ui_mainWindow import Ui_MainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import time
from detector_object import Pose_Detector
import pandas as pd
import datetime



class Thread(QThread):
    updateFrame = Signal(QImage)
    def __init__(self, parent=None , mode = False, upBody = False, smooth = True, detectionCon = None, trackCon = None):
        QThread.__init__(self, parent)
        self.aux_hip_izq,self.temp_hip_izq = [],[]
        self.status = True
        self.cap = True
        self.detector  = Pose_Detector()
        self.modo = "hombros"
        
    def run(self):
        self.detector.start()
        while self.status:
            ret, depth_frame, color_frame = self.detector.get_frame()
            color_frame = self.detector.find_Pose(color_frame)
            LmList = self.detector.find_Position(color_frame)

            (List_Data,temp, angle_hip_izq, angle_hip_dere, angle_knee_izq, 
            angle_knee_dere, angle_ankle_izq, angle_ankle_dere)  = self.detector.angle_joint(LmList)

            self.detector.angles_to_Lists(temp,angle_hip_izq, angle_hip_dere, angle_knee_izq, 
                                            angle_knee_dere, angle_ankle_izq, angle_ankle_dere)
            Data_to_Excel = self.detector.save_data_to_List(List_Data)
            frame = cv2.cvtColor(color_frame, cv2.COLOR_BGR2RGB)
            image = QImage(frame, frame.shape[1], frame.shape[0], 
                       frame.strides[0], QImage.Format_RGB888)
            scaled_img = image.scaled(720, 360, Qt.KeepAspectRatio)
            self.updateFrame.emit(scaled_img)
       
        self.detector.release()
        cv2.destroyAllWindows()
        self.save_to_Excel(Data_to_Excel)
        sys.exit(-1)

    def setFlagData(self, data):
        print("el modo de operacion  es:",data)
        self.modo = data
    def save_to_Excel(self, Data_to_Excel):
        
        Data_Frame = pd.DataFrame(Data_to_Excel, columns=['Tiempo','Ang_Cade_iz', 'Ang_Cade_de', 
                                'Ang_Rod_iz', 'Ang_Rod_de', 'Ang_Tob_iz', 'Ang_Tob_de'])

        tiempo = datetime.datetime.now()
        dt_string = tiempo.strftime("%d-%m-%Y-%H-%M-%S")
        Data_Frame.to_csv("ANGULOS-ARTICULARES-{}.csv".format(dt_string), index = False, sep = ';')
        print("Archivo  Guardado")
        Data_Frame.to_excel("ANGULOS-ARTICULARES-{}.xlsx".format(dt_string))
        print("Archivo excel Guardado")

        
 
class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class MainWindow(QMainWindow):
    flagArm = Signal(str)
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #programcion de los botones
        self.ui.btnStart.clicked.connect(self.start)
        self.ui.btnStop.clicked.connect(self.kill_thread)
        #conexion de los signal
        self.th = Thread(self)
        self.th.finished.connect(self.close)
        self.th.updateFrame.connect(self.setImage)

    def setFlagArm(self,_data):
        self.th.setFlagData(_data)
   
    @Slot()
    def kill_thread(self):
        cv2.destroyAllWindows()
        self.th.status = False
        time.sleep(10)
    
    @Slot()
    def start(self):
        self.th.start()
    @Slot(QImage)
    def setImage(self, image):
        self.ui.camera.setPixmap(QPixmap.fromImage(image))

      


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())

# Importamos las librerias a usar
from sre_constants import SUCCESS
import pyrealsense2 as rs
import numpy as np
import cv2

import mediapipe as mp
import matplotlib.pyplot as plt 
import pandas as pd
import sys
import datetime

import threading



class Pose_Detector:
    def __init__(self, mode = False, upBody = False, smooth = True, detectionCon = None, trackCon = None):
        self.pipeline = rs.pipeline()
        self.config = rs.config()
        self.config.enable_stream(rs.stream.depth, 1280, 720, rs.format.z16, 30)  
        self.config.enable_stream(rs.stream.color, 1920, 1080, rs.format.bgr8, 30) 
        self.mode = bool(mode)
        self.upBody = bool(upBody)
        self.smooth = bool(smooth)
        self.detectionCon = True if detectionCon else False
        self.trackCon = True if trackCon else False
        self.mpPose = mp.solutions.pose
        self.mpDraw = mp.solutions.drawing_utils
        self.posicion = False
        self.pose = self.mpPose.Pose(self.mode, self.upBody, self.smooth, self.detectionCon, self.trackCon)

        self.List_Data = []
        self.Data_to_Excel = []  
        self.Data_hip_izq, self.Data_hip_dere, self.Data_knee_izq, self.Data_knee_dere = [], [], [], []
        self.Data_ankle_izq , self.Data_ankle_dere = [], []

        self.tiempo = []
        self.aux_hip_izq,self.temp_hip_izq = [],[]
        self.aux_hip_dere,self.temp_hip_dere = [],[]
        self.aux_knee_izq,self.temp_knee_izq = [],[]
        self.aux_knee_dere,self.temp_knee_dere = [],[]
        self.aux_ankle_dere,self.temp_ankle_dere = [],[]
        self.aux_ankle_izq,self.temp_ankle_izq = [],[]



    def start(self):
        # Start streaming
        self.pipeline.start(self.config)

    def get_frame(self):
        frames = self.pipeline.wait_for_frames()
        depth_frame = frames.get_depth_frame()
        color_frame = frames.get_color_frame()
        if not depth_frame or not color_frame:
            return False, None, None
        depth_image = np.asanyarray(depth_frame.get_data())
        color_image = np.asanyarray(color_frame.get_data())
        return True, depth_image, color_image

    def release(self):
        self.pipeline.stop()

    def find_Pose(self, color_frame, draw = True):
        imgRGB = cv2.cvtColor(color_frame, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks:
            self.posicion = True
            if draw:
                self.mpDraw.draw_landmarks(color_frame, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
        else:
           
            self.posicion = False

        return color_frame

    def find_Position(self, color_frame, draw = True):
        LmList = []
        if self.posicion == True:
            h, w, c = color_frame.shape
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                cx = int(lm.x * w)
                cy = int(lm.y * h)
                cz = int(lm.z * c)
                LmList.append([id, cx, cy])
                if draw:
                    cv2.circle(color_frame, (cx, cy), 1, (0, 255, 0), cv2.FILLED)


        return LmList

    def angle_joint(self, LmList):
        self.List_Data = []
        LmList = LmList
        if self.posicion == True:
            temp = str(datetime.datetime.now())
            angle_hip_izq = angle_between_vectors(LmList[25][1], LmList[25][2], LmList[23][1], LmList[23][2],LmList[11][1], LmList[11][2]) 
            angle_hip_dere = angle_between_vectors(LmList[26][1], LmList[26][2], LmList[24][1], LmList[24][2], LmList[12][1], LmList[12][2])
            angle_knee_izq = angle_between_vectors(LmList[27][1], LmList[27][2], LmList[25][1], LmList[25][2], LmList[23][1], LmList[23][2]) 
            angle_knee_dere = angle_between_vectors(LmList[28][1], LmList[28][2], LmList[26][1], LmList[26][2], LmList[24][1], LmList[24][2])
            angle_ankle_izq = angle_between_vectors(LmList[29][1], LmList[29][2], LmList[27][1], LmList[27][2], LmList[25][1], LmList[25][2])# en x2, y2 usa coordenadas del talon 
            angle_ankle_dere = angle_between_vectors(LmList[30][1], LmList[30][2],LmList[28][1], LmList[28][2], LmList[26][1], LmList[26][2]) # en x2, y2 usa coordenadas del talon
   
            self.List_Data = [temp,angle_hip_izq, angle_hip_dere, angle_knee_izq, 
                                angle_knee_dere, angle_ankle_izq, angle_ankle_dere]

        if self.posicion == False:
            temp = str(datetime.datetime.now())
            angle_hip_izq, angle_hip_dere, angle_knee_izq, angle_knee_dere =  0.0, 0.0, 0.0, 0.0
            angle_ankle_dere, angle_ankle_izq = 0.0, 0.0



            self.List_Data = [temp ,angle_hip_izq, angle_hip_dere, angle_knee_izq, 
                                angle_knee_dere, angle_ankle_izq, angle_ankle_dere]


        return  (self.List_Data, temp,angle_hip_izq, angle_hip_dere, angle_knee_izq, angle_knee_dere, angle_ankle_izq, angle_ankle_dere) 

    def angles_to_Lists(self,temp,angle_hip_izq, angle_hip_dere, angle_knee_izq, 
                        angle_knee_dere, angle_ankle_izq, angle_ankle_dere):



 
        self.tiempo.append(temp)                    
        self.Data_hip_izq.append(angle_hip_izq)
        self.Data_hip_dere.append(angle_hip_dere)
        self.Data_knee_izq.append(angle_knee_izq)
        self.Data_knee_dere.append(angle_knee_dere)
        self.Data_ankle_izq.append(angle_ankle_izq)
        self.Data_ankle_dere.append(angle_ankle_dere)



    def save_data_to_List(self, List_Data):
        self.List_Data = List_Data
        if self.posicion == True:
            if len(self.List_Data) != 0:
                self.Data_to_Excel.append(List_Data)

        return self.Data_to_Excel
    


def angle_between_vectors(x2, y2, x1, y1, x0, y0):
    v1 = [-(x1 - x0), (y1 - y0)]
    v2 = [-(x1 - x2), (y1 - y2) ]
    dot_product = np.dot(v1, v2)
    norm_product = np.linalg.norm(v1) * np.linalg.norm(v2)
    angle = np.arccos(dot_product / norm_product)*(180/np.pi)
    angle = 180-angle

    return angle



    
   

    
    
    



 

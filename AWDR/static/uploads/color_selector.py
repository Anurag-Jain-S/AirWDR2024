import cv2

def color_detector():

    def setValues(x):
        print("")
    # creating a window for HUE selector
    cv2.namedWindow("Color detectors") 
    cv2.createTrackbar("Upper Hue", "Color detectors", 153, 180, setValues) 
    cv2.createTrackbar("Upper Saturation", "Color detectors", 255, 255, setValues) 
    cv2.createTrackbar("Upper Value", "Color detectors", 255, 255, setValues) 
    cv2.createTrackbar("Lower Hue", "Color detectors", 64, 180, setValues) 
    cv2.createTrackbar("Lower Saturation", "Color detectors", 72, 255, setValues) 
    cv2.createTrackbar("Lower Value", "Color detectors", 49, 255, setValues)

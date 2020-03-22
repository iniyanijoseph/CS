# not my code. This is from ASDRP program that i found interesting
from scipy.spatial import distance as dist
from imutils.video import FileVideoStream
from imutils.video import VideoStream
from imutils import face_utils
import numpy as np
import argparse
import imutils
import time
import dlib
import cv2
import PySimpleGUI as sg
import time


def eye_aspect_ratio(eye):
    # calculate vertical distances
    vert_dist_1 = dist.euclidean(eye[1], eye[5])
    vert_dist_2 = dist.euclidean(eye[2], eye[4])
    #  calculate horizontal distances
    horiz_dist = dist.euclidean(eye[0], eye[3])
    ear = (vert_dist_1 + vert_dist_2) / (2 * horiz_dist)
    return ear
#  parse arguments


ap = argparse.ArgumentParser()
ap.add_argument("-p", "--shape-predictor", required=True, help="path to facial landmark predictor")
ap.add_argument("-v", "--video", type=str, default="", help="path to input video file")
args = vars(ap.parse_args())
#  threshold to determine if a blink occurred
EAR_THRESHOLD = 0.27
#  number of consecutive frames the threshold condition must be met
EAR_CONSECUTIVE_FRAMES = 4
#  counter for blinks
COUNTER = 0
#  total number of blinks
TOTAL = 0
layout = [ [sg.Text('Press OK to start the blink detection program')],
            [sg.OK(), sg.Cancel()] ]
# Create the Window
window = sg.Window('Blink Detection', layout)
# Event Loop to process "events"
while True:
    event, values = window.Read()
    if event in (None, 'Cancel'):
        break
    else:
        window.Close()
        Time = sg.PopupGetText("Set Time", "How long do you want the blink detector to run for?")
        TIMER = int(Time)
        # initialize dlib's face detector (HOG-based) and then create
        # the facial landmark predictor
        print("[INFO] loading facial landmark predictor...")
        detector = dlib.get_frontal_face_detector()
        predictor = dlib.shape_predictor(args["shape_predictor"])
        # grab the indexes of the facial landmarks for the left and
        # right eye, respectively
        (lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
        (rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]
        # start the video stream thread
        print("[INFO] starting video stream thread...")
        vs = VideoStream(src=0).start()
        fileStream = False
        time.sleep(1.0)
        startTime = time.time()
        print("TIMER STARTED")
        elapsedTime = 0
        # loop over frames from the video stream
        while elapsedTime < TIMER:
            endTime = time.time()
            elapsedTime = endTime - startTime
            # if this is a file video stream, then we need to check if
            # there any more frames left in the buffer to process
            if fileStream and not vs.more():
                break
            # grab the frame from the threaded video file stream, resize
            # it, and convert it to grayscale
            # channels)
            frame = vs.read()
            frame = imutils.resize(frame, width=450)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # detect faces in the grayscale frame
            rects = detector(gray, 0)
            # loop over the face detections
            for rect in rects:
                # determine the facial landmarks for the face region, then
                # convert the facial landmark (x, y)-coordinates to a NumPy
                # array
                shape = predictor(gray, rect)
                shape = face_utils.shape_to_np(shape)
                # extract the left and right eye coordinates, then use the
                # coordinates to compute the eye aspect ratio for both eyes
                leftEye = shape[lStart:lEnd]
                rightEye = shape[rStart:rEnd]
                leftEAR = eye_aspect_ratio(leftEye)
                rightEAR = eye_aspect_ratio(rightEye)
                # average the eye aspect ratio together for both eyes
                ear = (leftEAR + rightEAR) / 2.0
                # compute the convex hull for the left and right eye, then
                # visualize each of the eyes
                leftEyeHull = cv2.convexHull(leftEye)
                rightEyeHull = cv2.convexHull(rightEye)
                cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
                cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)
                # check to see if the eye aspect ratio is below the blink
                # threshold, and if so, increment the blink frame counter
                if ear < EAR_THRESHOLD:
                    COUNTER += 1
                # otherwise, the eye aspect ratio is not below the blink
                # threshold
                else:
                    # if the eyes were closed for a sufficient number of
                    # then increment the total number of blinks
                    if COUNTER >= EAR_CONSECUTIVE_FRAMES:
                        TOTAL += 1
                    # reset the eye frame counter
                    COUNTER = 0
                # draw the total number of blinks on the frame along with
                # the computed eye aspect ratio for the frame
                cv2.putText(frame, "Blinks: {}".format(TOTAL), (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                cv2.putText(frame, "EAR: {:.2f}".format(ear), (300, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                # show the frame
                cv2.imshow("Frame", frame)
                key = cv2.waitKey(1) & 0xFF
                # if the `q` key was pressed, break from the loop
                if key == ord("q"):
                    x = 4
                    break
        else:
            print("FINISHED")
            loopContinue = False
            # do a bit of cleanup
            cv2.destroyAllWindows()
            vs.stop()
            blinkRate = TOTAL / TIMER
            text1 = ('Blink rate is too low. Please blink more.')
            text2 = ('Blink rate is normal.')
            sg.Popup("Results", "Blink rate:", blinkRate, "Total blinks:", TOTAL)
            #  0.083 -- strained rate (5 blinks /60 sec)
            #  0.133 is 8 blinks / 60 sec
            if blinkRate < 0.133:
                sg.Popup(text1)
                break
            else:
                sg.Popup(text2)
                break
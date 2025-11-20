# apps/attendance/views.py
import cv2
from deepface import DeepFace
from django.shortcuts import render
from django.http import HttpResponse
import os

def capture_attendance(request):
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        return HttpResponse("Camera not detected!")

    ret, frame = cam.read()
    cam.release()

    if not ret:
        return HttpResponse("Failed to capture image!")

    # Save temporary frame
    tmp_path = os.path.join("core", "media", "tmp.jpg")
    cv2.imwrite(tmp_path, frame)

    try:
        # DeepFace recognition against your dataset folder
        result = DeepFace.find(img_path=tmp_path, db_path="core/media/faces", model_name="VGG-Face")

        if len(result) > 0:
            recognized_name = os.path.basename(result[0]['identity'][0].split("\\")[-2])
            return HttpResponse(f"Attendance recorded for: {recognized_name}")
        else:
            return HttpResponse("Face detected but not recognized.")
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")

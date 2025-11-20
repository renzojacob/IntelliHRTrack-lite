from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


@login_required
def employee_dashboard(request):
    return render(request, 'employee/dashboard.html')

@login_required
def admin_dashboard(request):
    return render(request, 'admin/dashboard_final.html')

@staff_member_required
def admin_dashboard(request):
    return render(request, "admin/dashboard_final.html")


# Additional code for capturing attendance using OpenCV
# attendance/views.py

# attendance/views.py

import cv2
from django.http import HttpResponse
import time

def capture_attendance(request):
    """
    Open webcam, detect faces, and return how many faces are detected.
    """
    # Load Haar Cascade for frontal face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Open default webcam
    cam = cv2.VideoCapture(0)
    faces = []

    # Capture 5 frames to give camera time to adjust
    for i in range(5):
        ret, frame = cam.read()
        if not ret:
            continue

        # Convert to grayscale for detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

        if len(faces) > 0:
            break  # stop if we detected at least one face

        time.sleep(0.2)  # small delay between frames

    # Release camera
    cam.release()
    cv2.destroyAllWindows()

    return HttpResponse(f"Detected {len(faces)} face(s)")

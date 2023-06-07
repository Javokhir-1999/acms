# import os
# import sys

# SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# sys.path.append(os.path.dirname(SCRIPT_DIR))

# os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings'
# import django
# django.setup()

# import cv2
# cap = cv2.VideoCapture("rtsp://admin:voltohik23@192.168.0.25:554/ISAPI/Streaming/Channels/101")

# while(cap.isOpened()):
#     ret, frame = cap.read()
#     cv2.imshow('frame', frame)
#     if cv2.waitKey(20) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()
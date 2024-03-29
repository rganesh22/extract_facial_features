import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc('D','I','V','X')
out = cv2.VideoWriter('Videos\output.avi',-1, 20.0, (640,480))

print str(fourcc)
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
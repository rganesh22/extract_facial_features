import cv2
import numpy as np

faceCascade = cv2.CascadeClassifier("E:\OpenCV\opencv\sources\data\haarcascades\haarcascade_frontalface_alt.xml")
eyeCascade = cv2.CascadeClassifier("E:\OpenCV\opencv\sources\data\haarcascades\eye.xml")
noseCascade = cv2.CascadeClassifier("E:\OpenCV\opencv\sources\data\haarcascades\\nose.xml")
mouthCascade = cv2.CascadeClassifier("E:\OpenCV\opencv\sources\data\haarcascades\mouth.xml")

cap = cv2.VideoCapture("Videos\\output.avi")


#data arrays
faceData = []
faceData.append(0000)
faceData.append(0000)
faceData.append(0000)
faceData.append(0000)

rEyeData = []
rEyeData.append(0000)
rEyeData.append(0000)
rEyeData.append(0000)
rEyeData.append(0000)

lEyeData = []
lEyeData.append(0000)
lEyeData.append(0000)
lEyeData.append(0000)
lEyeData.append(0000)

noseData = []
noseData.append(0000)
noseData.append(0000)
noseData.append(0000)
noseData.append(0000)

mouthData = []
mouthData.append(0000)
mouthData.append(0000)
mouthData.append(0000)
mouthData.append(0000)

lPupilData= []
lPupilData.append(0000)
lPupilData.append(0000)
lPupilData.append(0000)
lPupilData.append(0000)

rPupilData = []
rPupilData.append(0000)
rPupilData.append(0000)
rPupilData.append(0000)
rPupilData.append(0000)

pfaceData = []
prEyeData = []
plEyeData = []
pnoseData = []
pmouthData = []

plPupilData= []
prPupilData = []

eye1 = 0
eye2 = 0
aE1 = 0
aE2 = 0

while(cap.isOpened()):

    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    finalEyes = []
    finalNoses = []
    finalMouths = []

    '''
    Facial Features
    '''
    faceH = None
    faceW = None
    faceEndpts=[]
    faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        face_roi = gray[y:y+w, x:x+h]
        faceH = h
        faceW = w

        faceData.append(x)
        faceData.append(y)
        faceData.append(w)
        faceData.append(h)


    if len(faces) >= 1:

        # Detect eyes
        eyes = eyeCascade.detectMultiScale(
                face_roi,
                scaleFactor=1.1,
                minNeighbors=10,
                minSize=(10, 10),
                flags=cv2.CASCADE_SCALE_IMAGE
        )

        for (x, y, w, h) in eyes:
            if y < 100:
                if x < 100:
                    lEyeData.append(x)
                    lEyeData.append(y)
                    lEyeData.append(w)
                    lEyeData.append(h)
                    eye1 = face_roi[y:y+w, x:x+h]
                    aE1 = 1
                    cv2.rectangle(face_roi, (x, y), (x+w, y+h), (0, 255, 0), 2)
                if x > 100:
                    rEyeData.append(x)
                    rEyeData.append(y)
                    rEyeData.append(w)
                    rEyeData.append(h)
                    eye2 = face_roi[y:y+w, x:x+h]
                    aE2 = 1
                    cv2.rectangle(face_roi, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Detect Nose
        noses = noseCascade.detectMultiScale(
                face_roi,
                scaleFactor=1.1,
                minNeighbors=10,
                minSize=(10, 10),
                flags=cv2.CASCADE_SCALE_IMAGE
        )


        nIter = 0
        for (x, y, w, h) in noses:
            if (y + h/2) > faceH/2:
                finalNoses.append(x)
                finalNoses.append(y)
                finalNoses.append(w)
                finalNoses.append(h)
        nIter += 1

        #print len(finalNoses)

        nAreas = [] # Areas of mouth boxes
        nMaxIndex = 100000 #
        for i in range(len(finalNoses)/4):
            i += 1
            # print i
            if i == 1:
                nAreas.append(finalNoses[2] * finalNoses[3])
            else:
                # i *= 4
                nAreas.append(finalNoses[((i * 4) - 4) + 2] * finalNoses[((i * 4) - 4) + 3])

        if len(nAreas) > 0:
            nMaxIndex = nAreas.index(max(nAreas))



        if nMaxIndex != 100000:

            if len(finalNoses) == 4:
                cv2.rectangle(face_roi, (finalNoses[nMaxIndex + 0], finalNoses[nMaxIndex + 1]),
                              (finalNoses[nMaxIndex + 0]+finalNoses[nMaxIndex + 2], finalNoses[nMaxIndex + 1]+finalNoses[nMaxIndex + 3]),
                              (255, 255, 255), 2)

                noseData.append(finalNoses[nMaxIndex + 0])
                noseData.append(finalNoses[nMaxIndex + 1])
                noseData.append(finalNoses[nMaxIndex + 2])
                noseData.append(finalNoses[nMaxIndex + 3])


        # Get Endpoints
        noseEndpts = []

        mouths = mouthCascade.detectMultiScale(
                face_roi,
                scaleFactor=1.1,
                minNeighbors=10,
                minSize=(10, 10),
                flags=cv2.CASCADE_SCALE_IMAGE
        )


        mIter = 0
        for (x, y, w, h) in mouths:
            if (y + h/2) > faceH/2:
                finalMouths.append(x)
                finalMouths.append(y)
                finalMouths.append(w)
                finalMouths.append(h)
        mIter += 1


        mAreas = [] # Areas of mouth boxes
        maxIndex = 0 #
        for i in range(len(finalMouths)/4):
            i += 1
            # print i
            if i == 1:
                mAreas.append(finalMouths[2] * finalMouths[3])
            else:
                # i *= 4
                mAreas.append(finalMouths[((i * 4) - 4) + 2] * finalMouths[((i * 4) - 4) + 3])

        if mAreas:
            maxIndex = mAreas.index(max(mAreas))

        # print maxIndex


        if len(finalMouths) == 4:
            cv2.rectangle(face_roi, (finalMouths[maxIndex + 0], finalMouths[maxIndex + 1]),
                          (finalMouths[maxIndex + 0]+finalMouths[maxIndex + 2], finalMouths[maxIndex + 1]+finalMouths[maxIndex + 3]),
                          (255, 255, 255), 2)

            mouthData.append(finalMouths[maxIndex + 0])
            mouthData.append(finalMouths[maxIndex + 1])
            mouthData.append(finalMouths[maxIndex + 2])
            mouthData.append(finalMouths[maxIndex + 3])


        mouthEndpts = []

        cv2.imshow('frame',face_roi)
    '''
    Gaze Tracking
    '''
    if aE1 == 1:

        # detect eye
        frame = eye1
        detected = eyeCascade.detectMultiScale(frame, 1.3, 5)

        pupilFrame = frame
        pupilO = frame
        windowClose = np.ones((5, 5), np.uint8)
        windowOpen = np.ones((2, 2), np.uint8)
        windowErode = np.ones((2, 2), np.uint8)

        # draw square
        for (x, y, w, h) in detected:
            cv2.rectangle(frame, (x, y), ((x + w), (y + h)), (0, 0, 255), 1)
            cv2.line(frame, (x, y), ((x + w, y + h)), (0, 0, 255), 1)
            cv2.line(frame, (x + w, y), ((x, y + h)), (0, 0, 255), 1)
            pupilFrame = cv2.equalizeHist(frame[y + (h * .25):(y + h), x:(x + w)])
            pupilO = pupilFrame
            ret, pupilFrame = cv2.threshold(pupilFrame, 55, 255, cv2.THRESH_BINARY)  # 50 ..nothin 70 is better
            pupilFrame = cv2.morphologyEx(pupilFrame, cv2.MORPH_CLOSE, windowClose)
            pupilFrame = cv2.morphologyEx(pupilFrame, cv2.MORPH_ERODE, windowErode)
            pupilFrame = cv2.morphologyEx(pupilFrame, cv2.MORPH_OPEN, windowOpen)

            # so above we do image processing to get the pupil..
            # now we find the biggest blob and get the centriod

            threshold = cv2.inRange(pupilFrame, 250, 255)  # get the blobs
            __, contours, hierarchy = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

            # if there are 3 or more blobs, delete the biggest and delete the left most for the right eye
            # if there are 2 blob, take the second largest
            # if there are 1 or less blobs, do nothing

            if len(contours) >= 2:
                # find biggest blob
                maxArea = 0
                MAindex = 0  # to get the unwanted frame
                distanceX = []  # delete the left most (for right eye)
                currentIndex = 0
                for cnt in contours:
                    area = cv2.contourArea(cnt)
                    center = cv2.moments(cnt)
                    cx = 0
                    cy = 0
                    if center['m00'] != 0:
                        cx, cy = int(center['m10'] / center['m00']), int(center['m01'] / center['m00'])
                    distanceX.append(cx)
                    if area > maxArea:
                        maxArea = area
                        MAindex = currentIndex
                    currentIndex = currentIndex + 1

                del contours[MAindex]  # remove the picture frame contour
                del distanceX[MAindex]

            eye = 'right'

            if len(contours) >= 2:  # delete the left most blob for right eye
                if eye == 'right':
                    edgeOfEye = distanceX.index(min(distanceX))
                else:
                    edgeOfEye = distanceX.index(max(distanceX))
                del contours[edgeOfEye]
                del distanceX[edgeOfEye]

            if len(contours) >= 1:  # get largest blob
                maxArea = 0
                for cnt in contours:
                    area = cv2.contourArea(cnt)
                    if area > maxArea:
                        maxArea = area
                        largeBlob = cnt

            if len(largeBlob) > 0:
                center = cv2.moments(largeBlob)
                cx, cy = int(center['m10'] / center['m00']), int(center['m01'] / center['m00'])
                cv2.circle(pupilO, (cx, cy), 5, 255, -1)
                lPupilData.append(cx)
                lPupilData.append(cy)

                # show picture
        cv2.imshow('eye[1]', pupilO)
        cv2.moveWindow('eye[1]',1000,200)
        cv2.imshow('eye[1][Blob]', pupilFrame)
        cv2.moveWindow('eye[1][Blob]',700,200)
    aE1 = 0

    if aE2 == 1:
        # detect eye
        frame = eye2
        detected = eyeCascade.detectMultiScale(frame, 1.3, 5)

        pupilFrame = frame
        pupilO = frame
        windowClose = np.ones((5, 5), np.uint8)
        windowOpen = np.ones((2, 2), np.uint8)
        windowErode = np.ones((2, 2), np.uint8)

        # draw square
        for (x, y, w, h) in detected:
            cv2.rectangle(frame, (x, y), ((x + w), (y + h)), (0, 0, 255), 1)
            cv2.line(frame, (x, y), ((x + w, y + h)), (0, 0, 255), 1)
            cv2.line(frame, (x + w, y), ((x, y + h)), (0, 0, 255), 1)
            pupilFrame = cv2.equalizeHist(frame[y + (h * .25):(y + h), x:(x + w)])
            pupilO = pupilFrame
            ret, pupilFrame = cv2.threshold(pupilFrame, 55, 255, cv2.THRESH_BINARY)  # 50 ..nothin 70 is better
            pupilFrame = cv2.morphologyEx(pupilFrame, cv2.MORPH_CLOSE, windowClose)
            pupilFrame = cv2.morphologyEx(pupilFrame, cv2.MORPH_ERODE, windowErode)
            pupilFrame = cv2.morphologyEx(pupilFrame, cv2.MORPH_OPEN, windowOpen)

            # so above we do image processing to get the pupil..
            # now we find the biggest blob and get the centriod

            threshold = cv2.inRange(pupilFrame, 250, 255)  # get the blobs
            __, contours, hierarchy = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

            # if there are 3 or more blobs, delete the biggest and delete the left most for the right eye
            # if there are 2 blob, take the second largest
            # if there are 1 or less blobs, do nothing

            if len(contours) >= 2:
                # find biggest blob
                maxArea = 0
                MAindex = 0  # to get the unwanted frame
                distanceX = []  # delete the left most (for right eye)
                currentIndex = 0
                for cnt in contours:
                    area = cv2.contourArea(cnt)
                    center = cv2.moments(cnt)
                    cx = 0
                    cy = 0
                    if center['m00'] != 0:
                        cx, cy = int(center['m10'] / center['m00']), int(center['m01'] / center['m00'])
                    distanceX.append(cx)
                    if area > maxArea:
                        maxArea = area
                        MAindex = currentIndex
                    currentIndex = currentIndex + 1

                del contours[MAindex]  # remove the picture frame contour
                del distanceX[MAindex]

            eye = 'right'

            if len(contours) >= 2:  # delete the left most blob for right eye
                if eye == 'right':
                    edgeOfEye = distanceX.index(min(distanceX))
                else:
                    edgeOfEye = distanceX.index(max(distanceX))
                del contours[edgeOfEye]
                del distanceX[edgeOfEye]

            if len(contours) >= 1:  # get largest blob
                maxArea = 0
                for cnt in contours:
                    area = cv2.contourArea(cnt)
                    if area > maxArea:
                        maxArea = area
                        largeBlob = cnt

            if len(largeBlob) > 0:
                center = cv2.moments(largeBlob)
                cx, cy = int(center['m10'] / center['m00']), int(center['m01'] / center['m00'])
                cv2.circle(pupilO, (cx, cy), 5, 255, -1)
                rPupilData.append(cx)
                rPupilData.append(cy)

                # show picture
        cv2.imshow('eye[2]', pupilO)
        cv2.moveWindow('eye[2]',1000,1)
        cv2.imshow('eye[2][Blobs]', pupilFrame)
        cv2.moveWindow('eye[2][Blobs]',700,0)

    '''
    Write Data to File
    '''

    # if len(faceData) == 0:
    #     faceData = pfaceData
    # else:
    #     pfaceData = faceData
    #
    # if len(noseData) == 0:
    #     noseData = pnoseData
    # else:
    #     pnoseData = noseData
    #
    # if len(mouthData) == 0:
    #     mouthData = pmouthData
    # else:
    #     pmouthData = mouthData
    #
    # if len(lEyeData) == 0:
    #     lEyeData = plEyeData
    #     print 'using prev'
    # else:
    #     plEyeData = lEyeData
    #
    # if len(rEyeData) == 0:
    #     rEyeData = prEyeData
    #     print 'using prev'
    # else:
    #     prEyeData = rEyeData
    #
    if len(lPupilData) == 0:
        lPupilData = plPupilData
    else:
         plPupilData = lPupilData
    #
    if len(rPupilData) == 0:
         rPupilData = prPupilData
    else:
         prPupilData = rPupilData
    print len(rPupilData)
    with open('tbp.vdata', 'a') as f:
        #if len(faceData) != 0 and len(noseData) != 0 and\
        #len(mouthData) != 0 and len(lEyeData) != 0 and\
        #len(rEyeData) != 0 and len(lPupilData) != 0 and len(rPupilData) != 0:
            #f.write('---\n')
            print ' writing'

            if len(faceData) != 0:
                f.write('[face]')
                f.write(',')
                f.write(str(faceData[0]).zfill(4))
                f.write(',')
                f.write(str(faceData[1]).zfill(4))
                f.write(',')
                f.write(str(faceData[2]).zfill(4))
                f.write(',')
                f.write(str(faceData[3]).zfill(4))
                f.write('\n')
            if len(noseData) != 0:
                f.write('[nose]')
                f.write(',')
                f.write(str(noseData[0]).zfill(4))
                f.write(',')
                f.write(str(noseData[1]).zfill(4))
                f.write(',')
                f.write(str(noseData[2]).zfill(4))
                f.write(',')
                f.write(str(noseData[3]).zfill(4))
                f.write('\n')
            if len(mouthData) != 0:
                f.write('[mouth]')
                f.write(',')
                f.write(str(mouthData[0]).zfill(4))
                f.write(',')
                f.write(str(mouthData[1]).zfill(4))
                f.write(',')
                f.write(str(mouthData[2]).zfill(4))
                f.write(',')
                f.write(str(mouthData[3]).zfill(4))
                f.write('\n')
            if len(lEyeData) != 0:
                f.write('[eye[1]]')
                f.write(',')
                f.write(str(lEyeData[0]).zfill(4))
                f.write(',')
                f.write(str(lEyeData[1]).zfill(4))
                f.write(',')
                f.write(str(lEyeData[2]).zfill(4))
                f.write(',')
                f.write(str(lEyeData[3]).zfill(4))
                f.write('\n')
            if len(rEyeData) != 0:
                f.write('[eye[2]]')
                f.write(',')
                f.write(str(rEyeData[0]).zfill(4))
                f.write(',')
                f.write(str(rEyeData[1]).zfill(4))
                f.write(',')
                f.write(str(rEyeData[2]).zfill(4))
                f.write(',')
                f.write(str(rEyeData[3]).zfill(4))
                f.write('\n')
            if len(lPupilData) != 0:
                f.write('[pupil[1]]')
                f.write(',')
                f.write(str(lPupilData[0]).zfill(4))
                f.write(',')
                f.write(str(lPupilData[1]).zfill(4))
                f.write('\n')
            if len(rPupilData) != 0:
                f.write('[pupil[2]]')
                f.write(',')
                f.write(str(rPupilData[0]).zfill(4))
                f.write(',')
                f.write(str(rPupilData[1]).zfill(4))
                f.write('\n')
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            del faceData[:]
            del noseData[:]
            del mouthData[:]
            del lEyeData[:]
            del rEyeData[:]
            del lPupilData[:]
            del rPupilData[:]

cap.release()
cv2.destroyAllWindows()
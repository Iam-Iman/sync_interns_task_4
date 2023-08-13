### Hand Gestures Collection

# import libraries
import os, cv2

# define data directory
data_path = './dataset'
if not os.path.exists(data_path):
    os.makedirs(data_path)

# number of classes used and each per class
num_classes = 3
dataset_size = 100

# video capturing
cap = cv2.VideoCapture(0)
for i in range(num_classes):
    if not os.path.exists(os.path.join(data_path, str(i))):
        os.makedirs(os.path.join(data_path, str(i)))

    print('collecting class {}'.format(i))

    done = False
    while True: # iterate through loop collecting for each class
        ret, frame = cap.read()
        cv2.putText(frame, 'Start.', (100, 50), cv2.FONT_HERSHEY_PLAIN, 1.3, (0, 255, 0), 3,
                    cv2.LINE_AA) # specify text style, color and size of frame
        cv2.imshow('Frame', frame)
        if cv2.waitKey(25) == ord('z'): # press z to start
            break

    counter = 0 # start image collection from 0
    while counter < dataset_size:
        ret, frame = cap.read()
        cv2.imshow('Frame', frame)
        cv2.waitKey(25)
        cv2.imwrite(os.path.join(data_path, str(i), '{}.jpg'.format(counter)), frame)

        counter += 1 # increase collecting by 1 each time
cap.release()
cv2.destroyAllWindows()

import os
import cv2
path = '.\\videodata\\TrainValVideo\\'

video = path + 'video3.mp4'
print(video)
if os.path.exists(video):
    cap = cv2.VideoCapture(video) # 동영상 캡쳐 객체 생성  ---①
    if cap.isOpened():                 # 캡쳐 객체 초기화 확인
        while True:
            ret, img = cap.read()      # 다음 프레임 읽기      --- ②
            if ret:                     
                cv2.imshow(video, img) # 화면에 표시  --- ③
                cv2.waitKey(25)            # 25ms 지연(40fps로 가정)   --- ④
            else:
                break
    else:
        print("can't open video.")
    cap.release()
    cv2.destroyAllWindows()
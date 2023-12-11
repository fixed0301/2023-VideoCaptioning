import json
import cv2

json_path = './videodata/train_val_videodatainfo.json'
video_path = './videodata/TrainValVideo/'

def video_time(json_path, id): #can print descriptions
    with open(json_path, 'r') as f:
        data = json.load(f)
        #print(data.keys()) #dict_keys(['info', 'videos', 'sentences'])
        #print(data['videos'][0].keys()) #dict_keys(['category', 'url', 'video_id', 'start time', 'end time', 'split', 'id'])

        for i in range(140200):
             if data['sentences'][i]['video_id'] == f'video{id}':
                 print(data['sentences'][i]['caption'],',', 'seq:', data['sentences'][i]['sen_id'])

        #for vid in data['videos']:
        #    if vid['video_id'] == 'video' + f'{id}':
        #        time = vid['end time'] - vid['start time']
        #        break
    return


def find_video(json_path, id):
    with open(json_path, 'r') as f:
        data = json.load(f)
        for vid in data['videos']:
            if vid['video_id'] == 'video' + f'{id}':
                file_path = video_path + 'video' + f'{id}.mp4'
                return file_path

def extract_frames(file_path, num_frames=20): #비디오의 프레임 균등하게 추출(20개 문장을 형성할 수 있는 구간으로)
    frames = []
    cap = cv2.VideoCapture(file_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    ret, frame = cap.read()
    if ret:
        for i in range(num_frames):
            frame_idx = int(total_frames * i / num_frames)
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)  # cap 객체를 원하는 위치로 옮겨서 추출
            frames.append(frame)
    else:
        print('Cannot open vid')
        cap.release()
    return frames



#id = 3
#file_path = find_video(json_path, id=id)
#frames = extract_frames(file_path, num_frames=20)
#video_time(json_path, id=id)
#cv2.imshow('asdf', frames[0])
#cv2.waitKey(0)
#cv2.destroyAllWindows()
#print(len(frames))






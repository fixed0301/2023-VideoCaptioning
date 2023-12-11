import os
import cv2


def extract_frames(file_path, num_frames=20):
    frames = []
    cap = cv2.VideoCapture(file_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    if cap.isOpened():
        for i in range(num_frames):
            frame_idx = int(total_frames * i / num_frames)
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)
            ret, frame = cap.read()
            if ret:
                frames.append(frame)
            else:
                break
        cap.release()
    else:
        print('cannot open capture')
    return frames


folder_path = '../videodata/TrainValVideo/'
save_folder_path = '../videodata/TrainValVideo_frame/'
num_frames = 20

for video_idx, video_filename in enumerate(os.listdir(folder_path)):
    video_file_path = os.path.join(folder_path, video_filename)

    # 파일 이름에서 이미 추출된 프레임이 있는지 확인
    existing_frames = [fname for fname in os.listdir(save_folder_path) if video_filename in fname]
    if len(existing_frames) >= num_frames:
        continue  # 이미 추출이 완료된 경우 건너뛰기

    for frame_num in range(len(existing_frames), num_frames):
        save_file_path = f'{save_folder_path}video{video_idx}_{frame_num}.jpg'
        if os.path.exists(save_file_path):
            continue
        else:
            frames = extract_frames(video_file_path, num_frames=num_frames)
            cv2.imwrite(save_file_path, frames[frame_num])


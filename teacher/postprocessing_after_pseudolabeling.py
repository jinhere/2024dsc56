import os
import shutil

# 경로 설정
txt_folder = '/data/yechan2468/share/June5th/runs/detect/predict4/labels'  # .txt 파일들이 있는 폴더
image_folder = '/data/yechan2468/share/June5th/database'  # 이미지 파일들이 있는 폴더
destination_folder = '/data/yechan2468/share/June5th/pseudolabeled_0.8/images'  # 이미지를 옮길 새 폴더
destination_folder_t = '/data/yechan2468/share/June5th/pseudolabeled_0.8/labels'  # 이미지를 옮길 새 폴더

# 새로운 폴더가 없으면 생성
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# txt 폴더의 모든 .txt 파일에 대해 반복
num=0
for txt_file in os.listdir(txt_folder):
    if txt_file.endswith('.txt'):
        num+=1
        # .txt 파일 이름에서 확장자를 제거
        base_name = os.path.splitext(txt_file)[0]
        
        # 이미지 폴더의 모든 파일에 대해 반복
        for image_file in os.listdir(image_folder):
            # 이미지 파일 이름에서 확장자를 제거
            image_base_name = os.path.splitext(image_file)[0]
            
            # .txt 파일 이름과 이미지 파일 이름이 같은 경우
            if base_name == image_base_name:
                # 이미지를 새로운 폴더로 이동
                src_image_path = os.path.join(image_folder, image_file)
                dest_image_path = os.path.join(destination_folder, image_file)
                shutil.copy(src_image_path, dest_image_path)
                print("image",num,"copied")


# 새로운 폴더가 없으면 생성
if not os.path.exists(destination_folder_t):
    os.makedirs(destination_folder_t)

for txt_file in os.listdir(txt_folder):
    src_txt_path = os.path.join(txt_folder, txt_file)
    dest_txt_path = os.path.join(destination_folder_t, txt_file)
    shutil.copy(src_txt_path,dest_txt_path)

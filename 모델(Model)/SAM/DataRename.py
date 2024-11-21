import os

# 데이터가 있는 경로 설정
dataset_path = r'C:\Users\USER\Desktop\dataset'

# 폴더 내의 모든 하위 폴더 순회
for folder_name in ['Training', 'Validation']:
    folder_path = os.path.join(dataset_path, folder_name)
    for case_folder in os.listdir(folder_path):
        case_folder_path = os.path.join(folder_path, case_folder)
        if os.path.isdir(case_folder_path):
            # case1, case2 폴더 내부의 파일들 처리
            for filename in os.listdir(case_folder_path):
                # PNG 파일만 처리
                if filename.endswith('.png'):
                    # 파일 이름에서 뒤의 3자리만 남기고 나머지 삭제
                    base_name = filename.split('_')[-1][:3]  # 뒤의 3자리만 추출
                    new_filename = base_name + '.png'
                    new_filepath = os.path.join(case_folder_path, new_filename)
                    
                    # 파일이 이미 있는지 확인하고, 없다면 이름 변경
                    if not os.path.exists(new_filepath):
                        old_filepath = os.path.join(case_folder_path, filename)
                        os.rename(old_filepath, new_filepath)
                    else:
                        print(f"파일이 이미 존재합니다: {new_filepath}")

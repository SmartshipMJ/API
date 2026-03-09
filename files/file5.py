import csv
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "student.csv")

# CSV 파일 읽기
with open(file_path, 'r', encoding='cp949') as file:
    reader = csv.DictReader(file)
    print("학생 성적 데이터")
    print("-" * 50)
    for row in reader:
        print(f"이름: {row['name']}, 수학: {row['math']}, 과학: {row['science']}, 영어: {row['english']}")

# 추가할 데이터
new_student = [{'name': '이영희', 'math': '95', 'science': '88', 'english': '92'},
               {'name': '김철수', 'math': '85', 'science': '90', 'english': '80'},
               {'name': '박민수', 'math': '78', 'science': '82', 'english': '85'},
               {'name': '홍길동', 'math': '90', 'science': '85', 'english': '88'},
               {'name': '김철수', 'math': '85', 'science': '90', 'english': '80'},
               {'name': '이영하', 'math': '95', 'science': '88', 'english': '92'},
               {'name': '박영현', 'math': '78', 'science': '82', 'english': '85'}]  

# 1. 기존 데이터 읽어서 이미 있는 이름들 수집
existing_names = []
if os.path.exists(file_path):
    with open(file_path, mode='r', encoding='cp949') as file:
        reader = csv.DictReader(file)
        for row in reader:
            existing_names.append(row['name'])

# 2. 리스트에 담긴 학생들을 하나씩 꺼내서 중복 확인 및 쓰기
# 'a' 모드로 파일을 한 번만 열어서 작업하는 것이 효율적입니다.
with open(file_path, mode='a', encoding='cp949', newline='') as file:
    fieldnames = ['name', 'math', 'science', 'english']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    # 파일이 비어있을 때만 헤더(제목줄) 작성
    if os.path.getsize(file_path) == 0:
        writer.writeheader()
    
    # 리스트 안의 각 학생 데이터(s)를 순회
    for s in new_student:
        if s['name'] in existing_names:
            print(f"⚠️ '{s['name']}'님은 이미 데이터에 존재합니다. 건너뜁니다.")
        else:
            writer.writerow(s)
            existing_names.append(s['name']) # 방금 추가한 이름도 목록에 추가 (연속 중복 방지)
            print(f"✅ '{s['name']}'님의 데이터를 추가했습니다.")
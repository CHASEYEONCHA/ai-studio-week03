from pathlib import Path
import pandas as pd
pd.set_option("display.width", 180)

# 파일 경로 설정
BASE_DIR = Path(__file__).resolve().parent
RAW_DATA_path = BASE_DIR / "RAW_DATA.csv"

"""데이터 로드 및 인코딩 문제 해결"""
df = pd.read_csv(RAW_DATA_path, encoding="cp949")

"""데이터 점검 - shape, info() 확인"""
print(" === RAW_DATA.csv 파일 내용 === ")
print(df.shape) # (행 수, 열 수)
print(df.info()) # 열 이름, 타입, 결측 여부

"""확인 결과"""
# === RAW_DATA.csv 파일 내용 === 
# (500, 5)
# <class 'pandas.DataFrame'>
# RangeIndex: 500 entries, 0 to 499
# Data columns (total 5 columns):
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   주문일자    500 non-null    str  
#  1   상품명     500 non-null    str  
#  2   카테고리    500 non-null    str  
#  3   단가      500 non-null    str  
#  4   수량      500 non-null    int64
# dtypes: int64(1), str(4)
# memory usage: 19.7 KB
# None

"""데이터 정제 및 파생 열 생성"""

"""매출 총합, 평균 계산"""

"""Excel 파일 저장"""

"""검증 코드"""

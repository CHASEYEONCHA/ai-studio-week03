from pathlib import Path
import pandas as pd
pd.set_option("display.width", 180)

# 파일 경로 설정
BASE_DIR = Path(__file__).resolve().parent
RAW_DATA_path = BASE_DIR / "RAW_DATA.csv"

"""데이터 로드 및 인코딩 문제 해결"""
df = pd.read_csv(RAW_DATA_path, encoding="cp949")

"""데이터 점검 - shape, info() 확인"""
# print(" === RAW_DATA.csv 파일 내용 === ")
# print(df.shape) # (행 수, 열 수)
# print(df.info()) # 열 이름, 타입, 결측 여부

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
# '단가' 열의 콤마 제거, 숫자 타입 변환
df["단가"] = (pd.to_numeric(df["단가"].astype(str).str.replace(",", "", regex = False), errors = "coerce").astype("Int64"))

# '매출액 = 단가 x 수량' 파생 열 생성
df["매출액"] = df["단가"] * df["수량"]
# print(" === df 데이터프레임 ('매출액' 추가)=== ")
# print(df.head())

"""매출 총합, 평균 계산"""
# '주문일자'에서 '월' 추출
df["주문일자"] = pd.to_datetime(df["주문일자"])
df["월"] = df["주문일자"].dt.month
# print(" === df 데이터프레임 ('월' 추가)=== ")
# print(df.head())

# 월별 x 카테고리별 매출 총합, 평균, 거래건수 집계
## 월별 카테고리
by_mon = df.groupby(["월", "카테고리"])["매출액"].agg(총매출="sum", 평균매출="mean", 거래건수="count")
by_mon = by_mon.reset_index()
# print(" === 월별 카테고리별 매출액 합계 === ")
# print(by_mon.head())

## 카테고리별
by_cat = df.groupby("카테고리")["매출액"].agg(총매출="sum")
by_cat = by_cat.reset_index().sort_values("총매출", ascending=False)
# print(" === 카테고리별 매출액 합계 === ")
# print(by_cat.head())

"""Excel 파일 저장"""

"""검증 코드"""

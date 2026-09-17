# AI 사용 기록
## 1. 데이터 로드 시 RAW_DATA.csv 파일을 찾지 못해 발생한 오류의 해결 방법 질문
- **프롬포트**:
    > 다음 코드로 데이터를 로드하려고 해.  
    df = pd.read_csv("RAW_DATA.csv", encoding="utf-8").  
    그런데 다음과 같은 오류가 나왔어. visual studio에서 파일을 불러오려면 어떻게 해야 해?  
    storage_options=self.options.get("storage_options", None),        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^)^File "/Users/chaseyeon/dev/ai-studio/my_project/venv2/lib/python3.13/site-packages/pandas/io/common.py", line 939, in get_handle. 
    handle = open(handle, ioargs.mode). 
    FileNotFoundError: [Errno 2] No such file or directory: 'RAW_DATA.csv'
- **채택 및 수정 내역**:
    - 답변 중 다음 내용을 채택함:
        > 방법 1. 파이썬 파일 기준 상대 경로 사용 (가장 추천)  
        현재 실행 중인 파이썬 스크립트(__file__)와 같은 폴더에 CSV 파일이 있다면, pathlib을 사용해 파일 위치를 기준으로 절대 경로를 자동 생성하는 것이 가장 깔끔합니다.
        ```python
        from pathlib import Path
        import pandas as pd

        # 현재 .py 파일이 위치한 디렉터리 기준 경로 설정
        BASE_DIR = Path(__file__).resolve().parent
        file_path = BASE_DIR / "RAW_DATA.csv"

        df = pd.read_csv(file_path, encoding="utf-8")
        ``` 
    - 수정 내역:
        ```python
        from pathlib import Path # 추가됨
        import pandas as pd
        pd.set_option("display.width", 180)

        BASE_DIR = Path(__file__).resolve().parent # 추가됨
        RAW_DATA_path = BASE_DIR / "RAW_DATA.csv" # 추가됨

        """데이터 로드 및 인코딩 문제 해결"""
        df = pd.read_csv(RAW_DATA_path, encoding="utf-8") # 수정됨
        ```

- **검증 결과**: `FileNotFoundError`을 해결함.

## 2. openpyxl 미설치로 인한 오류 메시지 설명과 설치 방법 질문
- **프롬포트**:
    > 오류 메시지야. openpyxl가 설치가 안돼서 오류가 난 것 같은데, 어떻게 설치해?  
    Traceback (most recent call last): File "/Users/chaseyeon/dev/ai-studio/my_project/week03/pipeline.py", line 64, in <module> with pd.ExcelWriter("Monthly_Report.xlsx", engine="openpyxl") as writer: ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/Users/chaseyeon/dev/ai-studio/my_project/venv2/lib/python3.13/site-packages/pandas/io/excel/_openpyxl.py", line 58, in __init__ from openpyxl.workbook import Workbook  ModuleNotFoundError: No module named 'openpyxl'
- **채택 및 수정 내역**:
    - 답변 중 다음 내용을 채택함:
        > 현재 프로젝트에서 사용 중인 가상환경(venv2)에 openpyxl 라이브러리가 없어서 발생한 문제입니다.
        > openpyxl 패키지 설치: 터미널에 다음 명령어를 입력하여 설치합니다: `pip install openpyxl`
- **검증 결과**: openpyxl 설치 완료 후 오류를 해결함.
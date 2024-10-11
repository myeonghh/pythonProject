import pandas as pd  # 데이터 처리를 위한 pandas 라이브러리
from sklearn.model_selection import train_test_split  # 데이터를 학습/테스트 세트로 분할하기 위한 함수
from sklearn.linear_model import LinearRegression  # 선형 회귀 모델 클래스
from sklearn.datasets import load_diabetes  # 당뇨병 데이터셋을 로드하는 함수
import seaborn as sns  # 시각화를 위한 seaborn 라이브러리
import matplotlib.pyplot as plt  # 그래프를 그리기 위한 matplotlib 라이브러리
import numpy as np  # 수치 계산을 위한 numpy 라이브러리

# 기존 프로젝트에서 저장된 학습 및 테스트 데이터셋을 가져오는 부분 (사용하지 않으면 주석처리 가능)
from project.machine_learning.linear_regresseion_example import x_train, x_test, y_train, y_test

# 당뇨병 데이터셋을 로드
load_data = load_diabetes()

# 로드한 데이터를 pandas DataFrame으로 변환하고 컬럼명 설정
df = pd.DataFrame(load_data.data, columns=load_data.feature_names)

# 'target' 컬럼에 당뇨병 진행 정도를 추가 (회귀 목표 변수)
df["target"] = load_data.target

# 데이터셋의 첫 5행을 출력하여 확인
print(df.head())

# (주석처리됨) 여러 변수들과 타겟 간의 관계를 시각화하는 pairplot
# sns.pairplot(df[["target", "bmi", "bp", "s1"]])
# plt.show()

# 랜덤 시드 고정 (모델 훈련 시 재현성을 위해)
np.random.seed(0)

# 입력 데이터 (특징) 선택 - 마지막 'target' 컬럼을 제외한 나머지
x = df[df.columns[:-1]]

# 출력 데이터 (목표 변수) 선택 - 'target' 컬럼
y = df["target"]

# 데이터를 학습용과 테스트용으로 분리 (test_size=0.2은 20%를 테스트용으로 할당)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, shuffle=True)

# 선형 회귀 모델 초기화
model = LinearRegression()

# 학습 데이터를 이용해 모델 훈련
model = model.fit(x_train, y_train)

# 모델의 학습된 회귀 계수를 출력
print(model.coef_)

# 테스트 데이터를 이용해 모델 성능을 평가 (결정 계수 R^2 점수를 출력)
print(model.score(x_test, y_test))

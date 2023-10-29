<h1 align="center">원자재 수집 및 예츠 프로젝트 데이터 💻 </h1>



## 🛠️ 기술 스택
<img src="https://img.shields.io/badge/python-3776AB?style=round&logo=python&logoColor=white" /> <img src="https://img.shields.io/badge/pytorch-EE4C2C?style=round&logo=pytorch&logoColor=white" /> <img src="https://img.shields.io/badge/pandas-150458?style=round&logo=pandas&logoColor=white" /> <img src="https://img.shields.io/badge/scikitlearn-F7931E?style=round&logo=scikitlearn&logoColor=white" />



## 🤹🏻 기술 스택 선정 이유
- Python : 다양한 라이브러리를 활용하여 데이터 전처리 및 AI 학습을 진행하기에 유리합니다.
- PyTorch : 직관적이고 간결하게 딥러닝 모델을 활용할 수 있습니다.
- Pandas : 대용량의 데이터를 빠르게 처리하고 시각화하는데 유리합니다.
- Scikit-learn : 스케일러를 활용하여 데이터를 정규화할 수 있습니다.

## 📌 프로젝트 목표

```sh
파이썬을 활용하여 환율 정보, 원자재 가격 정보, 뉴스 정보를 일일 단위로 수집하여 모니터링합니다.
또한 수집한 가격 데이터를 바탕으로 향후 1주일 간의 원자재 가격을 예측합니다.
```

## 🔍 Overview

### 1. 데이터 수집

1) 환율 정보 : 한국수출입은행 Open API 활용
2) 원자재 가격 정보 및 뉴스 정보 : requests, beautifulsoup 활용

<br>

### 2. AI 학습

LSTM을 활용하여 최대 20년치의 가격 정보로 가격의 추이를 학습하여 7일 후까지의 가격을 예측합니다.

<br>

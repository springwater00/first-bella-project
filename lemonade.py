#1. 라이브러리 사용
import tensorflow as tf
import pandas as pd

#2. 데이터 준비
파일경로 = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/lemonade.csv'
데이터 = pd.read_csv(파일경로)
print(데이터.head())

독립 = 데이터[['온도']]
종속 = 데이터[['판매량']]
print(독립.shape, 종속.shape)

#3. 모델 만들기
X = tf.keras.layers.Input(shape=[1])
Y = tf.keras.layers.Dense(1)(X)
model = tf.keras.models.Model(X,Y)
model.compile(loss='mse')

#4. 모델 학습하기
model.fit(독립, 종속, epochs=10000, verbose=0)

#5. 모델에 독립변수를 넣어서 종속변수의 값이 나오는지 체킹
model.predict(독립)

#6. 모델 이용하기
model.predict([[34]])
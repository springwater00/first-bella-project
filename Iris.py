#1. Importing libraries
import pandas as pd
import tensorflow as tf

#2. Preparing Data
Iris = pd.read_csv('https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/iris.csv')
Iris = pd.get_dummies(Iris)   
#Onehot encording(분류할 카테고리를 0과 1의 데이터로 테이블을 만들어주는 과정)
Iris.head()
Iris.columns

iv = Iris[['꽃잎길이', '꽃잎폭', '꽃받침길이', '꽃받침폭']]
dv = Iris[['품종_setosa', '품종_versicolor', '품종_virginica']]
print(iv.shape, dv.shape)

#3. Making a model
X = tf.keras.layers.Input(shape=[4])
Y = tf.keras.layers.Dense(3,activation='softmax')(X) 
#회귀모형은 숫자로 나오면 그만이었기 때문에 그냥 dense(2)(X)를 넣었지만
#분류모형은 확률을 예측해야 하므로 y값이 +- 의 모든 값으로 나오는 것이 아니라 
#0과 1사이에 나올 수 있도록 새로운 함수 (=활성화 함수)로 한번 더 감싸주는데,
#그 활성화 함수가 바로 softmax. 즉, 확률을 예측할 땐 softmax activation fuction.  
model = tf.keras.models.Model(X,Y)
model.compile(loss='categorical_crossentropy', metrics='accuracy')
#loss값은 0이 나올 수록 학습이 잘 된것.
#회귀모형은 loss='mse', 분류모형은 loss='categorical_crossentropy')
#분류모형에서는 loss보다 사람이 보기 더 좋은 지표가 있는데 그게 accuracy.
#accuracy가 1에 가까울 수록 정확하고, 0에 가까울 수록 틀렸음.loss와 반비례.

#4. Learning Model
model.fit(iv,dv,epochs=100)

#5. Using & checking Model
model.predict(iv[-5:])
print(dv[-5:])

#6.get formula
model.get_weights()

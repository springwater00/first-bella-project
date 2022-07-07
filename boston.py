#!. importing libraries
import tensorflow as tf
import pandas as pd

#2. preparing data
boston = pd.read_csv('https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/boston.csv')
print(boston.columns)
iv = boston[['crim', 'zn', 'indus', 'chas', 'nox', 'rm', 'age', 'dis', 'rad', 'tax',
       'ptratio', 'b', 'lstat']]
dv = boston[['medv']]
print(iv.shape, dv.shape)

#3. making model
X = tf.keras.layers.Input(shape=[13])
Y = tf.keras.layers.Dense(1)(X)
model = tf.keras.Model(X,Y)
model.compile(loss='mse')

#4. learning model
model.fit(iv,dv,epochs=100, verbose=0)

#5. using model
model.predict(iv[0:5]) 

#6. compare
dv[0:5]


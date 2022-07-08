#회귀Model 만드는 코드
#퍼셉트론(=뉴런) 하나일 때는 input layer와 output layer뿐.
X = tf.keras.layers.Input(shape=[13])
Y = tf.keras.layers.Dense(1)(X)

#퍼셉트론이 두 개일 때는 중간에 hidden layer가 1개 있음.
#하지만 input&hidden, hidden&output으로 같은 구조가 두번이라고 생각하면 됨.
X = tf.keras.layers.Input(shape=[13])
H = tf.keras.layers.Dense(5, activation='swish')(X)
Y = tf.keras.layers.Dense(1)(H)
model = tf.keras.models.Model(X,Y)
model.compile(loss='mse')

#퍼셉트론이 4개면 hidden layers가 3개
#노드(처리값)은 13->5->3->3->1
X = tf.keras.layers.Input(shape=[13])
H = tf.keras.layers.Dense(5, activation='swish')(X)
H = tf.keras.layers.Dense(3, activation='swish')(X)
H = tf.keras.layers.Dense(3, activation='swish')(X)
Y = tf.keras.layers.Dense(1)(H)
model = tf.keras.models.Model(X,Y)
model.compile(loss='mse')

#데이터 처리할 때 일어나는 문제들.
1. 원핫인코딩(=get dummies) 은 데이터의 종류가 category이거나 object일때만 가능하다.
아이리스 품종칼럼에서 A유형은 1, B유형은 2 이런식으로 숫자로 써서 분류해 놓았다면, 
데이타의 종류를 확인했을 때, int, 즉 정수로 나오기 때문에 get dummies가 먹지 않는다.
이럴때에는 품종 타입의 칼럼을 범주형으로 바꿔준 후 원핫인코딩한다.
print(Iris.dtypes) #데이터 종류 확인하여
Iris['품종'].astype('category') #데이터타입을 int에서 category로 바꾸고
print(Iris.dtypes) #바뀌었는지 확인 후
data = pd.get.dummies(Iris) #원핫인코딩

2. 데이터중 값이 없는 NA일 때는, NA대신 평균값을 자동으로 들어가게 하면 된다.
Iris.isna().sum() #NA값이 몇 개나 되는지, 어떤 칼럼인지 확인하고
mean = Iris['꽃잎폭'].mean() #해당 칼럼의 평균값을 구하고
Iris['꽃잎폭'] = Iris['꽃잎폭'].fillna(mean) #NA를 평균값으로 채우기

#모델을 만들 때 일어나는 문제 : loss가 잘 안떨어진다.
해결책 : dense와 activation을 분리하고, 그 사이에 batchnormalization을 넣는다.
결과 : 그냥 중간에 hidden layer를 넣었을 때 보다도 훨씬 모델 학습이 잘된다.

X = tf.keras.layers.Input(shape=[13])
H = tf.keras.layers.Dense(10, activation="swish")(X)
H = tf.keras.layers.Dense(5, activation="swish")(H)
Y = tf.keras.layers.Dense(1)(H)
model = tf.keras.Model(X,Y)
model.compile(loss='mse')

X = tf.keras.layers.Input(shape=[13])
H = tf.keras.layers.Dense(10)(X)
H = tf.keras.layers.BatchNormalizaion()(H)
H = tf.keras.layers.Activation('swish')(H)

H = tf.keras.layers.Dense(5)(H)
H = tf.keras.layers.BatchNormalizaion()(H)
H = tf.keras.layers.Activation('swish')(H)

Y = tf.keras.layers.Dense(1)(H)
model = tf.keras.Model(X,Y)
model.compile(loss='mse')
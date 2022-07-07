import pandas as pd
# [1. Preparing Data] -----------중요한 것 : 독립, 종속 데이터의 갯수--------------------
#----------------------------------------------------------------------------------------
# 1. csv 파일 불러오기
파일경로 = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/lemonade.csv'
레모네이드 = pd.read_csv(파일경로)

파일경로 = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/boston.csv'
보스턴 = pd.read_csv(파일경로)

파일경로 = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/iris.csv'
아이리스 = pd.read_csv(파일경로)

# 2. 파일의 형태 (행과 열의 갯수) 확인하기
print(레모네이드.shape)
print(보스턴.shape)
print(아이리스.shape)

# 3. csv 파일의 columns 이름 추출하기
print(레모네이드.columns)
print(보스턴.columns)
print(아이리스.columns)

# 4. 독립변수와 종속변수 extract하기
독립 = 레모네이드[['온도']]
종속 = 레모네이드[['판매량']]
print(독립.shape, 종속.shape)

독립 = 보스턴[['crim', 'zn', 'indus', 'chas', 'nox', 'rm', 'age', 'dis', 'rad', 'tax',
       'ptratio', 'b', 'lstat']]
종속 = 보스턴[['medv']]
print(독립.shape, 종속.shape)

독립 = 아이리스[['꽃잎길이', '꽃잎폭', '꽃받침길이', '꽃받침폭']]
종속 = 아이리스[['품종']]
print(독립.shape, 종속.shape)

# 5. csv 파일에서 위에 5행만 출력해보기
print(레모네이드.head())
#----------------------------------------------------------------------------------------


# [2. Making a Model] -------------------------------------------------------------------
#----------------------------------------------------------------------------------------
X = tf.keras.layers.Input(shape=[1]) #독립변수 갯수 []
Y = tf.keras.layers.Dense(1)(X)      #종속변수 갯수 []
model = tf.keras.models.Model(X,Y)
model.compile(loss='mse')
#----------------------------------------------------------------------------------------


# [3. Studying] -------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
model.fit(독립, 종속, epochs=1000)   #훈련횟수 epoch
#----------------------------------------------------------------------------------------


# [4. Predicting] -------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
print("Predictions: ", model.predict([[15]]))
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow.keras as karas
import json

def load_data(path):
    with open(path,'r') as fp:
        data = json.load(fp)

    X = np.array(data['music'])
    Y = np.array(data['labels'])

    return X, Y

def build_network(X,X_train):
    model = keras.sequential([
        keras.layers.Flatten(input_shape=(X.shape[1],X.shape[2])),
        keras.layers.Dense(512,input_dim = X_train.shape[1],activation='relu',kernel_regularizers.l2(0,0.001)),
        keras.layers.Dropout(0.5)
        keras.layers.Dense(256,activation='relu',kernel_regularizers.l2(0.001)),
        keras.layers.Dropout(0.5)
        keras.layers.Dense(64,activation='relu',kernel_regularizers.l2(0,0.001)),
        keras.layers.Dropout(0.5)
        keras.layers.Dense(10,activation='softmax',kernel_regularizers.l2(0,0.001)),
    ])
    return model 



if __name__ == '__main__':
    X,Y = load_data(path)
    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size= 0.3)


    model = buil_network(X,X_train)
    optimizer = kera.optimizer.Adam(learning_rate = 0.0001)
    model.compile(optimizer = optimizer ,
                    loss = 'categorical_crossentropy',
                    metrics = ['accuracy'])
    model,summary()
    model.fit(X_train,Y_train,validation_data=(X_test,Y_test),batch_size=32, epochs = 100 )

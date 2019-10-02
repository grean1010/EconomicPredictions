# Set the seed value for the notebook so the results are reproducible
from numpy.random import seed
seed(1)

# Dependencies
import numpy as np
import pandas as pd
import tensorflow
tensorflow.keras.__version__

# Import the data file and create column names
names = ['date','median_house', 'gold_price','dow_open','gdp', 'fed_rate', '13_wk', '5_yr', '10_yr', '30_yr',\
        'unemployment', 'gas_price', 'earnings_chg', 'cpi', 'inflation', 'cars_sold', 'housing_starts', 'recession']
economic_data = pd.read_csv('Combined_Data_Base.csv', names=names)
economic_data.head(2)

# Drop the first row of column headers that came with the imported file (inside the csv file)
economic_data = economic_data.drop([0], axis=0)
economic_data.head(2)

# Check for data type, as string will not compute in model, if string must convert to float
economic_data.dtypes

# Convert all the data types to float
economic_data[['median_house', 'gold_price','dow_open','gdp', 'fed_rate', '13_wk', '5_yr', '10_yr', '30_yr', \
        'unemployment', 'gas_price', 'earnings_chg', 'cpi', 'inflation', 'cars_sold', 'housing_starts']] = \
        economic_data[['median_house', 'gold_price','dow_open','gdp', 'fed_rate', '13_wk', '5_yr', '10_yr', '30_yr', \
        'unemployment', 'gas_price', 'earnings_chg', 'cpi', 'inflation', 'cars_sold', 'housing_starts']].astype(np.float64)

# Confirming data type conversion to float from string
economic_data.dtypes

# Drop date column and any other coloumn(s) lacking data back to oldest majority date (in this case Jan 1963)
economic_data.drop(columns = ["date", "30_yr", "gas_price", "cars_sold"], inplace = True)
economic_data.head(2)

# Last data file cleaning step, if needed
#economic_data.dropna(inplace = True)

# Pre-processing of the data for ML
# assign x & y
X = economic_data.drop("recession", axis=1)
y = economic_data["recession"]
print(X.shape, y.shape)

# Additional dependencies/functions for modeling to import
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from tensorflow.keras.utils import to_categorical

# Randomly splitting up the data set into separate training and testing data sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, random_state=1, stratify=y)

# Scaling the data
X_scaler = MinMaxScaler().fit(X_train)
X_train_scaled = X_scaler.transform(X_train)
X_test_scaled = X_scaler.transform(X_test)

# Step 1: Label-encode data set
label_encoder = LabelEncoder()
label_encoder.fit(y_train)
encoded_y_train = label_encoder.transform(y_train)
encoded_y_test = label_encoder.transform(y_test) 

# Step 2: Convert encoded labels to one-hot-encoding
y_train_categorical = to_categorical(encoded_y_train)
y_test_categorical = to_categorical(encoded_y_test)

# Creating the Deep Learning Model
# Importing additional modeling functions
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Create model and add layers
# changed input_dim from 20 to value shown correct an error relating to the number of expected values
model = Sequential()
model.add(Dense(units=100, activation='relu', input_dim=13)) 
model.add(Dense(units=100, activation='relu'))
model.add(Dense(units=2, activation='softmax'))

# Compile and fit the model
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Assessing model 
model.summary()

# Fit the model
model.fit(
    X_train_scaled,
    y_train_categorical,
    epochs=60,
    shuffle=True,
    verbose=2
)

# Quantify the training of the model
model_loss, model_accuracy = model.evaluate(
    X_test_scaled, y_test_categorical, verbose=2)
print(
    f"Normal Neural Network - Loss: {model_loss}, Accuracy: {model_accuracy}")

# Make predictions (display)
encoded_predictions = model.predict_classes(X_test_scaled[:5])
print(encoded_predictions)
prediction_labels = label_encoder.inverse_transform(encoded_predictions)
print(prediction_labels)

print(f"Predicted classes: {prediction_labels}")
print(f"Actual Labels: {list(y_test[:5])}")

# Test model with positive and negative lists
yes_list = [179400.0, 271.0, 10734.0, 1.1, 4.14, 3.53, 4.89, 5.37, 4.5, -114.0, 178.0, 0.2, 1636.0]
X_train_scaled = X_scaler.transform([yes_list])
prediction = model.predict_classes(np.array(X_train_scaled))
answer = label_encoder.inverse_transform(prediction)
prediction[:]
print(answer)

no_list = [18200.0, 35.1, 682.9, 3.6, 3.0, 2.9, 3.67, 3.93, 5.7, 90.0, 30.5, 0.33, 1534.0]
X_train_scaled2 = X_scaler.transform([no_list])
prediction2 = model.predict_classes(np.array(X_train_scaled2))
answer2 = label_encoder.inverse_transform(prediction2)
prediction2[:]
print(answer2)






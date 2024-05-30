
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import LabelEncoder

# Load the data into a pandas DataFrame
data = pd.read_csv('product_data.csv')

# Convert the expiry date column to a numerical format
data['expiry_date'] = pd.to_datetime(data['expiry_date'])
data['expiry_date'] = (data['expiry_date'] - pd.to_datetime('1970-01-01')) // np.timedelta64(1, 'D')

# Split the DataFrame into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data.drop('expiry_date', axis=1), data['expiry_date'], test_size=0.2)

# Train a regression model on the training set
model = LinearRegression()
model.fit(X_train, y_train)

# Use the model to predict the expiry dates for the testing set
predictions = model.predict(X_test)

# Evaluate the performance of the model using mean absolute error
mae = mean_absolute_error(y_test, predictions)
print(f'Mean Absolute Error: {mae} days')
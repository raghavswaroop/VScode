import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
# Read in the data from the CSV file
df = pd.read_csv('../datasets/payment_fraud.csv')
df.sample(30)


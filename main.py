import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

#Data Set
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

df = pd.read_csv(url)

#inspect Data
print(df.info())
print(df.describe())

#Handle Missing Values
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

#Handle Duplicate
df = df.drop_duplicates()

#filter data: Passenger is 1st class
first_class = df[df["Pclass"] == 1]
print("\nFirst Class Passengers: \n", first_class.head())

#BarChart : Survival rate by class
survival_by_Class = df.groupby("Pclass")["Survived"].mean()
survival_by_Class.plot(kind="bar", color="lightblue")
plt.title("Survival Rate BY Class")
plt.ylabel("Survival Rate")
plt.show()

#Histogram : Age distribution
sns.histplot(df["Age"] , kde = True , bins = 20, color="purple")
plt.title("Age Histogram")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

#Scatter plot : Age vs Fare
plt.scatter(df["Age"], df["Fare"], alpha=0.5, c="red")
plt.title("AGE VS FARE")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.show()
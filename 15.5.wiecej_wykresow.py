pip install matplotlib
salaries = [
    ("Mark", 1000),
    ("John", 1500),
    ("Daniel", 2300),
    ("Greg", 5000)
]
#%matplotlib inline
import matplotlib.pyplot as plt
X = [0,1,2,3]
Y = [0,1,0,1]
plt.plot(X, Y)

salaries = [
	("Mark", 1000),
	("John", 1500),
	("Daniel", 2300),
	("Greg", 5000)
]

names = list(map(lambda tup:tup[0], salaries))
salary_values = list(map(lambda tup:tup[1], salaries))

salary_increased_series = df['salary'].apply(lambda salary: salary + 2000)
df['salary'] = salary_increased_series

salary_raise = [2000, 2000, 2000, 2000]
df['salary'] + salary_raise

salaries = [
	("Mark", 1000, 23),
	("John", 1500, 25),
	("Daniel", 2300, 38),
	("Greg", 5000, 42)
]
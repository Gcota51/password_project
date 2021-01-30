import random
import pandas as pd



def getANumber():
	for x in range(6):
  		a = random.randint(1,6) * 10000 + random.randint(1,6) * 1000 + random.randint(1,6) * 100 + random.randint(1,6) * 10 + random.randint(1,6)
  		return a

def generatePass():
	data = pd.read_csv("my_dicewareEsp.csv")
	data.head()
	print(getANumber())



generatePass()
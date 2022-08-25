import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("../data_mining/data_2022-08-15_Audi.xlsx")
print(data)
unique_models = data.Model.unique()
print(unique_models)

data.plot(kind='scatter', x= "Year_of_production", y="Price")
plt.show()

data['Kilometers_traveled'].plot(kind='hist')
plt.show()
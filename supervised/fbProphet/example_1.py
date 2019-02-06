import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
from fbprophet import Prophet



df = pd.read_csv('../../data/dataset_1.csv')
print(df.head())



model = Prophet()
model.fit(df)


future = model.make_future_dataframe(periods=365)
print(future.tail())


forecast = model.predict(future)

print (forecast.tail())


plot1 = model.plot(forecast)
print (type(plot1))

#plot1.figure()


plot1.savefig('./foo.png')
plot1.show()

print('done')


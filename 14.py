#14
from matplotlib import colors, markers, pyplot


years = [1398 , 1399 , 1400, 1401, 1402]
kala = [100 ,90 , 150 , 200 , 400 ]
pyplot.plot(years , kala, marker ='o' , color = 'blue'  )
pyplot.title('Goods')
pyplot.xlabel('Years')
pyplot.ylabel('Price')
pyplot.legend(['Prices01'])
pyplot.show()

numeros = {
	'0': ['', '', ''],
	'1': ['ciento', 'diez', 'uno'],
	'2': ['doscientos', 'veinte', 'dos'],
	'3': ['trescientos', 'treinta', 'tres'],
	'4': ['cuatrocientos', 'cuarenta', 'cuatro'],
	'5': ['quinientos', 'cincuenta', 'cinco'],
	'6': ['seiscientos', 'sesenta', 'seis'],
	'7': ['setecientos', 'setenta', 'siete'],
	'8': ['ochocientos', 'ochenta', 'ocho'],
	'9': ['novecientos', 'noventa', 'nueve']}

def numeros_letras(dict, numero):
	r = []
	if len(numero) == 4:
		r.append('mil')
		return r
	else:	
		for x in range(len(numero)):
			r.append(dict[numero[x]][x])
	
	return print(' '.join(r))

numeros_letras(numeros, '1000')

def palindromo(numero):
	reverso = str(numero)[::-1]
	if reverso == str(numero):
		return 1
	else:
		if int(numero) > 1000000000:
			return 0
		res = int(numero) + int(reverso)
		palindromo(res)
count = 0
for i in range(0, 10000):
	count += palindromo(i)

print(count)


import numpy as np
import random

# m denotes the number of examples here, not the number of features
def gradientDescent(x, y, theta, alpha, m, numIterations):
    xTrans = x.transpose()
    for i in range(0, numIterations):
        hypothesis = np.dot(x, theta)
        loss = hypothesis - y
        # avg cost per example (the 2 in 2*m doesn't really matter here.
        # But to be consistent with the gradient, I include it)
        cost = np.sum(loss ** 2) / (2 * m)
        print("Iteration %d | Cost: %f" % (i, cost))
        # avg gradient per example
        gradient = np.dot(xTrans, loss) / m
        # update
        theta = theta - alpha * gradient
    return theta


def genData(numPoints, bias, variance):
    x = np.zeros(shape=(numPoints, 2))
    y = np.zeros(shape=numPoints)
    # basically a straight line
    for i in range(0, numPoints):
        # bias feature
        x[i][0] = 1
        x[i][1] = i
        # our target variable
        y[i] = (i + bias) + random.uniform(0, 1) * variance
    return x, y

# gen 100 points with a bias of 25 and 10 variance as a bit of noise
x, y = genData(100, 25, 10)
m, n = np.shape(x)
numIterations= 100000
alpha = 0.0005
theta = np.ones(n)
theta = gradientDescent(x, y, theta, alpha, m, numIterations)
print(theta)

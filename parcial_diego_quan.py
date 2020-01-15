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



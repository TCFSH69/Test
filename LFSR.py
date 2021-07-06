file = bytearray(open('C:\\Users\\Patrick\\Desktop\\secretMessage.hex','rb').read())
key = 'CTFlearn{'
arr = list(map(lambda x: '0'*(8-len(x))+x, [bin(ord(key[i])^file[i])[2:] for i in range(len(key))]))

def newvec(seed, vector):
	res = 0
	for i in range(8):
		if seed[i] == '1':
			res ^= int(vector[i])
	return str(res) + vector[:7]

def dfs(arr, vector, seed, idx):
	if idx == len(arr) - 1:
		return seed
	else:
		vector = newvec(seed, vector)
		if vector == arr[idx+1]:
			return dfs(arr, vector, seed, idx+1)

def decrypt(seed, vector, i, file):
	if i != len(file):
		print(chr(int(vector,2) ^ file[i]), end='')
		decrypt(seed, newvec(seed,vector), i+1, file)

for i in range(256):
	b = bin(i)[2:]
	b = '0'*(8-len(b)) + b
	seed = dfs(arr, arr[0], b, 0) 
	if seed != None:
		break

decrypt(seed, arr[0], 0, file)
#Requisitando o anagrama para analise
anagram=input('Digite uma palavra:  ')

# Realiza a contagem de anagramas
def cont_anagram(sub):
	
	
	n = len(sub)
	mp = dict()
	
	# loop para o tamanho de substring
	for i in range(n):
		sb = ''
		for j in range(i, n):
			sb = ''.join(sorted(sb + sub[j]))
			mp[sb] = mp.get(sb, 0)
			
			# Aumentando a contagem correspondente ao dicionário
			mp[sb] += 1

	anas = 0
	
	# loop pelo  dicionário
	# contagem de items  da substring
	for k, v in mp.items():
		anas += (v*(v-1))//2
	return anas




sub = anagram
print(cont_anagram(sub))
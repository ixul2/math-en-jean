n = int(input("Numéro de la colonne : "))
taille = int(input("Taille du pattern précédent : "))
i = int(input("Rang à partir duquel le pattern précédent se répète : "))+1
début = i
éléments_précédents = []

while True:
	Un = 2**i
	numéro_de_la_colonne = Un//(10**n)%10
	if numéro_de_la_colonne in éléments_précédents[(i-début)%taille::taille]:
		break

	else:
		éléments_précédents.append(numéro_de_la_colonne)

	i+=1

premier_rang_pattern = éléments_précédents[(i-début)%taille::taille].index(numéro_de_la_colonne)*taille+((i-début)%taille)+début
print(éléments_précédents, premier_rang_pattern)
print(f"la patern fait {i-premier_rang_pattern} chiffres, et se répète à partir du rang {premier_rang_pattern}")

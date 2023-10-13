def define_linha(indice, resenha):
	
	if (indice == 31):
	
		poster = resenha[5]
		titulo = resenha[4].strip()	
		frase = '        <img src="' + poster + '" alt="' + titulo + '" class="poster">\n'
	
	
	elif (indice == 34):
	
		pfp = "fotosPerfil/" + resenha[2]
		username = resenha[3].replace(" ", "")
		frase = '        	<div><img src="' + pfp + '"> <p id="username"> Review by <span class="user">' + username +'</span> </p> </div>\n'
		
			
	elif (indice == 37):
	
		titulo = resenha[4].strip()
		estrelas = "★" * int(resenha[6])
		
		if (resenha[7] == "Sim"):
			frase = '            <h1 class="titulo">' + titulo + '<span id="ano">' + resenha[9] + '</span> <span id="estrelas">' + estrelas + '</span> <span id="coracao">❤</span> </h1>\n'
		else:
			frase = '            <h1 class="titulo">' + titulo + '<span id="ano">' + resenha[9] + '</span> <span id="estrelas">' + estrelas + '</span> </h1>\n'
		
			
	elif (indice == 40):
		frase = '            <p><span id="texto">' + resenha[8] + '</span></p>\n'
		
		
	return frase	
			
# 0- horário/ 1- email/ 2- foto de perfil/ 3- nome de usuario/ 4- filme/ 5- poster/ 6- estrelas/ 7- coracao/ 8- mensagem/ 9- ano de lançamento
def preenche_arquivo(novaPagina, resenha):

	# modelo
	template = open('template.html')
	linhas = template.readlines()
	
	# antes da página de review todas tem o mesmo começo (header)
	for i in range(31):
		novaPagina.write(linhas[i])
	
	# aqui começa a personalização
	for i in range(31, 53):
		# se é uma das linhas personalizadas
		if (i == 31 or i == 34 or i == 37 or i == 40):
			linhaCod = define_linha(i, resenha)
		# se não copia e cola	
		else:
			linhaCod = linhas[i]
			
		novaPagina.write(linhaCod)
		
	template.close()

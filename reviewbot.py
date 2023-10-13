from funcoes import*
import csv

# modelo da página inicial
template = open('paginaInicial.html')
paginaInicial = template.readlines()
novoIndex = open('index.html', "w")

# arquivo com as resenhas
letterboxd = open('reviews.csv', encoding='utf-8')
listaResenhas = csv.reader(letterboxd, delimiter=',')

# a primeira parte da página inicial é normal, então copio e colo no novo index
for i in range(31):
	novoIndex.write(paginaInicial[i])
	
cabecalho = 31
filmes = 0

# 0- horário/ 1- email/ 2- foto de perfil/ 3- nome de usuário/ 4- filme/ 5- pôster/ 6- estrelas/ 7- coração/ 8- mensagem/ 9- ano de lançamento
for resenha in listaResenhas:
  
  	# se é uma das linhas de cabeçalho do INDEX 
	if (filmes == 0):
		for i in range(cabecalho, cabecalho+3):
			novoIndex.write(paginaInicial[i])
		cabecalho += 6
		
	# o strip serve pra tirar os espaços da borda, o replace tira os espaços do meio
	filme = resenha[4].strip()
	nomeArquivo = filme.replace(" ", "") + ".html"
	
	# cria o novo arquivo com  nome do filme + formato // encoding arruma o erro em windows
	novaPagina = open(nomeArquivo, "w", encoding='utf-8')
	preenche_arquivo(novaPagina, resenha)
	novaPagina.close()
	
	indexPoster = '            <a href="' + nomeArquivo + '"><img src="' + resenha[5] + '" alt="' + resenha[4] + '"></a>\n'
	novoIndex.write(indexPoster)
	filmes += 1
	
	if (filmes == 6):
		novoIndex.write('         </section>\n\n')
		filmes = 0

# se não zerou então não fechou o bloco
if (filmes != 0):
	novoIndex.write('         </section>\n\n')

# parte final
for i in range(67, 83):
	novoIndex.write(paginaInicial[i])
	
template.close()
novoIndex.close()
letterboxd.close()

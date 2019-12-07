# Senac_Ep4
EP4 -Stream


-Subir os containers

	docker-compose up -d

-Iniciar o serviço de stream

	docker-compose run processor bash


Obs.: o próprio processor possui métodos para enviar info. ao stream de tempos em tempo utilizando valores randomicos está comentado

-Enviar as informações para o stream:
	faust -A compra send comprasA '{"produto":"queijo","qtd":"2","valor":"8.50"}'

	faust -A compra send comprasA '{"produto":"sabonte","qtd":"5","valor":"3.35"}'

	faust -A compra send comprasA '{"produto":"tenis","qtd":"1","valor":"329.99"}'

	faust -A compra send comprasA '{"produto":"kiwi","qtd":"4","valor":"1.29"}'


-Visualizar as informações do stream - rotas

-Contar vendas em R$ do último 1 minuto (sliding)

	localhost:6066/rs_1_min/valor_1min


-Contar vendas em quantidade de cada 2 minutos (tumbling)

	localhost:6066/qtd_2_min/qtd_2_min

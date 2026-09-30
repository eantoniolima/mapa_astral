#  Mapa Astral

Aplicação desenvolvida em Python para criação de um mapa astral a partir dos dados de nascimento do usuário.

O projeto surgiu devido à ausência de tutoriais completos e específicos na internet sobre a integração entre as bibliotecas utilizadas. Dessa forma, seu desenvolvimento foi realizado de maneira prática e experimental, buscando integrar interface gráfica, 
localização e cálculos astrológicos em uma única aplicação.

##  Sobre o projeto

A aplicação permite informar:

- Nome da pessoa
- Dia, mês e ano de nascimento
- Hora e minuto do nascimento
- Cidade de nascimento
- País de nascimento

A partir dessas informações, o sistema utiliza os dados de localização e os cálculos astrológicos para gerar o mapa astral.

##  Tecnologias e bibliotecas

### Python

Linguagem utilizada para o desenvolvimento de toda a aplicação.

### Streamlit

Utilizado para criar a interface web da aplicação de forma simples e interativa.

### Kerykeion

Biblioteca responsável pelos cálculos astrológicos e pela criação dos dados necessários para o mapa astral.

### GeoNames

Utilizado pelo Kerykeion para obter informações geográficas relacionadas à cidade informada pelo usuário.

### Base64

Utilizado para converter a imagem utilizada na interface para uma representação que possa ser incorporada diretamente ao HTML.

### CSS / HTML

Utilizados para personalizar a aparência da aplicação, incluindo:

- Tema escuro
- Centralização da imagem
- Tamanho da imagem
- Formatação do título
- Personalização visual da página

Caso tenha interesse em ver o app funcionando, basta acessar:
https://mapaastral.streamlit.app/

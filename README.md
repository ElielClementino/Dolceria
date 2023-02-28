# Dolceria
[Dolceria](gifProjeto.gif)
### Feito usando como template [huogerac/djavue](https://github.com/huogerac/djavue)
<br />

## O que é e motivação

Minha irmã é formada em gastrônomia e tem um sonho de abrir uma loja, e a gente sempre brincou sobre eu fazer o site e tudo mais, então pensei, porquê não tentar ? mesmo que obviamente só o  básico tentei aplicar o que eu imaginaria que o site teria como fluxo.

<br />

## Setup do projeto
Mudar a .env-example para .env

docker compose build 

docker compose up

para acessar o site basta colocar na url http://localhost/

## Ajudinha
-- Caso esteja com os containers do nginx/frontend/postgres rodando e o django fora do container, com python manage.py runserver --  

Para poder facilitar o setup do projeto usando o banco adicionei no root do projeto o arquivo "dump.json"  

Ele tem alguns produtos cadastrados, basta rodar no terminal o seguinte comando para jogar esses arquivos no seu banco de dados.  

    python manage.py loaddata dump.json  


-- Caso esteja rodando todos os ambientes com docker(nginx/frontend/backend/postgres)--

Você irá precisar acessar o container do backend
rodando o comando docker ps, você vai ter os ids dos containers que estão rodando, basta pegar o id do container do backend e rodar o seguinte comando no terminal:

    docker exec -it IDDOCONTAINER bash  

Assim que você entrar no container basta rodar o comando:

    python manage.py loaddata dump.json  



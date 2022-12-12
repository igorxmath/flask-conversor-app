# Resumo do projeto
> Projeto em andamento, sendo realizado pelo estudante **Igor Matheus**, visando a prática com a linguagem Python e os conceitos do paradigma de orientação a objetos.
<p align="center">
<img src="https://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge" />
<img src="https://img.shields.io/badge/Flask-0769AD?style=for-the-badge&logo=flask&logoColor=white" />
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" />
</p>

## Funcionalidades do projeto
- `Conversão de medidas`: Conversão rápida e simples de diversas medidas de temperatura.
- `Interface web`: O projeto utiliza o Flask como web framework e o responsivo Skeleton CSS
- `API`: O sistema faz a requisição da taxa cambial atual.
- `CI/CD`: Test, Build e Push automático das imagens ao Docker HUB.

<p align="center">
<img src="https://xbn.igormatheus.com.br/zOGI1/kEjAmaSI21/raw.png" />
</p>

## Como usar a imagem
```console
$ docker run -d \
-p 5000:5000 \
igormath/flask-conversor-app:latest
```

## Técnicas e tecnologias utilizadas

- ``Python 3``
- ``Flask``
- ``Docker``
- ``GitHub Actions``

## Acesso ao projeto
Você pode acessar os arquivos do projeto clicando [aqui](https://github.com/igorxmath/flask-conversor-app/)
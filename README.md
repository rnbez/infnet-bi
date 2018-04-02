## Projeto da Disciplina de Business Intelligence

Esse é o projeto para a disciplina BI. Ele é baseado nos _datasets_ encontrados em na página de dados abertos do Senado. Clique [aqui](https://www12.senado.leg.br/dados-abertos/conjuntos?grupo=senadores&portal=administrativo) para visitar a pagina.

Os datasets utilizados foram os dados de **Cotas para Exercício da Atividade Parlamentar dos Senadores (CEAPS)** referêntes aos anos de [2016](http://www.senado.gov.br/transparencia/LAI/verba/2016.csv), [2017](http://www.senado.gov.br/transparencia/LAI/verba/2017.csv) e [2018](http://www.senado.gov.br/transparencia/LAI/verba/2018.csv).

### Rodando o script de transformação
Para rodar o projeto, primeiro clone esse repositório e baixe o arquivos `.csv` listados abaixo. Copie eles do local de download para a raiz do repositório clonado.

- [Dados de 2016](http://www.senado.gov.br/transparencia/LAI/verba/2016.csv)
- [Dados de 2017](http://www.senado.gov.br/transparencia/LAI/verba/2017.csv)
- [Dados de 2018](http://www.senado.gov.br/transparencia/LAI/verba/2018.csv)

Depois execute:
```
$ mkdir ./out
$ python3 ./src/main.py
```

Após a execução do script, você deve ser capáz de listar o seguintes arquivos com o comando `ls -1 out`:

```
$ ls -1 out
DM_DT_CUSTO.csv
DM_DT_LANCAMENTO.csv
DM_FORNECEDOR.csv
DM_SENADOR.csv
DM_TIPO_DESP.csv
FATO.csv
```

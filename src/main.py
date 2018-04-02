import csv

from tables.dm_dt_custo import DM_DT_CUSTO
from tables.dm_dt_lancamento import DM_DT_LANCAMENTO
from tables.dm_fornecedor import DM_FORNECEDOR
from tables.dm_senador import DM_SENADOR
from tables.dm_tipo_desp import DM_TIPO_DESP
from tables.fato import FATO


def load(files):
    for file in files:
        with open(file, newline='', encoding='latin-1') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                fk_dm_dt_lancamento = DM_DT_LANCAMENTO.add(row['ANO'], row['MES'])
                if not fk_dm_dt_lancamento:
                    continue

                fk_dm_dt_custo = DM_DT_CUSTO.add(row['DATA'])
                if not fk_dm_dt_custo:
                    continue

                fk_dm_senador = DM_SENADOR.add(row['SENADOR'])
                if not fk_dm_senador:
                    continue

                fk_dm_fornecedor = DM_FORNECEDOR.add(row['FORNECEDOR'], row['CNPJ_CPF'])
                if not fk_dm_fornecedor:
                    continue

                fk_dm_tipo_desp = DM_TIPO_DESP.add(row['TIPO_DESPESA'])
                if not fk_dm_tipo_desp:
                    continue

                FATO.add(
                    row['VALOR_REEMBOLSADO'],
                    row['DOCUMENTO'],
                    row['DETALHAMENTO'],
                    fk_dm_dt_lancamento,
                    fk_dm_dt_custo,
                    fk_dm_senador,
                    fk_dm_fornecedor,
                    fk_dm_tipo_desp)


def main():
    load([
        '2016.csv',
        '2017.csv',
        '2018.csv'
    ])

    DM_DT_LANCAMENTO.dump_file('./out')
    DM_DT_CUSTO.dump_file('./out')
    DM_SENADOR.dump_file('./out')
    DM_FORNECEDOR.dump_file('./out')
    DM_TIPO_DESP.dump_file('./out')
    FATO.dump_file('./out')


if __name__ == '__main__':
    main()

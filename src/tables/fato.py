from tables.dump_file import dump_file


class FATO(object):
    headers = ['ID',
               'VALOR_REEMBOLSADO',
               'DOCUMENTO_DESPESA',
               'DETALHAMENTO_DESPESA',
               'FK_DM_DT_LANCAMENTO',
               'FK_DM_DT_CUSTO',
               'FK_DM_SENADOR',
               'FK_DM_FORNECEDOR',
               'FK_DM_TIPO_DESP']
    values = {}
    _empty_value = 'Não informado'

    @classmethod
    def format(cls, _valor_reembolsado, documento, detalhamento,
               fk_dm_dt_lancamento, fk_dm_dt_custo, fk_dm_senador,
               fk_dm_fornecedor, fk_dm_tipo_desp):
        if (not _valor_reembolsado or not fk_dm_dt_lancamento or
            not fk_dm_dt_custo or not fk_dm_senador or
                not fk_dm_fornecedor or not fk_dm_tipo_desp):
            print('DISCARDING: FATO')
            return False, None, None

        id = '%s_%s_%s_%s_%s' % (fk_dm_dt_lancamento, fk_dm_dt_custo,
                                 fk_dm_senador, fk_dm_fornecedor, fk_dm_tipo_desp)
        valor_reembolsado = float(_valor_reembolsado.replace('.', '').replace(',', '.'))
        documento_despesa = documento or cls._empty_value
        detalhamento_despesa = detalhamento or cls._empty_value
        return True, id, [id, valor_reembolsado, documento_despesa, detalhamento_despesa,
                          fk_dm_dt_lancamento, fk_dm_dt_custo, fk_dm_senador,
                          fk_dm_fornecedor, fk_dm_tipo_desp]

    @classmethod
    def add(cls, valor_reembolsado, documento, detalhamento,
            fk_dm_dt_lancamento, fk_dm_dt_custo, fk_dm_senador, fk_dm_fornecedor, fk_dm_tipo_desp):
        succ, id, formatted = cls.format(valor_reembolsado,
                                         documento, detalhamento, fk_dm_dt_lancamento,
                                         fk_dm_dt_custo, fk_dm_senador, fk_dm_fornecedor,
                                         fk_dm_tipo_desp)
        if succ and id not in cls.values:
            cls.values[id] = formatted
        # return id

    @classmethod
    def dump(cls):
        for row in cls.values.values():
            print(row)

    @classmethod
    def dump_file(cls, path):
        dump_file('%s/%s.csv' % (path, cls.__name__), cls.headers, cls.values.values())
    # with open('%s/%s.csv' % (path, cls.__name__), 'w') as f:
    #     writer = csv.writer(f)
    #     writer.writerow(['ID', 'VALOR_REEMBOLSADO', 'DOCUMENTO_DESPESA', 'DETALHAMENTO_DESPESA',
    #                      'FK_DM_DT_LANCAMENTO', 'FK_DM_DT_CUSTO', 'FK_DM_SENADOR',
    #                      'FK_DM_FORNECEDOR', 'FK_DM_TIPO_DESP'])
    #     writer.writerows(cls.values.values())

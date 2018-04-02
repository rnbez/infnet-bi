from tables.dump_file import dump_file


class DM_DT_LANCAMENTO(object):
    headers = ['ID',
               'ANO',
               'MES',
               'ANO_MES',
               'TRIMESTRE',
               'SEMESTRE',
               'ANO_TRIMESTRE',
               'ANO_SEMESTRE']
    values = {}

    @classmethod
    def format(cls, _ano, _mes):
        ano = int(_ano)
        if ano < 2015 or ano > 2018:
            print('DISCARDING: DM_DT_LANCAMENTO %s/%s' % (_ano, _mes))
            return False, None, None
        mes = int(_mes)
        id = '%d_%02d' % (ano, mes)
        ano_mes = id
        trimestre = int((mes - 1) / 3) + 1
        semestre = int((mes - 1) / 6) + 1
        ano_trimestre = '%d_%d' % (ano, trimestre)
        ano_semestre = '%d_%d' % (ano, semestre)
        return True, id, [id, ano, mes, ano_mes, trimestre, semestre, ano_trimestre, ano_semestre]

    @classmethod
    def add(cls, ano, mes):
        succ, id, formatted = cls.format(ano, mes)
        if succ and id not in cls.values:
            cls.values[id] = formatted
        return id

    @classmethod
    def dump(cls):
        for row in cls.values.values():
            print(row)

    @classmethod
    def dump_file(cls, path):
        dump_file('%s/%s.csv' % (path, cls.__name__), cls.headers, cls.values.values())
        # with open('%s/%s.csv' % (path, cls.__name__), 'w') as f:
        #     writer = csv.writer(f)
        #     writer.writerow(['ID', 'ANO', 'MES', 'ANO_MES', 'TRIMESTRE',
        #                      'SEMESTRE', 'ANO_TRIMESTRE', 'ANO_SEMESTRE'])
        #     writer.writerows(cls.values.values())

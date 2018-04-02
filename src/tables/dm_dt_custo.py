from tables.dump_file import dump_file


class DM_DT_CUSTO(object):
    headers = ['ID',
               'ANO',
               'MES',
               'DIA',
               'DATA',
               'ANO_MES',
               'MES_DIA',
               'TRIMESTRE',
               'SEMESTRE',
               'ANO_TRIMESTRE',
               'ANO_SEMESTRE']
    values = {}

    @classmethod
    def format(cls, _data):
        _dia, _mes, _ano = _data.split('/')
        # print(_dia, _mes, _ano)
        ano = int(_ano)
        if ano < 2015 or ano > 2018:
            print('DISCARDING: DM_DT_CUSTO %s' % _data)
            return False, None, None
        mes = int(_mes)
        dia = int(_dia)
        id = '%d_%02d_%02d' % (ano, mes, dia)
        data = '%d_%02d_%02d' % (ano, mes, dia)
        ano_mes = '%d_%02d' % (ano, mes)
        mes_dia = '%02d_%02d' % (mes, dia)
        trimestre = int((mes - 1) / 3) + 1
        semestre = int((mes - 1) / 6) + 1
        ano_trimestre = '%d_%d' % (ano, trimestre)
        ano_semestre = '%d_%d' % (ano, semestre)
        return True, id, [id, ano, mes, dia,
                          data, ano_mes, mes_dia,
                          trimestre, semestre, ano_trimestre, ano_semestre]

    @classmethod
    def add(cls, data):
        # print(data)
        succ, id, formatted = cls.format(data)
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
        #     writer.writerow(['ID', 'ANO', 'MES', 'DIA', 'DATA', 'ANO_MES', 'MES_DIA',
        #                      'TRIMESTRE', 'SEMESTRE', 'ANO_TRIMESTRE', 'ANO_SEMESTRE'])
        #     writer.writerows(cls.values.values())

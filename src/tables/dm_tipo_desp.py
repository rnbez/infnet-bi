from tables.dump_file import dump_file


class DM_TIPO_DESP(object):
    headers = ['ID',
               'TIPO_DESPESA']
    values = {}

    @classmethod
    def format(cls, tipo_despesa):
        if not tipo_despesa:
            print('DISCARDING: DM_TIPO_DESP')
            return False, None, None
        id = len(cls.values.keys()) + 1
        nome_tipo_despesa = tipo_despesa
        return True, id, [id, nome_tipo_despesa]

    @classmethod
    def add(cls, tipo_despesa):
        succ, id, formatted = cls.format(tipo_despesa)
        key = tipo_despesa.replace(' ', '_').lower()
        if succ and key not in cls.values:
            cls.values[key] = formatted
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
        #     writer.writerow(['ID', 'TIPO_DESPESA'])
        #     writer.writerows(cls.values.values())

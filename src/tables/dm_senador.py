from tables.dump_file import dump_file


class DM_SENADOR(object):
    headers = ['ID_DM_SENADOR',
               'NOME_SENADOR']
    values = {}

    @classmethod
    def format(cls, senador):
        if not senador:
            print('DISCARDING: DM_SENADOR')
            return False, None, None
        id = len(cls.values.keys()) + 1
        nome_senador = senador
        return True, id, [id, nome_senador]

    @classmethod
    def add(cls, senador):
        succ, id, formatted = cls.format(senador)
        key = senador.replace(' ', '_').lower()
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
        #     writer.writerow(['ID', 'NOME_SENADOR'])
        #     writer.writerows(cls.values.values())

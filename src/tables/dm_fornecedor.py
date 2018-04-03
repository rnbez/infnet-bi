from tables.dump_file import dump_file


class DM_FORNECEDOR(object):
    headers = ['ID_DM_FORNECEDOR',
               'CNPJ_CPF_FORNECEDOR',
               'NOME_FORNECEDOR']
    values = {}

    @classmethod
    def format(cls, fornecedor, cnpj_cpf):
        if not fornecedor:
            print('DISCARDING: DM_FORNECEDOR')
            return False, None, None
        id = len(cls.values.keys()) + 1
        nome_fornecedor = fornecedor
        cnpj_cpf_fornecedor = cnpj_cpf
        return True, id, [id, cnpj_cpf_fornecedor, nome_fornecedor]

    @classmethod
    def add(cls, fornecedor, cnpj_cpf):
        succ, id, formatted = cls.format(fornecedor, cnpj_cpf)
        if not succ:
            return None
        key = cnpj_cpf
        if key in cls.values:
            return cls.values[key][0]
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
        #     writer.writerow(['ID', 'CNPJ_CPF_FORNECEDOR', 'NOME_FORNECEDOR'])
        #     writer.writerows(cls.values.values())

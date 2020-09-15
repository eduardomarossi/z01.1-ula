import sys
from random import randrange
from ula import compute_ula, convert_output

VERSION = '1.1.0'


class UlaTerminal:
    ula_fields = ['x', 'y', 'zx', 'nx', 'zy', 'ny', 'f', 'no']

    def __init__(self):
        self.data = {}
        for k in UlaTerminal.ula_fields:
            self.data[k] = randrange(0, 2)
        self.data['x'] = randrange(0, 2**16)
        self.data['y'] = randrange(0, 2**16)

    def print_ula_vals(self):
        print('======-- ULA --======')
        for k in UlaTerminal.ula_fields:
            print('{0:s}: {1:b}'.format(k, self.data[k]))
        print('\n')
        result = compute_ula(**self.data)
        print('======-- Output --======')
        print('zr: {}  ng: {}  out: {}'.format(result[0], result[1], convert_output(result[2])))
        print('')

    def ask(self):
        campo = ''
        valor = None

        while campo not in UlaTerminal.ula_fields:
            campo = input('Digite nome do campo para alterar valor ou S para sair: ')
            if campo.strip() == 'S':
                sys.exit(0)

        while valor is None:
            try:
                valor = input('Digite um valor para o campo: ')

                if campo not in ['x', 'y'] and (valor not in ['0', '1']):
                    valor = None
                    raise Exception('Valor deve ser 0 ou 1')
                elif campo in ['x', 'y']:
                    try:
                        int(valor, 2)
                    except:
                        valor = None
                        raise Exception('Valor de X e Y deve ser binário')

            except Exception as e:
                print(e)

        self.data[campo] = int(valor, 2)

if __name__ == '__main__':
    print('z01.1-ula terminal - v' + VERSION)
    ula = UlaTerminal()
    while True:
        ula.print_ula_vals()
        ula.ask()



# Instalando
pip3 install pycep-correios

print('=============================================================')
print('============Olá! Seja bem vindo ao busca de CEP==============')
print('=============================================================')
print('\n')
print('\n')
cep = input('Digite um CEP:')

# importando
from pycep_correios import get_address_from_cep, WebService

# Consumindo

cep = input('Digite um CEP:')

try:
    address = get_address_from_cep(cep, webservice=WebService.APICEP)

    print('========= Resultado =========')
    print(address['logradouro'])
    print(address['complemento'])
    print(address['bairro'])
    print(address['cep'])
    print(address['cidade'])
    print(address['uf'])
    print('============================')

except:
    print('Algo de errado aconteceu')


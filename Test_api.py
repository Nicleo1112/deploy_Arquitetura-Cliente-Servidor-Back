import urllib.request
import urllib.parse
import json

BASE = 'https://livraria-api-btc4e6eucreuctae.eastus-01.azurewebsites.net'

def teste_status():
    res = urllib.request.urlopen(f'{BASE}/')
    data = json.loads(res.read())
    assert 'status' in data
    print('✅ Status:', data['status'])

def teste_listar_livros():
    res = urllib.request.urlopen(f'{BASE}/api/livros')
    livros = json.loads(res.read())
    assert len(livros) > 0
    print(f'✅ Listar: {len(livros)} livros retornados')

def teste_filtrar_por_titulo():
    titulo = urllib.parse.quote('Harry Potter')
    res = urllib.request.urlopen(f'{BASE}/api/livros?titulo={titulo}')
    livros = json.loads(res.read())
    assert len(livros) == 2
    print(f'✅ Filtro por título: {len(livros)} livros encontrados')

def teste_adicionar_livro():
    dados = json.dumps({"titulo": "Livro Teste", "autor": "Autor Teste", "ano": 2024}).encode()
    req = urllib.request.Request(
        f'{BASE}/api/livros',
        data=dados,
        headers={'Content-Type': 'application/json'},
        method='POST'
    )
    res = urllib.request.urlopen(req)
    data = json.loads(res.read())
    assert 'mensagem' in data
    print('✅ Adicionar:', data['mensagem'])

def teste_remover_livro():
    titulo = urllib.parse.quote('Livro Teste')
    req = urllib.request.Request(
        f'{BASE}/api/livros/{titulo}',
        method='DELETE'
    )
    res = urllib.request.urlopen(req)
    data = json.loads(res.read())
    assert 'mensagem' in data
    print('✅ Remover:', data['mensagem'])

if __name__ == '__main__':
    print('🔍 Testando API...\n')
    teste_status()
    teste_listar_livros()
    teste_filtrar_por_titulo()
    teste_adicionar_livro()
    teste_remover_livro()
    print('\n✅ Todos os testes passaram!')

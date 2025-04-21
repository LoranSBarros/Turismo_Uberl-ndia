from django.shortcuts import render

# Create your views here.

pontos_turisticos = [[
    {'nome': 'Parque do Sabiá'},
    {'desc': 'O Parque do Sabiá é um parque municipal e zoológico localizado na Zona Leste de Uberlândia, Minas Gerais. Conta com 1,8 milhão de metros quadrados e está localizado entre os bairros Tibery e Santa Mônica, possuindo portarias de acesso por ambas as regiões.'},
    {'imagem': 'Parque do Sabiá.png'}

],
[
    {'nome': 'Parque Siquierolli'},
    {'desc': 'O Parque Municipal Victorio Siquierolli está localizado na Zona Norte de Uberlândia, onde encontram-se legítimos exemplos da vegetação do cerrado, com suas árvores de folhas coreáceas, troncos retorcidos e cascudos, flores muitos coloridas e frutos agrestes, um espaço com brinquedos pra crianças, museu de biodiversidade do cerrado. '},
    {'imagem': 'Parque Siquierolli.jpg'}
],
[
    {'nome': 'Cachoeira Sucupira'},
    {'desc': 'A Cachoeira do Sucupira é um dos pontos turísticos mais procurados para curtir o verão na cidade mineira. Então, se você está pesquisando o que fazer em Uberlândia nos dias mais quentes e gosta de curtir um off-road, mesclar esse passeio ao roteiro urbano será o match perfeito. '},
    {'imagem': 'Cachoeira Sucupira.jpg'}
   
],
[
    {'titulo': 'Uberlândia'},
    {'intro': 'Já pensou em visitar Uberlândia? Atualmente a segunda maior cidade do maior cidade do segundo maior estado do Brasil! Faremos uma breve introdução de alguns dos pontos turisticos da Cidade, caso esteja pensando em nos visitar <3'},
    {'imagem': 'Uberlândia.jpg'}
]
]


def sabia(request):
    return render(request, 'turismo/uberlandia.html',{
        'nome': pontos_turisticos[0][0]['nome'],
        'descrição': pontos_turisticos[0][1]['desc'],
        'imagem': pontos_turisticos[0][2]['imagem']
    })

def siquierolli(request):
    return render(request, 'turismo/uberlandia.html',{
        'nome': pontos_turisticos[1][0]['nome'],
        'descrição': pontos_turisticos[1][1]['desc'],
        'imagem': pontos_turisticos[1][2]['imagem']
    })

def sucupira(request):
    return render(request, 'turismo/uberlandia.html',{
        'nome': pontos_turisticos[2][0]['nome'],
        'descrição': pontos_turisticos[2][1]['desc'],
        'imagem': pontos_turisticos[2][2]['imagem']
    })


def intro(request):
    return render(request, 'turismo/uberlandia.html',{
        'nome': pontos_turisticos[3][0]['titulo'],
        'descrição': pontos_turisticos[3][1]['intro'],
        'imagem': pontos_turisticos[3][2]['imagem']
    })


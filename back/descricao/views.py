from django.shortcuts import render

from random import choice, sample
from math import floor

lista = {
    'Águia': 'Ave que voa muito alto e caça outro animais para se alimentar',
    'Cachorro': 'Um animal que pode viver com pessoas e late',
    'Gato': 'Um animal que gosta de fazer carinho e miar',
    'Lobo': 'Um animal que parece cachorro e uiva nas noites de lua cheia',
    'Coruja': 'Uma ave que faz poo e gosta de sair a noite',
    'Baleia': 'Um animal que vive no mar e é muito grande, já engoliu o Pinóquio',
    'Girafa': 'Um animal que tem um pescoço bem grande',
    'Elefante': 'Um animal bem grande, mas que tem medo de rato e gosta de amendoim',
    'Jacaré': 'Um lagarto bem grande que fica nos rios e, quando vai caçar, coloca os olhos para fora d\'água',
    'Rato': 'Um roedor bem pequeno que gosta de comer queijo',
    'Tigre': 'Um animal de cor laranja e preto que parece um gato bem grande',
    'Formiga': 'Um inseto bem pequeno e trabalhador',
    'Tubarão': 'Um animal que mora no mar e caça outros peixes, ele tem muitos dentes bem afiados',
    'Leão': 'Ele é o rei da selva',
    'Foca': 'Um animal que vive na água e gosta de bricar com bola',
    'Barata': 'Um inseto grande e nojento que gosta de esgoto',
    'Abelha': 'Um inseto que voa e tem ferrão, faz mel',
    'Mosquito': 'Um inseto que gosta de pertubar o sono das pessoas e picar, a pícada fica coçando',
    'Sapo': 'Um animal que vive na lagoa, gosta de comer insetos e não lava o pé',
    'Cobra': 'Um animal que não tem patas, vive rastejando, todos têm medo da sua mordida',
    'Aranha': 'Um animal que faz sua casa com teia',
    'Galinha': 'Um animal que passa o dia ciscando o chão e botando ovos',
    'Vaca': 'Um animal muito conhecido por seu leite',
    'Porco': 'Um animal que vive na lama e come lavagem'
}

listaAnim = list(lista.keys())


def animais(request):
    acertou = None
    pessoal = None
    qnt_erros = 0
    acertos = 0
    total = 0

    if request.method == 'POST':
        if 'descricoes' in request.session:
            correto = request.session['descricoes'][0]
            qnt_erros = request.session['descricoes'][1]
            acertos = request.session['descricoes'][2]
            total = request.session['descricoes'][3]
            del (request.session['descricoes'])
        else:
            correto = None
            acertos = 0
            total = 0

        total += 1

        pessoal = str(request.POST['resposta'])

        if pessoal == correto:
            acertou = 1
            qnt_erros = 0
            acertos += 1
        else:
            acertou = 0
            qnt_erros += 1
    elif 'descricoes' in request.session:
        del (request.session['descricoes'])

    lanim = sample(listaAnim, 5)
    correto = choice(lanim)
    desc = lista[correto]

    request.session['descricoes'] = [correto, qnt_erros, acertos, total]

    perc = floor(acertos / total * 100) if total > 0 else '-'
    
    return render(
        request, 'descricao.html',
        {
            'desc': desc,
            'lanim': lanim,
            'acertou': acertou,
            'pessoal': pessoal,
            'perc': perc,
            'total': total
        }
    )
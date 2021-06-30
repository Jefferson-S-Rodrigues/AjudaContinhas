from django.shortcuts import render

from random import randint, choice
from math import floor


def continhas(request):
    trocar = True
    acertou = None
    pessoal = None
    resto = None
    qnt_erros = 0
    acertos = 0
    total = 0

    if request.method == 'POST':
        if 'contas' in request.session:
            a = request.session['contas'][0]
            b = request.session['contas'][1]
            o = request.session['contas'][2]
            qnt_erros = request.session['contas'][3]
            acertos = request.session['contas'][4]
            total = request.session['contas'][5]
            del (request.session['contas'])
        else:
            a = None
            b = None
            o = None
            acertos = 0
            total = 0

        total += 1

        if o == 0:
            r = a * b
            res = 0
        else:
            r = floor(a / b)
            res = a % b

        pessoal = int(request.POST['resposta'])
        resto = int(request.POST.get('resto', 0))

        if pessoal == r and (o == 0 or resto == res):
            trocar = True
            acertou = 1
            qnt_erros = 0
            acertos += 1
        else:
            trocar = False
            acertou = 0
            qnt_erros += 1
    elif 'contas' in request.session:
        del (request.session['contas'])

    if trocar or qnt_erros > 3:
        o = randint(0, 1)
        if o == 0:
            a = randint(1000, 10000)
            b = randint(0, 1000)
        else:
            a = randint(1000, 10000)
            b = randint(1, 12)

    request.session['contas'] = [a, b, o, qnt_erros, acertos, total]

    perc = floor(acertos / total * 100) if total > 0 else '-'

    return render(
        request, 'continhas.html',
        {
            'a': a,
            'b': b,
            'o': o,
            'acertou': acertou,
            'pessoal': pessoal,
            'resto': resto,
            'perc': perc,
            'total': total
        }
    )

def continhasB(request):
    trocar = True
    acertou = None
    pessoal = None
    qnt_erros = 0
    acertos = 0
    total = 0

    if request.method == 'POST':
        if 'contasB' in request.session:
            expressao = request.session['contasB'][0]
            qnt_erros = request.session['contasB'][1]
            acertos = request.session['contasB'][2]
            total = request.session['contasB'][3]
            del (request.session['contasB'])
        else:
            expressao = None
            acertos = 0
            total = 0

        total += 1

        r = eval(expressao)

        pessoal = int(request.POST['resposta'])

        if pessoal == r:
            trocar = True
            acertou = 1
            qnt_erros = 0
            acertos += 1
        else:
            trocar = False
            acertou = 0
            qnt_erros += 1
    elif 'contasB' in request.session:
        del (request.session['contasB'])

    if trocar or qnt_erros > 3:
        l = 1
        m = 20
        contas = ['+','-','*','+','*']
        ff = randint(0, 1)
        expressao = str(randint(l, m))
        expressao += choice(contas)
        expressao += str(randint(l, m))
        expressao += choice(contas)
        expressao += str(randint(l, m))
        expressao += choice(contas)
        expressao += str(randint(l, m))
        if ff > 0:
            expressao += choice(contas)
            expressao += str(randint(l, m))


    request.session['contasB'] = [expressao, qnt_erros, acertos, total]

    perc = floor(acertos / total * 100) if total > 0 else '-'

    return render(
        request, 'continhasB.html',
        {
            'expressao': expressao.replace('*', 'x'),
            'acertou': acertou,
            'pessoal': pessoal,
            'perc': perc,
            'total': total
        }
    )

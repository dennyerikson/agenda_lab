from django.template.loader import render_to_string
from django.core.mail import send_mail
from datetime import datetime



def send_email(data):
    emails = ['tifat@anhanguera.com']

    if data['email']:
        emails.append(data['email'])

    hora = datetime.now().hour
    msg = ''
    if hora >= 6 and hora < 12:
        msg = 'Bom dia,'
    elif hora >= 12 and hora < 18:
        msg = 'Boa tarde,'
    else:
        msg = 'Boa noite,'


    data = {'lab': data['lab'], 'course':data['course'], 'name':data['name'],
        'period':data['period'], 'details':data['details'], 'unidade':data['unidade'],
        'create_date':data['create_date'], 'msg':msg, 'email':data['email']
    }

    plain_text = render_to_string('blog/emails/novo_agendamento.txt', data)
    html_email = render_to_string('blog/emails/novo_agendamento.html', data)
    
    send_mail(
        'TIFAT - AGENDAMENTO DOS LABORATÓRIOS', # assunto
        plain_text, # mensagem
        'denny.monteiro@anhanguera.com', #to
        emails, #from
        html_message=html_email,
        fail_silently=False,
    )
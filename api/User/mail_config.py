from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from datetime import datetime
from django.shortcuts import get_object_or_404

def sendResetPasswordEmail(email, password, user):
    """
    Envoyer un email contenant un nouveau mot de passe à l'utilisateur
    """
    subject = 'Vos identifiants'
    recipient_list = [email]
    context = {'password': password, 'email': email, 'subject':subject, 'user': user}
    html_message = render_to_string('email_template.html', context)
    plain_message = strip_tags(html_message)
    from_email = settings.EMAIL_HOST_USER
    send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message)
__author__ = 'mengmeng'
#coding=UTF-8

from settings import *
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, Http404
from forms import ContactForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError,mail_admins,EmailMultiAlternatives
from threading import Thread




def index(request):
    return render_to_response('index.html', {},
                              context_instance=RequestContext(request))

def about(request):

    return render_to_response('contact/about.html', {
    }, context_instance=RequestContext(request,{

        }))

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject=cd['subject']
            message=cd['message']
            from_email=cd.get('from_email', 'noreply@example.com')
            sender=EMAIL_HOST_USER
            try:
                send_mail(subject,[from_email,message],sender,
                          ['poohmeng@sina.com'], fail_silently=False)

                thread = Thread(target=send_mail,args=(subject,message,from_email,['poohmeng@sina.com']))
                thread.start()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('/thanks/')

    else:
        form = ContactForm(
            initial = {'subject':'I love this one!'}
        )
    c = {}
    c = RequestContext(request, {
        'form':form,
        })
    return render_to_response('contact/contact.html',c)


def thanks(request):
    return render_to_response('contact/thanks.html', {
    }, context_instance=RequestContext(request))





#DJANGO Imports
from json import load
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import redirect, render

#Internationalization and Translations
from django.utils import translation

#CORE Models
from core import models

def context_maker (request, context):
    context['SupportedLanguages'] = models.SupportedLanguage.get_languages()

    try:
        context['language'] = models.SupportedLanguage.objects.get(languageKey=translation.get_language())
    except models.SupportedLanguage.DoesNotExist:
        context['language'] = models.SupportedLanguage.objects.first()

    context['ApplicationSettings'] = models.ApplicationSetting.load_settings(language=context['language'])
    return context

def template_loader(request, context, load_template):
#    try:
        context['segment'] = load_template
        print ("Loading... " + load_template)

        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))

#    except template.TemplateDoesNotExist:
#        print ("Template not found at: " + load_template)

#        html_template = loader.get_template('core/errors/page-404.html')
#        return HttpResponse(html_template.render(context, request))

#    except:
#        html_template = loader.get_template('core/errors/page-500.html')
#        return HttpResponse(html_template.render(context, request))


def togglelanguage(request, language_id):
    language = models.SupportedLanguage.objects.get(pk=language_id)

    translation.activate(language.languageKey)
    print("REFERRER: " + request.META.get('HTTP_REFERER'))
    return redirect(request.META.get('HTTP_REFERER'))

def companyprofile(request):
    context = context_maker(request, {})
    return template_loader(request, context, 'core/companyprofile.html')

def editcompanyprofile(request):
    context = context_maker(request, {})
    return template_loader(request, context, 'core/edit_companyprofile.html')

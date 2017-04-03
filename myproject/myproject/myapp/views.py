# -*- coding: utf-8 -*-
import requests
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse

from myproject.myapp.models import Document
from myproject.myapp.forms import DocumentForm

from keystoneauth1 import loading
from keystoneauth1 import session
from heatclient import client

AUTH_TOKEN = ""


def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(user=request.POST['user'], docfile=request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('list'))
    else:
        form = DocumentForm()  # A empty, unbound form

    # _get_token()
    # Load documents for the list page
    documents = {}
    documents_db = Document.objects.all()

    for document in documents_db:
        if documents.has_key(document.user):
            documents[document.user].append(document)
        else:
            documents[document.user] = [document]

    # Render list page with the documents and the form
    return render(
        request,
        'list.html',
        {'documents': documents, 'form': form}
    )


def build(request, user):
    # Recuperar arquivos do usuário
    files = Document.objects.filter(user=user)

    # criar instancia Heat
    # loader = loading.get_plugin_loader('password')
    # auth = loader.load_from_options(auth_url=AUTH_URL,
    # username = USERNAME,
    # password = PASSWORD,
    # project_id = PROJECT_ID)
    # sess = session.Session(auth=auth)
    # heat = client.Client('1', session=sess)


    # heat.stacks.list()

    # enviar arquivos para a instancia

    # executar a aplicacao

    # exibir ip da instancia

    return HttpResponse("building")


def list_stacks(request):
    # Handle file upload

    #
    #
    #
    #
    # curl  -H 'X-Auth-Token: gAAAAABY4kZZKo_2qOESqoEj6GOG2YpT1jzfkkIh1Cr9QiwriRLyTSF4DLEn8XqNRMpyO-RMZAkANyPjgJsx3mmI-3jCXIYL1VaG61q8J71Pnj3dPRJT1nWOgBBXB1ekMElaNsuR46W49teS1BQci2E393W3jApMnUS4odes9j4qZG9I8hljqOU'
    #
    #
    #
    #
    #
    #
    #
    _get_token()

    header = {
        'X-Auth-Token': AUTH_TOKEN,
    }

    r = requests.get('http://172.29.236.100:8004/v1/default/stacks', headers=header)
    print r.text


    # Render list page with the documents and the form
    return HttpResponse({"listagem feita"})


def _get_token():
    header = {
        "Content-Type": "application/json",
    }

    payload = {
        "auth":
            {"identity":
                 {"methods":
                      ["password"],
                  "password": {
                      "user": {"domain":
                                   {"name": "Default"},
                               "name": "admin",
                               "password": "f55597e72a9b8eba7e3dc90891e6484349918499a698e2dc3eb26"}}},
             "scope":
                 {"project":
                      {"domain":
                           {"name": "Default"},
                       "name": "admin"}
                  }
             }
    }
    r = requests.post('https://10.11.4.100:5000/v3/auth/tokens', data=payload, verify=False)
    print 'header: ', r.headers
    if 'X-Subject-Token' in r.headers:
        AUTH_TOKEN = r.headers['X-Subject-Token']
        print AUTH_TOKEN
    else:
        print "sem token"
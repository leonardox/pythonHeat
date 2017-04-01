# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse

from myproject.myapp.models import Document
from myproject.myapp.forms import DocumentForm

from keystoneauth1 import loading
from keystoneauth1 import session
from heatclient import client


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





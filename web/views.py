from django.shortcuts import render
from web.models import Candidato, IdeaFuerza, Cita, Documento, Noticia

# Create your views here.
def index(request):
    ideasfuerza_m = IdeaFuerza.objects.filter(seccion='m').order_by('orden')
    m_columns = 0
    if len(ideasfuerza_m) > 0:
        m_columns = 12 / len(ideasfuerza_m)
    ideasfuerza_p = IdeaFuerza.objects.filter(seccion='p').order_by('orden')
    p_columns = 0
    if len(ideasfuerza_p) > 0:
        p_columns = 12 / len(ideasfuerza_p)
    ideasfuerza_a = IdeaFuerza.objects.filter(seccion='a').order_by('orden')
    a_columns = 0
    if len(ideasfuerza_a) > 0:
        a_columns = 12 / len(ideasfuerza_a)
    citas = Cita.objects.order_by('orden')
    candidatos = Candidato.objects.order_by('orden')
    documentos = Documento.objects.order_by('orden')
    noticias = Noticia.objects.order_by('-fecha')
    return render(request, 'index.html', {
        'ideasfuerza_m': ideasfuerza_m,
        'm_columns': m_columns,
        'ideasfuerza_p': ideasfuerza_p,
        'p_columns': p_columns,
        'ideasfuerza_a': ideasfuerza_a,
        'a_columns': a_columns,
        'citas': citas,
        'candidatos': candidatos,
        'documentos': documentos,
        'noticias': noticias,
    })
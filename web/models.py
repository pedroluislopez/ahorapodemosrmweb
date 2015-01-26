# -*- encoding: utf-8 -*-

from django.db import models

# Create your models here.
class Candidato(models.Model):
    nombre = models.CharField('Nombre', max_length=50)
    apellidos  = models.CharField('Apellidos', max_length=50)
    imagen = models.ImageField('Imagen', upload_to='profile_images', blank=True)
    secretario = models.BooleanField('Secretario General', default=False)
    consejo = models.BooleanField('Consejo Ciudadano', default=False)
    descripcion_corta = models.CharField('Descripción corta', max_length=100)
    motivacion = models.TextField('Motivación', max_length=1000, blank=True)
    orden = models.IntegerField('Orden')
    podemos = models.CharField('Perfil de Podemos', max_length=255, blank=True, default='')
    blog = models.CharField('Blog', max_length=255, blank=True, default='')
    facebook = models.CharField('Facebook', max_length=255, blank=True, default='')
    twitter = models.CharField('Twitter', max_length=255, blank=True, default='')
    youtube = models.CharField('Youtube', max_length=255, blank=True, default='')
    
    def __unicode__(self):
        return self.nombre + ' ' + self.apellidos
    
    def get_imagen(self):
        if not self.imagen:
            return 'http://placehold.it/200x200'
        return self.imagen.url
    
    def get_candidatura(self):
        if self.secretario:
            return 'Secretaría general'
        elif self.consejo:
            return 'Consejo ciudadano'
        else:
            return ''
    
class IdeaFuerza(models.Model):
    SECCION_CHOICES = (
        ('m', 'Método'),
        ('p', 'Podemos Murcia'),
        ('a', 'Ayuntamiento'),
    )
    
    titulo = models.CharField('Título', max_length=50)
    seccion = models.CharField('Sección', max_length=2, choices=SECCION_CHOICES)
    icono = models.CharField('Icono', max_length=20)
    descripcion = models.TextField('Descripción', max_length=500)
    orden = models.IntegerField('Orden')
    
    def __unicode__(self):
        return self.seccion + ': ' + self.titulo
    
class Cita(models.Model):
    candidato = models.ForeignKey(Candidato)
    cita = models.TextField('Cita', max_length=500)
    orden = models.IntegerField('Orden')
    
    def __unicode__(self):
        return u'%s %d' % (self.candidato, self.orden)
    
class Documento(models.Model):
    CATEGORIA_CHOICES = (
        ('d', 'Documento'),
        ('o', 'Octavilla'),
        ('s', 'Sin categoría')
    )
    
    nombre = models.CharField('Nombre', max_length=50)
    categoria = models.CharField('Categoría', max_length=2, choices=CATEGORIA_CHOICES)
    imagen =  models.ImageField('Imagen', upload_to='document_images')
    documento = models.FileField('Documento', upload_to='document_documents', blank=True)
    orden = models.IntegerField('Orden')
    
    def __unicode__(self):
        return self.nombre
    
    def get_documento(self):
        if not self.documento:
            return self.imagen.url
        return self.documento.url
    
class Noticia(models.Model):
    titular = models.CharField('Titular', max_length=255)
    resumen = models.TextField('Resumen', max_length=1000)
    enlace = models.CharField('Enlace', max_length=255)
    diario = models.CharField('Diario', max_length=50)
    fecha = models.DateField('Fecha')
    
    def __unicode__(self):
        return self.diario + ': ' + self.titular
    
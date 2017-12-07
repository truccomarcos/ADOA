class Patron(models.Model):
    titulo = RichTextField()
    descripcion = RichTextField()
    problemas = RichTextField()
    solucion = RichTextField()
    def get_contenidos(self):
        contenidos = []
        for contenido in self.contenidopatron_set.all():
            contenidos.append(Contenido(titulo = contenido.titulo, descripcion = contenido.descripcion, orden = contenido.orden))
        return contenidos
    def __unicode__(self):
       return self.titulo

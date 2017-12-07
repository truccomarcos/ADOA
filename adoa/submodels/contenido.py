class Contenido(models.Model):
    orden = models.IntegerField()
    titulo = RichTextField()
    descripcion = RichTextField()
    contenido = RichTextField()
    objetoAprendizaje = models.ForeignKey(ObjetoAprendizaje)
    def __unicode__(self):
       return self.titulo
       

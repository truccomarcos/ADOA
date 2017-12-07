class ObjetoAprendizaje(models.Model):
    titulo = RichTextField()
    descripcion = RichTextField()
    patron = models.ForeignKey(Patron)
    user = models.ForeignKey(User)
    def __unicode__(self):
       return self.titulo

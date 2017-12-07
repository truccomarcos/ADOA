class ContenidoPatron(models.Model):
    orden = models.IntegerField()
    titulo = RichTextField()
    descripcion = RichTextField()
    patron = models.ForeignKey(Patron)

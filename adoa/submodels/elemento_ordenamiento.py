class ElementoOrdenamiento(models.Model):
    enunciado = RichTextField()
    orden = models.IntegerField()
    actividad = models.ForeignKey(Actividad, null=True)

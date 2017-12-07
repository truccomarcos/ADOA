class ElementoAsosiacion(models.Model):
    enunciado = RichTextField()
    imagen = models.ImageField()
    actividad = models.ForeignKey(Actividad, null=True)

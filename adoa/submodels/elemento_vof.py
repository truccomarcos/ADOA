class ElementoVoF(models.Model):
    enunciado = RichTextField()
    verdad = models.BooleanField()
    actividad = models.ForeignKey(Actividad, null=True)

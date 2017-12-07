class ElementoIdentificacion(models.Model):
    enunciado = RichTextField()
    correcto = models.BooleanField()
    actividad = models.ForeignKey(Actividad, null=True)

class Actividad(models.Model):
    enunciado = RichTextField()
    tipo = models.CharField(max_length=1, choices=ACTIVIDAD_TYPE_CHOICES, null=True)
    objetoAprendizaje = models.ForeignKey(ObjetoAprendizaje)
    def __unicode__(self):
       return self.titulo

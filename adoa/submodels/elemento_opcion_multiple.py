class ElementoOpcionMultiple(models.Model):
    enunciado = RichTextField()
    correcta = RichTextField()
    incorrecta1 = RichTextField()
    incorrecta2 = RichTextField()
    incorrecta3 = RichTextField()
    actividad = models.ForeignKey(Actividad, null=True)

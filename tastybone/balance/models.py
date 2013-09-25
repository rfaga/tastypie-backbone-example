# coding: UTF-8

from django.db import models

# Create your models here.
class Operation(models.Model):
    description = models.TextField(verbose_name="Descrição da operação", null=True)
    value = models.DecimalField(u'Valor', max_digits=19, decimal_places=2, null=True)
    date = models.DateField(verbose_name="Data", null=True)

    class Meta:
        verbose_name = "Operação"
        
    def __unicode__(self):
        return "%10.2f (%s)" % (self.value, self.description)

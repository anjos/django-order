#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Thu Apr 15 10:00:30 CEST 2010

"""Models for our DB entries
"""

from django.db import models
from django.utils.translation import ugettext_lazy as _

class OrderedModel(models.Model):
    """
    An abstract model that allows objects to be ordered relative to each other.
    Provides an ``order`` field.
    """
    
    order = models.PositiveIntegerField(_(u'Order'), editable=False)
    
    class Meta:
        abstract = True
        ordering = ('order',)
    
    def save(self, *args, **kwargs):
        if not self.id:
            qs = self.__class__.objects.order_by('-order')
            try:
                self.order = qs[0].order + 1
            except IndexError:
                self.order = 0
        super(OrderedModel, self).save(*args, **kwargs)
    
    def _move(self, up):
        qs = self.__class__._default_manager
        if up:
            qs = qs.order_by('-order').filter(order__lt=self.order)
        else:
            qs = qs.order_by('order').filter(order__gt=self.order)
        try:
            replacement = qs[0]
        except IndexError:
            # already first/last
            return
        self.order, replacement.order = replacement.order, self.order
        self.save()
        replacement.save()
    
    def move_down(self):
        """
        Move this object down one position.
        """
        return self._move(up=False)
    
    def move_up(self):
        """
        Move this object up one position.
        """
        return self._move(up=True)

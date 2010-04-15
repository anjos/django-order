#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Thu Apr 15 10:02:19 CEST 2010

"""Adminstrative models for our DB entries
"""

from django.contrib import admin
from django.contrib.admin.util import unquote
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.utils.functional import update_wrapper
from django.utils.translation import ugettext, ugettext_lazy
from django.conf import settings

class OrderedModelAdmin(admin.ModelAdmin):

  ordering = ['order',]

  def get_urls(self):
    from django.conf.urls.defaults import patterns, url
    def wrap(view):
        def wrapper(*args, **kwargs):
            return self.admin_site.admin_view(view)(*args, **kwargs)
        return update_wrapper(wrapper, view)
    info = self.model._meta.app_label, self.model._meta.module_name
    return patterns('',
        url(r'^(.+)/move-(up)/$',
            wrap(self.move_view),
            name='%s_%s_move_up' % info),
        url(r'^(.+)/move-(down)/$',
            wrap(self.move_view),
            name='%s_%s_move_down' % info),
    ) + super(OrderedModelAdmin, self).get_urls()
      
  def move_view(self, request, object_id, direction):
    obj = get_object_or_404(self.model, pk=unquote(object_id))
    if direction == 'up':
        obj.move_up()
    else:
        obj.move_down()
    return HttpResponseRedirect('../../')
  
  def move_up_down_links(self, obj):
    return '<a href="../../%(app_label)s/%(module_name)s/%(object_id)s/move-up/"title="%(up)s"><img width="16" height="16" src="%(MEDIA_URL)sorder/img/go-up.png" alt="%(up)s" /></a><nobr/><a href="../../%(app_label)s/%(module_name)s/%(object_id)s/move-down/" title="%(down)s"><img width="16" height="16" src="%(MEDIA_URL)sorder/img/go-down.png" alt="%(down)s" /></a>' % {
        'MEDIA_URL': settings.MEDIA_URL,
        'app_label': self.model._meta.app_label,
        'module_name': self.model._meta.module_name,
        'object_id': obj.id,
        'up': ugettext(u'Move up'),
        'down': ugettext(u'Move down'),
    }
  move_up_down_links.allow_tags = True
  move_up_down_links.short_description = ugettext_lazy('Move')
  

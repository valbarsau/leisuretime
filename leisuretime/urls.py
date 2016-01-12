from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'leisuretime.views.home', name='home'),
    # url(r'^leisuretime/', include('leisuretime.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^$',"principal.views.index"),
    url(r'^user/registrar/', "principal.views.registrar"),
url(r'^user/entrar/', "principal.views.entrar"),
url(r'^libros/user/listarpuntuados/', "principal.views.libros_usuario"),
url(r'^libros/user/listarnopunt/', "principal.views.libros_no_puntuados"),
url(r'^user/salir/', "principal.views.cierre_sesion"),
url(r'^libro/info/(?P<id_libro>\d+)$', "principal.views.info"),
url(r'^libros/recomienda/$', "principal.views.recomienda"),
url(r'^libros/todos/$', "principal.views.listar"),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
url(r'libro/user/puntuar/(?P<id_libro>\d+)$',"principal.views.puntuar"),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

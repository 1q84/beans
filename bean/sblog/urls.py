from django.conf.urls.defaults import *
urlpatterns = patterns('sblog.views',
   (r"^$", "main"),
   (r"^(\d+)/$", "post"),
   (r"^add_comment/(\d+)/$", "add_comment"),
    (r"^month/(\d+)/(\d+)/$", "month"),
)
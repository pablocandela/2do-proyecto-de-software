from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from aplicacion import views, errorViews

urlpatterns = [
    url(r'^users/$', views.UserList.as_view()),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^index/$', views.index, name='index'),
    url(r'^crearClase/$', views.crearClase, name='crearClase'),
    url(r'^course/$', views.CourseList.as_view()),
    url(r'^course/(?P<pk>\d+)$', views.CourseDetailView.as_view(template_name='course-detail.html'), name='course-detail'),
    #url(r'^users/(?P<format>[a-z0-9]+)/$', views.UserDetail.as_view()),
    url(r'^user/(?P<pk>\d+)$', views.UserDetailView.as_view(template_name='user-detail.html'), name='user-detail'),
    #url(r'^take/(?P[0-9]+)/$', views.TakeList.as_view()),
    url(r'^tomados/$', views.TakeList.as_view()),
    url(r'^', errorViews.noEncontrado),

]

urlpatterns = format_suffix_patterns(urlpatterns)

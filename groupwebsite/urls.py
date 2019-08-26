from django.urls import path
from . import views
urlpatterns = [
               path('professor/',views.Professor, name = "Prof"),
               path('people/',views.Type, name = "People"),
               path('photos/',views.Ourphotos,name = "Photos"),
               path('<int:id>',views.news_detail,name = "new"),
               path('news/',views.news_list,name= "news"),
               path('publication/',views.publications_list,name = "publication"),
               path('research',views.research, name="research"),
               path('contact/',views.contact,name='contact'),
               path('search/',views.search,name='search')
               ]
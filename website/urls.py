from django.urls import path
from . import views

urlpatterns = [path('<int:id>',views.article_detail,name = "detail"),
               path('type/<int:blog_type_pk>', views.blogs_with_type, name="blogs_with_type"),
               path('articles/',views.article_list,name= "article_list"),
               path('publication/',views.publication_list,name = "publication_list"),
               path('member/',views.member_list, name = "member_list"),
               path('research',views.research, name="research"),
               ]
from django.urls import path
from app import views

urlpatterns = [
    path('form/', views.form),
    path('',views.data),
    path('alldata',views.alldata),
    #path('softdelete/<int:tid>',views.softdelete),
    path('update/<int:tid>', views.update),
    path('delete/<int:tid>', views.delete),
    path('htol/', views.htol),
    path('ltoh/', views.ltoh),
    path('AtoZ/', views.AtoZ),
    path('ZtoA/', views.ZtoA),
    path('catfilter/<str:cat>',views.catfilter),
    path('logout/', views.userlogout),
    #path('',views.data)
#second authentication by form.py
    path('register/',views.registerPage),
    #path('login2/',views.loginPage),


]

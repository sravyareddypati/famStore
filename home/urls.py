from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name='home'),
    path("about",views.about,name='about'),
    path("contact",views.contact,name='contact'),
    path("shop",views.shop,name='shop'),
    path("shop/tracker/",views.tracker,name='tracker'),
    path('shop/products/<int:myid>',views.prodView,name="ProductView"),
    path("shop/checkout/",views.checkout,name="Checkout"),
    path("shop/search/",views.search,name="search"),
    
]
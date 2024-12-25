from django.urls import path
from task5.views import main_page, shop, shopping_cart, sign_up_by_django, news

urlpatterns = [
        path('', main_page),
        path('games/', shop),
        path('cart/', shopping_cart),
        path('regdj/', sign_up_by_django),
        path('news/', news)
]
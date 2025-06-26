from django.urls import path
from food.views import index, item, detail

app_name = 'food'
urlpatterns = [
    # 'food/'
    path('', index, name='index'),
    # 'food/1'
    path('<int:item_id>/', detail, name='detail'),
    path('item', item, name='item'),
]

from django.urls import path
from food.views import index, item, detail, create_item, update_item, delete_item, IndexClassView, FoodDetail, CreateItem

app_name = 'food'
urlpatterns = [
    # 'food/'
    path('', IndexClassView.as_view(), name='index'),
    # 'food/1'
    path('<int:pk>/', FoodDetail.as_view(), name='detail'),
    path('item', item, name='item'),
    # add item
    path('add/', CreateItem.as_view(), name='create_item'),
    # update
    path('update/<int:item_id>/', update_item, name='update_item'),
    # delete
    path('delete/<int:item_id>/', delete_item, name='delete_item'),
]

from django.urls import include, path
from main.views import create_product_flutter, show_main
from main.views import show_main, create_product
from main.views import show_main, create_product, show_xml 
from main.views import show_main, create_product, show_xml, show_json
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id 
from main.views import register
from main.views import login_user
from main.views import logout_user
from main.views import add_stock
from main.views import reduce_stock
from main.views import add_stock
from main.views import delete_product
from main.views import edit_product
from main.views import delete_product
from main.views import get_product_json
from main.views import create_ajax

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('add_stock/<int:id>/', add_stock, name='add_stock'),
    path('reduce-stock/<int:id>/', reduce_stock, name='reduce_stock'),
    path('delete-product/<int:id>/', delete_product, name='delete_product'),
    path('edit-product/<int:id>', edit_product, name='edit_product'),
    # path('delete/<int:id>', delete_product, name='delete_product'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-ajax/', create_ajax, name='create_ajax'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
]
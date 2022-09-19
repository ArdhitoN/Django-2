from django.urls import path
from .views import show_html
from .views import show_xml 
from .views import show_json
from .views import show_html
from .views import show_json_by_id 
from .views import show_xml_by_id 

app_name = 'mywatchlist'

urlpatterns = [
    path('', show_html, name='show_html'),
    path('xml/', show_xml, name= 'show_xml'),
    path('json/', show_json, name='show_json'),
    path('html/', show_html, name='show_html'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
]

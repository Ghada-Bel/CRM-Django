from django.urls import path
from .views import general_sales_graph, specific_sales_graph

urlpatterns = [
    path('general-sales/', general_sales_graph, name='general_sales_graph'),
    path('specific-sales/<int:company_id>/', specific_sales_graph, name='specific_sales_graph'),
]
from django.urls import path
from . import views

urlpatterns = [
    path("graph/",views.graph,name="totalviews"),
    path("table/",views.table,name="tableview"),
]

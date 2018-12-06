from django.urls import path
from . import views 

urlpatterns = [
    path('api/system135/', views.Systemlens135List.as_view() ),
    path('api/systemMedium/', views.SystemlensMediumList.as_view()),
    path('api/components/', views.ComponentList.as_view()),
    path('api/formulas/', views.FormulaList.as_view()),
]
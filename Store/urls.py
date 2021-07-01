from django.urls import path
from .views import MerchandiseView, AutoView

urlpatterns = [
    path('merch/', MerchandiseView.as_view()),
    path('merch/<merch_id>/', MerchandiseView.as_view()),
    path('auto/', AutoView.as_view()),
    path('auto/<auto_id>/', AutoView.as_view()),
]
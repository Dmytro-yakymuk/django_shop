from django.urls import path

from . import views

urlpatterns = [
    path('', views.ProductView.as_view(), name="home"),
    path('shop/', views.ProductListView.as_view(), name="product_list"),
    path('filter/', views.ProductFilterView.as_view(), name="product_filter"),
    path('search/', views.SearchListView.as_view(), name="search"),
    path('add-rating/', views.AddStarRating.as_view(), name="add_rating"),
    path('json-filter/', views.JsonProductFilterView.as_view(), name="product_filter_json"),
    path('<slug:slug>/', views.ProductDetailView.as_view(), name="product_detail"),
    path('review/<int:pk>', views.AddReview.as_view(), name="add_review"),
]




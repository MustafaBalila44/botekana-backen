from django.urls import path

from . import views


urlpatterns = [
    path("", views.ProductListView.as_view(), name="product-list"),
    path("<int:pk>/", views.ProductEditView.as_view(), name="product-detail"),
    path("has_discount/", views.DiscountedProductListView.as_view(),
         name="discountedproducts-list"),
    path("categories/", views.CategoryListView.as_view(),
         name="category-list"),
    path("categories/<int:pk>/", views.CategoryEditView.as_view(),
         name="category-detail"),
    path("sub-categories/", views.SubCategoryListView.as_view(),
         name="subcategory-list"),
    path("sub-categories/<int:pk>/",
         views.SubCategoryEditView.as_view(), name="subcategory-detail"),
    path("brands/", views.BrandListView.as_view(), name="brand-list"),
    path("brands/<int:pk>/", views.BrandEditView.as_view(),
         name="brand-detail"),
    path("discounts/", views.DiscountListView.as_view(), name="discount-list"),
    path("discounts/<int:pk>/", views.DiscountEditView.as_view(),
         name="discount-detail"),
]

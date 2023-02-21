from django.urls import path
from customer import views


urlpatterns=[
    path("register/",views.SignUpView.as_view(),name="signup"),
    path("login",views.SignInView.as_view(),name="signin"),
    path("home/",views.IndexView.as_view(),name="home"),
    path("products/<int:id>",views.ProductDetailView.as_view(),name="product-detail"),
    path("products/<int:id>/carts/add",views.AddToCartView.as_view(),name="cart-add"),
    path("customer/carts/all",views.CartListView.as_view(),name="cart-list"),
    path("carts/<int:id>/change",views.CartRemoveView.as_view(),name="cart-change"),
    path("orders/add/<int:id>/",views.MakeOrderView.as_view(),name="create-order"),
    path("orders/all",views.MyorderView.as_view(),name="placed-order"),
    path("orders/cancelled/<int:id>",views.OrderCancelView.as_view(),name="order-cancelled"),
    path("discount",views.DiscountProductsView.as_view(),name="offers"),
    path("reviews/<int:id>/add",views.ReviewView.as_view(),name="review-add"),
    path("logout",views.signout_view,name="signout")
]
from django.urls import path
from customer import views
urlpatterns=[
    path("home",views.CustomerHome.as_view(),name="custhome"),
    # path("carts",views.view_my_cart,name="cart"),
    # path("orders",views.view_my_orders,name="order"),
    # path("feedback",views.FeedbackView.as_view(),name="feedback"),
    # path("accounts/signup",views.RegistrationView.as_view(),name="signup"),
    # path("login",views.LoginView.as_view(),name="login"),
    path("account/signup",views.SignUpView.as_view(),name="signup"),
    path("account/signin",views.SignInView.as_view(),name="signin"),
    path("account/signout",views.sign_out,name="signout"),
    path("carts/add/<int:id>",views.AddToCart.as_view(),name="addtocart"),
    path("carts/items",views.CartItems.as_view(),name="cartitems"),
    path("carts/items/remove/<int:id>",views.RemoveCartItem.as_view(),name="removeitem"),
    path("carts/orders/add/<int:id>/<int:c_id>",views.OrderCreate.as_view(),name="ordercreate"),
    path("orders",views.MyOrderView.as_view(),name="myorders"),
    path("orders/cancel/<int:id>",views.cancel_order,name="cancelorder"),
    path("profile/add",views.ProfileView.as_view(),name="cust_profile"),
    path("view/profile",views.ViewMyProfile.as_view(),name="viewprofile")

]
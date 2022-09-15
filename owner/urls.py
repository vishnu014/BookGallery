from django.urls import path
from owner import views
urlpatterns=[
    path("books/all",views.Booklist.as_view(),name="listbook"),
    # path('home',views.index),
    path("books/add",views.Addbook.as_view(),name="addbook"),
    # path('remove',views.book_remove),
    # path("books",views.book_list),
    path('books/<int:id>',views.BookDetail.as_view(),name="bookdetail"),
    path("books/change/<int:id>",views.BookChange.as_view(),name="bookedit"),
    path("books/remove/<int:id>",views.BookDelete.as_view(),name="bookdelete"),
    path("dashboard",views.OwnerDashboard.as_view(),name="dashboard"),
    path("orders.<int:o_id>",views.OrderDetails.as_view(),name="orderdetail"),
    path("orders/process/<int:id>",views.OrderProcessView.as_view(),name="orderprocess"),

]

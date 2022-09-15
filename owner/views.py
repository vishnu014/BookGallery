from django.shortcuts import render,HttpResponse,redirect
from django.views.generic import View,ListView,DetailView,CreateView,UpdateView,DeleteView
from owner.models import books,Books
from owner.forms import BookForm,OrderProcessForm
from django.urls import reverse_lazy
from customer.decorators import owner_permission_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from customer.models import Orders
from django.core.mail import send_mail




# Create your views here.
# def index(request):
#     return HttpResponse("<h1> welcome to owner  index  </h1>")

# def book_add(request):
#     return HttpResponse("<h1> Add books </h1>")
# def book_remove(request):
#     return HttpResponse("<h1> Delete books</h1>")

@method_decorator(owner_permission_required,name="dispatch")
class Booklist(ListView):
    model = Books
    context_object_name="books"
    template_name = "book_list.html"


    # def get(self,request,*args,**kwargs):
    #     books=Books.objects.all()
    #     context={"books":books}


        # return render(request,"book_list.html",context)
@method_decorator(owner_permission_required,name="dispatch")
class Addbook(CreateView):
    model = Books
    form_class = BookForm
    template_name = "book_add.html"
    success_url = reverse_lazy("listbook")

    # def get(self,request,*args,**kwargs):
    #     form=BookForm()
    #
    #     return render(request,"book_add.html",{"form":form})
    # def post(self,request,*args,**kwargs):
    #     # bookname=request.POST["bk_name"]
    #     # authorname=request.POST["bk_author"]
    #     # price=request.POST["bk_price"]
    #     # copies=request.POST["bk_copies"]
    #     form=BookForm(request.POST,files=request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request,"book has been added")
    #         # book_name=form.cleaned_data.get("book_name")
    #         # author=form.cleaned_data.get("author_name")
    #         # price=form.cleaned_data.get("price")
    #         # copies=form.cleaned_data.get("copies")
    #         # bookadd=Books(book_name=book_name,author_name=author,price=price,copies=copies)
    #         # bookadd.save()
    #         return redirect("addbook")
    #     else:
    #         context={'form':form}
    #         messages.error( request,"book adding failed")
    #         return render(request,"book_add.html",context)



@method_decorator(owner_permission_required,name="dispatch")
class BookDetail(DetailView):
    model = Books
    context_object_name = "book"
    template_name = "book_details.html"
    pk_url_kwarg = "id"

    # def get(self,request,*args,**kwargs):
    #     id=kwargs["id"]
    #     book=Books.objects.get(id=id)
    #     context={"book":book}
    #     return render(request,"book_details.html",context)

@method_decorator(owner_permission_required,name="dispatch")
class BookChange(UpdateView):
    model = Books
    template_name = "book_edit.html"
    form_class = BookForm
    pk_url_kwarg = "id"
    success_url = reverse_lazy("listbook")
    # def get(self,request,*args,**kwargs):
    #     print(kwargs)
    #     id=kwargs["id"]
    #     book=Books.objects.get(id=id)
    #
    #     # form=BookForm(initial={"book_name":book["book_name"],"author":book["author"],"price":book["price"],"copies":book["copies"]})
    #     form=BookForm(instance=book)
    #     return render(request,"book_edit.html",{"form":form})
    # def post(self,request,*args,**kwargs):
    #     id=kwargs["id"]
    #     book=Books.objects.get(id=id)
    #     form=BookForm(request.POST,instance=book,files=request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("listbook")
@method_decorator(owner_permission_required,name="dispatch")
class BookDelete(DeleteView):
    template_name="book_delete.html"
    pk_url_kwarg = "id"
    success_url = reverse_lazy("listbook")
    model = Books

    # def get(self,request,*args,**kwargs):
    #     id=kwargs["id"]
    #     book=Books.objects.get(id=id)
    #     book.delete()
    #     return redirect("listbook")

class OwnerDashboard(ListView):
    model = Orders
    template_name = "owner_dashboard.html"

    def get(self,request,*args,**kwargs):
        new_orders=self.model.objects.filter(status="orderplaced")

        context={"n_orders":new_orders}
        return render(request,self.template_name,context)

class OrderDetails(DetailView):
    model = Orders
    template_name = "order_detail.html"
    context_object_name = "order"
    pk_url_kwarg = "o_id"

class OrderProcessView(UpdateView):
    model=Orders
    pk_url_kwarg = "id"
    template_name = "order_process.html"
    form_class = OrderProcessForm
    success_url = reverse_lazy("dashboard")

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        expected_date=form.cleaned_data.get("expected_delivery_date")
        send_mail(
            'Book Order Confirmation',
            'Your order will be delivered on'+str(expected_date),
            'vishnuprabhakar014@gmail.com',
            ['sanoopsahadevan99@gmail.com'],
            fail_silently=False,
        )
        return super().form_valid(form)




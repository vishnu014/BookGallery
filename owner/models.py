from django.db import models

# Create your models here.
books=[
    {"id": 100,"book_name":"randamoozham","author":"mt","price":480,"copies":250},
    {"id":101,"book_name":"aarachar","author":"meera","price":580,"copies":250},
    {"id":102,"book_name":"the alchemist","author":"paulo","price":780,"copies":250},
    {"id":103,"book_name":"rainrising","author":"nirupama","price":1000,"copies":250},
    {"id":104,"book_name":"indulekha","author":"chandhu menon","price":280,"copies":250},
]

class Books(models.Model):
    book_name=models.CharField(max_length=120,unique=True)
    author_name=models.CharField(max_length=120)
    price=models.PositiveIntegerField(default=50)
    copies=models.PositiveIntegerField(default=10)
    active_status=models.BooleanField(default=True)
    image=models.ImageField(upload_to="images",null=True,blank=True)

    def __str__(self):
        return self.book_name


# orm qureies
# print all book details available under 600
# books=Books.objects.filter(price__lt=600)

# print all book details available in range 400-600
# books=Books.objects.filter(price__=400,price__lt=600)

# print details of book induleka
# books=Books.objects.get(id=5)

# print books whose copies>30 and their count
# books=Books.objects.filter(copies__gt=30).count()

# print inactives books only
# booknames=books=Books.objects.filter(active_status=False).values("book_name")

# create new application location
# create a model districts with fields (district name, first dose vaccination rate,second dose vaccinations rate)
from django.db import models

class Brand(models.Model):
    brand_name = models.CharField(max_length=40)
    slug = models.SlugField(max_length=40, null=True, blank=True, unique=True)

    def __str__(self):
        return self.brand_name

class Car(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.FloatField()
    brand_name = models.ForeignKey(Brand, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.name

class Comment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.name}"
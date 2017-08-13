from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone


class User(models.Model):
    username = models.CharField(max_length=21)
    password = models.CharField(max_length=26)
    name = models.CharField(max_length=100)
    degree = models.CharField(max_length=100, blank=True, help_text='Leave blank if personnel/faculty')
    office = models.CharField(max_length=100, blank=True, help_text='Leave blank if student')

    def get_absolute_url(self):
        return reverse('home:homepage', kwargs={'pk': self.pk})

    def __str__(self):
        return self.username

item_Type = (
    ('Academic Use', 'Academic Use'),
    ('Office Use', 'Office Use'),
)


class Item(models.Model):
    userName = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(primary_key=True, max_length=300)
    photo = models.FileField()
    quantity = models.PositiveIntegerField(default=1)
    condition = models.CharField(max_length=200)
    itemType = models.CharField(max_length=100, choices=item_Type, default='Academic Use')
    courseName = models.CharField(max_length=100, blank=True, help_text='Leave blank if Office Use')
    pub_date = models.DateTimeField('date published')

    # def choice(self):
    #     if self.

    def get_absolute_url(self):
        return reverse('home:homepage', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Tags(models.Model):
    name = models.ForeignKey(Item, on_delete=models.CASCADE)
    tag = models.CharField(max_length=100)
    
    def __str__(self):
        return self.tag

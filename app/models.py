from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from taggit.managers import TaggableManager

# Create your models here.

# class Tag(models.Model):
#    name = models.CharField(max_length=200, null=True)
#
#    def __str__(self):
#        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    about = models.TextField(max_length=150, null=True, blank=True)
    website = models.CharField(max_length=50, null=True, blank=True)
    github = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True)
    image = models.ImageField(default="default.png", null=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)

class Bench(models.Model):
    CATEGORY = (
        ('Picnic Bench', 'Picnic Bench'),
        ('Park Bench', 'Park Bench'),
        ('Picnicspot', 'Picnicspot'),
        ('Picnic Area', 'Picnic Area'),
    )

    CONDITION = (
        ('Spiffing', 'Spiffing'),
        ('Okay', 'Okay'),
        ('Apalling', 'Appalling'),
        ('Not There', 'Not There'),
    )

    CAPACITY = (
        ('1-2', '1-2'),
        ('3-5', '3-5'),
        ('6-10', '6-10'),
        ('10+', '10+'),
    )

    name = models.CharField(max_length=30, null=True)
    description = models.TextField(max_length=350, null=True, blank=True)
    # location = 
    image = models.ImageField(default="default.png", null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    category = models.CharField(max_length=30, null=True, choices=CATEGORY)
    condition = models.CharField(max_length=30, null=True, choices=CONDITION)
    # tag = TaggableManager(blank=True)
    capacity = models.CharField(max_length=30, null=True, choices=CAPACITY)

    class Meta:
        ordering = ['date_created']

class Comments(models.Model):
    bench = models.ForeignKey(Bench, on_delete=models.CASCADE, related_name='comments')
    name = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

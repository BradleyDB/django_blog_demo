from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class BlogPost(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    text = models.TextField()
    #defaults to the TIME_ZONE in settings.py
    created_date = models.DateTimeField(default=timezone.now)
    #published date can be blank, can save to drafts
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comment(self):
        return self.comments.filter(approved_comments=True)

    def get_absolute_url(self):
        #they will be sent to the published blog post once published
        return reverse("blogpost_detail",kwargs={'pk':self.pk})


    def __str__(self):
        return self.title

class BlogComment(models.Model):
    post = models.ForeignKey('blog.BlogPost',related_name='comments',on_delete=models.CASCADE)
    author = models.CharField(max_length=75)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    #should match approved_comments above
    approved_comments = models.BooleanField(default=False)

    def approve(self):
        self.approved_comments = True
        self.save()

    def get_absolute_url(self):
        #will go to the list of blogs after making comment (since comments need
        #super user approval)
        return reverse('blogpost_list')

    def __str__(self):
        return self.text

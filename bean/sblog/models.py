from django.db.models import *
from django.contrib.auth.models import User
from django.contrib import admin
from django.core.mail import send_mail

notify = False

class Post(Model):
    title = CharField(max_length=60)
    body = TextField()
    created = DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]

    def __unicode__(self):
        return self.title

class Comment(Model):
    author = CharField(max_length=60, blank=True)
    body = TextField()
    post = ForeignKey(Post,related_name="comments", blank=True, null=True)
    created = DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u"%s: %s"%(self.post,self.body[:60])

    def save(self, *args, **kwargs):
        if notify:
            tpl = "Comment was added to '%s' by '%s':\n\n%s"
            message = tpl%(self.post,self.author,self.body)
            from_address = "ericsu1988@gmail.com"
            recipient_list=["myemail@gmail.com"]
            send_mail("New comment added",message,from_address,recipient_list)
        super(Comment,self).save(*args,**kwargs)

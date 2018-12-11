from django.db import models
from django.urls import reverse
from django.utils.text import  slugify
# Create your models here.


class Post(models.Model):
    # user =models.ForeignKey('auth.User')
    title=models.CharField(max_length=120)
    content=models.TextField()
    publising_date=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(null=True,blank=True)
    slug=models.SlugField(unique=True,editable=False,max_length=130)



    def __str__(self):
        return self.title



    def get_absolute_url(self):
        return reverse('post:detail', kwargs={'slug': self.slug})
        #return "/post/{}".format(self.id)

    # def get_create_url(self):
    #     return reverse('post:create')
    #
    # def get_update_url(self):
    #     return reverse('post:update', kwargs={id: self.id})
    #
    # def get_delete_url(self):
    #     return reverse('post:delete', kwargs={id:self.id})


    def get_unique_slug(self):
        slug=slugify(self.title.replace('ı','i'))
        unique_slug=slug
        counter=1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug='{}-{}'.format(slug,counter)
            counter+=1
            return unique_slug


    def save(self, *args, **kwargs):
        # self.slug=slugify(self.title.replace('ı','i'))
        self.slug=self.get_unique_slug()
        return super(Post,self).save(*args,**kwargs)



    class Meta:
        ordering=['-publising_date']

    class Comment(models.Model):

        post=models.ForeignKey('post.Post',related_name='comments',on_delete=models.CASCADE())

        name=models.CharField(max_length=120,verbose_name='Name')
        content =models.TextField(verbose_name="Commnet")

        created_date=models.DateTimeField(auto_now_add=True)
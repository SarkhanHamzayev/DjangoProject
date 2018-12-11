from django.contrib import admin
from .models import Post
#from post.models import Post


class PostAdmin(admin.ModelAdmin):

    list_display = ['title','content','publising_date','slug']
    list_display_links = ['title','content','publising_date']
    list_filter = ['publising_date']
    search_fields = ['title','content']
    # prepopulated_fields = {'slug','title',}

    class Meta:
        model =Post




admin.site.register(Post,PostAdmin)
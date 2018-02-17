#views are used to conect models and template
from django.shortcuts import render #In the render function we have one parameter request (everything we receive from the user via the Internet)
from django.utils import timezone
from .models import Post #to include the model we have written in models.py

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') # published blog posts sorted by published_date
    return render(request, 'blog/post_list.html', {'posts': posts}) #last parameter, {}, is a place in which we can add some things for the template to use

#a variable for our QuerySet: posts. Treat this as the name of our QuerySet. 
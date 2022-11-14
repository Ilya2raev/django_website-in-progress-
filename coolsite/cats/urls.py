from django.urls import path, re_path

from .views import *

urlpatterns = [
	path('', index, name='home'),
	path('about/', about, name='about'),
	path('addcontent/', add_content, name='add_content'),
	path('contact/', feedback, name='feedback'),
	path('login/', login, name='login'),
	path('post/<slug:post_slug>/', show_post, name='post'),
	path('category/<int:category_id>/', show_category, name='category')
]
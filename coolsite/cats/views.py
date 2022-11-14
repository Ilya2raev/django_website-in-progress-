from django.http import HttpResponse, HttpResponseNotFound, Http404	
from django.shortcuts import render, redirect, get_object_or_404

from .forms import *
from .models import *

menu = [{'title':'О сайте', 'url_name': 'about'},
		{'title':'Добавить контент', 'url_name': 'add_content'},
		{'title':'Обратная связь', 'url_name': 'feedback'},
		{'title':'Войти', 'url_name': 'login'}
]

def index(request):
	posts = Cats.objects.all()

	context = {'posts':posts,
			   'menu': menu,
			   'title': 'Главная страница',
			   'category_selected': 0,
	}

	return render(request, 'cats/index.html', context=context)

def add_content(request):
	if request.method == 'POST':
		form = AddContentForm(request.POST, request.FILES)
		if form.is_valid():
			# print(form.cleaned_data)
			form.save()
			return redirect('home')

	else:
		form = AddContentForm
	return render(request, 'cats/addcontent.html', {'form': form, 'menu': menu, 'title': 'Добавление контента'})

def feedback(request):
	return HttpResponse('Обратная связь')

def login(request):
	return HttpResponse('Авторизация')

def about(request):
	return render(request, 'cats/about.html', {'menu': menu, 'title': 'О сайте'})

def show_post(request, post_slug):
	post = get_object_or_404(Cats, slug=post_slug)

	context = {'post':post,
			   'menu': menu,
			   'title': post.title,
			   'category_selected': post.category_id,
	}
	return render(request, 'cats/post.html', context=context)

def pageNotFound(request, exception):
	return HttpResponseNotFound('<h1>Ошибка 404</h1>')

def show_category(request, category_id):
	posts = Cats.objects.filter(category_id=category_id)

	if len(posts) == 0:
		raise Http404()
	context = {'posts':posts,
			   'menu': menu,
			   'title': 'Котики',
			   'category_selected': 0,
	}

	return render(request, 'cats/index.html', context=context)
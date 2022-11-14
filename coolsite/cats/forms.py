from django import forms
from django.core.exceptions import ValidationError

from .models import *

class AddContentForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['category'].empty_label = 'Выберите категорию'
	class Meta:
		model = Cats
		fields = ['title', 'slug', 'content', 'photo', 'is_published', 'category']
		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-input'}),
			'content': forms.Textarea(attrs={'cols': 60, 'rows': 10})
		}

	def clean_title(self):
		title = self.cleaned_data['title']
		if len(title) > 200:
			raise ValidationError('Длина заголовка превышает 200 символов')

		return title
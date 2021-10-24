from django import forms
# from .models import Category   # для несвязанных форм
from .models import News        # # для связанных форм


# class NewsForm(forms.Form):
#     title = forms.CharField(max_length=150, label='Название', widget=forms.TextInput(attrs={"class":"form-control"}))
#     content = forms.CharField(label='Текст', widget=forms.Textarea(attrs={
#         "class":"form-control",
#         "rows": 5
#     }))
#     is_published = forms.BooleanField(label='Опубликовано', initial=True)
#     category = forms.ModelChoiceField(label='Категория', empty_label="Выберите категорию", queryset=Category.objects.all(),
#                                       widget=forms.Select(attrs={"class":"form-control"}))


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        # fields = '__all__'
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }

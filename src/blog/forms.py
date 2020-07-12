from django import (forms)
from .models import BlogPost

class BlogPostForm(forms.Form):
    title = forms.CharField()
    slug = forms.CharField()
    content = forms.CharField(widget = forms.Textarea)

class BlogPostModelForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'slug', 'content', 'publish_date']

    def clean_title(self, *args, **kwargs):
        # for updating a blog
        instance = self.instance

        # new blog
        title = self.cleaned_data.get('title')
        qs = BlogPost.objects.filter(title = title)

        #updating a blog
        if instance is not None:
            qs = qs.exclude(pk = instance.pk)
        # new blog
        if qs.exists():
            raise forms.ValidationError("Title already used.")
        return title

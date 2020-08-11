from django import forms
from .models import BlogPost, BlogComment


class BlogPostForm(forms.ModelForm):

    class Meta():
        model = BlogPost
        fields = ('author','title','text')

        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea blogpostcontent'}),
        }


class BlogCommentForm(forms.ModelForm):

    class Meta():
        model = BlogComment
        fields = ('author','text')

        #how to connect widgets to styling
        widgets = {
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'}),
        }

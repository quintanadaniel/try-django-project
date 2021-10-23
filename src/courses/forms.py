from django import forms

from courses.models import Course


class CourseModelForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            'title',
            'description',
            'credit'
        ]

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title.lower() == 'abc':
            raise forms.ValidationError('This is not valid title')
        return title

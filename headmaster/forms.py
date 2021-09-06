from django import forms


class CourseAddForm(forms.Form):
    course = forms.CharField(label="course", max_length=120)


class AddBatchForm(forms.Form):
    batch_name = forms.CharField(label="batch name", max_length=120)
    starting_date = forms.IntegerField(label="starting_date")
    course_name = forms.CharField(label="course name", max_length=120)


    def clean(self):
        pass



from django import forms

from main_app.models import Question_text
from main_app.models import Answer_text

# class QuestionTextForm(forms.ModelForm):
#     class Meta:
#         model = Question_text
#         fields = ['content',]

class AnswerTextForm(forms.ModelForm):
    class Meta:
        model = Answer_text
        fields = ['question_id','content']
        
class QuestionTextForm(forms.Form):
    content = forms.CharField(label='質問')



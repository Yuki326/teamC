from django.shortcuts import render
from django.http import HttpResponse
from main_app.forms import QuestionTextForm
from main_app.forms import AnswerTextForm
from django.shortcuts import redirect
from main_app.models import Question_text
from main_app.models import Answer_text


# Create your views here.
def index(request):
  if(request.method == 'POST'):
    content = request.POST['content']
    item = Question_text(content=content) 
    item.save()
    return redirect(to = 'index')
  params={
    'form':QuestionTextForm(),
    'data':Question_text.objects.all()
  }
  return render(request,'index.html',params)

def answer(request):
  if(request.method == 'POST'):
    obj=Answer_text()
    item = AnswerTextForm(request.POST,instance=obj) 
    item.save()
    return redirect(to = 'answer')
  params={
    'form':AnswerTextForm(),
    'data':Answer_text.objects.all(),
    'dataQ':Question_text.objects.all()
  }
  return render(request,'answer.html',params)
  
def createQuestionText(request):
  if(request.method == 'POST'):
      item = QuestionTextForm(request.POST)
      item.save()
      return redirect(to = '')

  return render(request,'index.html')

def save_text_answers(request):
    questions = Question_text.objects.all()
    for i in questions:
      if 'answer'+str(i.id) in request.GET:
        answer = request.GET['answer'+str(i.id)]
        question = Question_text.objects.get(id=i.id)
        obj=Answer_text(question_id=question,content=answer)
        obj.save()
    # subject=Subject.objects.get(id=subject_id)
    # #todo 開始日と締め切り日の要素を後で追加する
    # obj = Task(subject_id=subject,name=name,author = request.user,start=start)
    # obj.save()
    return HttpResponse('Hellooooo')
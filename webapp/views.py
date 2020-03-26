from django.shortcuts import get_object_or_404, render

# Create your views here.
def index(request):
    #context = {'latest_question_list': latest_question_list}
    return render(request, 'webapp/index.html') #shortcut

def login(request):
    #question = get_object_or_404(Question, pk=question_id)
    return render(request, 'webapp/login.html', {'variable': "value"})

def logout(request):
    #question = get_object_or_404(Question, pk=question_id)
    return render(request, 'webapp/logout.html', {'variable': "value"})

def signup(request):
    return render(request, 'webapp/signup.html', {'variable': "value"})

def about(request):
    return render(request, 'webapp/about.html', {'variable': "value"})

def faq(request):
    return render(request, 'webapp/faq.html',    {'variable': "value"})

def boards(request):
    return render(request, 'webapp/boards.html', {'variable': "value"})

def detail(request):
    return render(request, 'webapp/detail.html', {'variable': "value"})

def terms(request):
    return render(request, 'webapp/terms.html',  {'variable': "value"})

def policy(request):
    return render(request, 'webapp/policy.html', {'variable': "value"})

def forgot(request):
    return render(request, 'webapp/forgot.html', {'variable': "value"})





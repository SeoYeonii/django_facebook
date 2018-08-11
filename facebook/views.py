from django.shortcuts import render
from facebook.models import Article, Comment
# Create your views here.
def play(request):
    return render(request, 'play.html')

count = 0
def play2(request):
    jangseoyeon = "장서연"
    age = 20

    global count
    count = count +1
    
    if age > 19:
        status = '성인'
    else:
        status = '청소년'

    diary = ['오늘은 날씨가 맑았다. - 4월 3일', '미세먼지가 너무 심하다. (4월 2일)', '비가 온다. 4월 1일에 작성']

    return render(request, 'play2.html', {'name':jangseoyeon, 'cnt':count, 'age':status, 'diary': diary})

def profile(request):
    adr1 = 'http://127.0.0.1:8000/play'
    adr2 = 'http://127.0.0.1:8000/play2'
    return render(request, 'profile.html',{'adr1':adr1, 'adr2':adr2 })

def event(request):
    jangseoyeon = "장서연"
    age = 20

    global count
    count = count + 1

    if age > 19:
        status = '성인'
    else:
        status = '청소년'

    return render(request, 'event.html', {'name': jangseoyeon,
                                          'cnt': count,
                                          'age': status})


def fail(request):
    return render(request, 'fail.html')

def help(request):
    return render(request, 'help.html')

def warn(request):
    return render(request, 'warn.html')

def newsfeed(request):
    articles = Article.objects.all()
    return render(request, 'newsfeed.html', {'articles':articles})

def detail_feed(request, number):
    article = Article.objects.get(pk=number)

    if request.method == 'POST':
        Comment.objects.create(
            article=article,
            author=request.POST["nickname"],
            text=request.POST["reply"],
            password=request.POST["password"]
        )
    return render(request, 'detail_feed.html', {'feed':article})

def new_feed(request):

    if request.method == 'POST':
        content = request.POST['content'] + ' 추신'
        Article.objects.create(
            author=request.POST['author'],
            password=request.POST['password'],
            title=request.POST['title'],
            text=content
        )

    return render(request, 'new_feed.html')


def edit_feed(request, number):
    article = Article.objects.get(pk=number)

    if request.method == 'POST':
        article.author = request.POST['author']
        article.title = request.POST['title']
        article.text = request.POST['content']
        article.save()

    return render(request, 'edit_feed.html', {'feed': article})


def remove_feed(request, number):
    article = Article.objects.get(pk=number)

    if request.method == 'POST':
        if article.password == request.POST['password']:
            article.delete()

    return render(request, 'remove_feed.html', {'feed': article})
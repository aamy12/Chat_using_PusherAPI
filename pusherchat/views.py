#render library for returning views to the browser
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from pusher import Pusher

pusher = Pusher(app_id=u'511250', key=u'84ed998cf1f276710378', secret=u'fe1332f9e0bf759924f6')


# Create your views here.
@login_required(login_url='/admin/login/')
def chat(request):
    return render(request, "chat.html")


@csrf_exempt
def broadcast(request):
    pusher.trigger(u'a_channel', u'an_event', {u'name': request.user.username, u'message': request.POST['message']})
    return HttpResponse("done")
# Create your views here.
from masterpiece.models import piece, entry
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def home(request):
	hepsi=piece.objects.all()
	return render_to_response('index.html', {'all_pieces' : hepsi}, context_instance=RequestContext(request))
	

def word(request, the_word):
	the_piece = get_object_or_404(piece, word=the_word)
	if request.method == 'POST':
		newEntry = request.POST.get('yeni',None)
		if newEntry:
			entry.objects.create(content=newEntry, word=the_piece, username=User.objects.get(username="kullanici1"))
	the_entry = entry.objects.filter(word=the_piece.pk)
	if request.user.is_authenticated():
		logged = "true"
	else:
		logged=()
	return render_to_response('word.html', {'the_entry': the_entry, 'the_word': the_word, 'logged' : logged}, context_instance=RequestContext(request))

def log_it(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				hepsi=piece.objects.all()
				return render_to_response('index.html', {'all_pieces' : hepsi}, context_instance=RequestContext(request))
			else:
				pass
		else:
			pass
	return render_to_response('login.html', context_instance=RequestContext(request))
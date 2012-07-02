# Create your views here.
# -*- coding: utf-8 -*-
from masterpiece.models import piece, entry
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def home(request):
	hepsi=piece.objects.all()
	if request.user.is_authenticated():
		logged = "true"
		the_name = request.user.username
	else:
		logged = ()
		the_name = ()
	return render_to_response('index.html', {'all_pieces' : hepsi, 'logged' : logged, 'the_logged' : the_name}, context_instance=RequestContext(request))
	

def word(request, the_word):
	the_piece = get_object_or_404(piece, word=the_word)
	if request.user.is_authenticated():
		logged = "true"
		the_name = request.user.username
	else:
		logged = ()
		the_name = ()
	if request.method == 'POST':
		newEntry = request.POST.get('yeni',None)
		if newEntry:
			if request.user.is_authenticated():
				logged = "true"
				entry.objects.create(content=newEntry, word=the_piece, username=User.objects.get(username=request.user.username))
			else:
				logged = ()
	the_entry = entry.objects.filter(word=the_piece.pk)
	return render_to_response('word.html', {'the_entry': the_entry, 'the_word': the_word, 'logged' : logged, 'the_logged' : the_name}, context_instance=RequestContext(request))

def log_it(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				hepsi=piece.objects.all()
				if request.user.is_authenticated():
					logged = "true"
					the_name = request.user.username
				return render_to_response('index.html', {'all_pieces' : hepsi, 'logged' : logged, 'the_logged' : the_name}, context_instance=RequestContext(request))
			else:
				hata = "Kullanıcı aktif değil"
				the_name = ()
				return render_to_response('login.html', {'hata' : hata, 'the_logged' : the_name}, context_instance=RequestContext(request))
		else:
			hata = "Kullanıcı adı veya şifre hatalı! Tekrar Deneyin."
			the_name = ()
			return render_to_response('login.html', {'hata' : hata, 'the_logged' : the_name}, context_instance=RequestContext(request))
	return render_to_response('login.html', context_instance=RequestContext(request))

def logout_it(request):
	logout(request)
	hepsi=piece.objects.all()
	return render_to_response('index.html', {'all_pieces' : hepsi}, context_instance=RequestContext(request))
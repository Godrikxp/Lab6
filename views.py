# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response
from mysite.models import foo

def lab6ajax(request):
    return render_to_response('Lab6ajax.html')

def postajax(request):
	values = request.GET.items()
	values.sort()
	html = []
	for k, v in values:
		html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
	foos = foo.objects.all()
	#print request.GET['age']
	if request.method == 'GET':
		Foo = foo(
			fio = request.GET['fio'],
			age = request.GET['age'],
			email = request.GET['email'],
			phone = request.GET['tel']
		)
	Foo.save()
	return HttpResponse('<table>%s</table>' % '\n'.join(html))
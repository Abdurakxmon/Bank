from django.shortcuts import render
from math import log
# Create your views here.
def home(request):
	return render(request, 'index.html')
def formulalar(request):
	return render(request, 'formulalar.html')
def misollar(request):
	return render(request, 'misollar.html')
def about(request):
	return render(request, 'about.html')
def hisob(request):
	form=False
	if request.method=='POST':
		form = request.POST.get('form')
	return render(request, 'hisob.html', {'form':form})
def umumiy_hisob(request):
	context = {
		'typee':"Choose...",
		'c':'',
		'r':'',
		'n':'',
		'k':'',
	}
	if request.method=='POST':
		typee = request.POST.get('a')
		c = request.POST.get('b')
		r = request.POST.get('c')
		n = request.POST.get('d')
		k = request.POST.get('e')
		if typee=='sodda':
			mes =(float(c)*float(r)*float(n))/100
		elif typee=='murakkab':
			mes =float(c)*pow((1+(float(r)/(float(k)*100))),(float(n)*float(k)))
		else:
			mes ="Fo'rmani to'liq to'ldiring!"
		print(mes)
		context = {
			'mes':mes,
			'typee':typee,
			'c':c,
			'r':r,
			'n':n,
			'k':k,
		}
	return render(request, 'hisob_.html',context)
def faq(request):
	return render(request, 'faq.html')
def a(request):
	context = {
		'typee':"Choose...",
		'c':'',
		'r':'',
		'n':'',
		'k':'',
	}

	if request.method=='POST':
		typee = request.POST.get('a')
		c = request.POST.get('b')
		r = request.POST.get('c')
		n = request.POST.get('d')
		k = request.POST.get('e')
		if typee=='sodda':
			mes =float(c)+(float(c)*float(r)*float(n))/100
		elif typee=='murakkab':
			mes =float(c)*pow((1+(float(r)/(float(k)*100))),(float(n)*float(k)))
		else:
			mes ="Fo'rmani to'liq to'ldiring!"
		print(mes)
		context = {
			'mes':mes,
			'typee':typee,
			'c':c,
			'r':r,
			'n':n,
			'k':k,
		}
	return render(request, 'A.html',context)

def i(request):
	context = {
		'typee':"Choose...",
		'c':'',
		'r':'',
		'n':'',
		'k':'',
	}

	if request.method=='POST':
		typee = request.POST.get('a')
		c = request.POST.get('b')
		r = request.POST.get('c')
		n = request.POST.get('d')
		k = request.POST.get('e')
		if typee=='sodda':
			mes = (float(c)*float(r)*float(n))/100
		elif typee=='murakkab':
			mes = (float(c)*pow((1+(float(r)/(float(k)*100))),(float(n)*float(k))))-float(c)
		else:
			mes ="Fo'rmani to'liq to'ldiring!"
		print(mes)
		context = {
			'mes':mes,
			'typee':typee,
			'c':c,
			'r':r,
			'n':n,
			'k':k,
		}
	return render(request, 'I.html',context)

def c(request):
	return render(request, 'C.html')

def c_1(request):
	context = {
		'c':'',
		'r':'',
		'n':'',
	}

	if request.method=='POST':
		c = request.POST.get('b')# I
		r = request.POST.get('c')
		n = request.POST.get('d')
		mes = (float(c)*100)/(float(r)*float(n))
		context = {
			'mes':mes,
			'c':c,
			'r':r,
			'n':n,
		}
	return render(request, 'C_1.html',context)

def c_2(request):
	context = {
		'c':'',
		'r':'',
		'n':'',
		'k':'',
	}

	if request.method=='POST':
		c = request.POST.get('b') #A
		r = request.POST.get('c')
		n = request.POST.get('d')
		k = request.POST.get('e')
		mes = float(c)/(pow((1+(float(r)/(float(k)*100))),(float(n)*float(k))))
		context = {
			'mes':mes,
			'c':c,
			'r':r,
			'n':n,
			'k':k,
		}
	return render(request, 'C_2.html',context)

def r(request):
	return render(request, 'r.html')

def r_1(request):
	context = {
		'c':'',
		'r':'',
		'n':'',
	}

	if request.method=='POST':
		c = request.POST.get('b') 
		r = request.POST.get('c')#I
		n = request.POST.get('d')
		mes = (float(r)*100)/(float(c)*float(n))
		context = {
			'mes':mes,
			'c':c,
			'r':r,
			'n':n,
		}
	return render(request, 'r_1.html',context)

def r_2(request):
	context = {
		'c':'',
		'r':'',
		'n':'',
		'k':'',
	}

	if request.method=='POST':
		c = request.POST.get('b')
		r = request.POST.get('c')# A
		n = request.POST.get('d')
		k = request.POST.get('e')
		mes = (((float(r)/float(c)) ** (1/(float(k)*float(n))))-1)*100*float(k)
		context = {
			'mes':mes,
			'c':c,
			'r':r,
			'n':n,
			'k':k,
		}
	return render(request, 'r_2.html',context)


def n(request):
	return render(request, 'n.html')

def n_1(request):
	context = {
		'c':'',
		'r':'',
		'n':'',
	}

	if request.method=='POST':
		c = request.POST.get('b')
		r = request.POST.get('c')# I
		n = request.POST.get('d') 
		mes = (float(n)*100)/(float(r)*float(c))
		context = {
			'mes':mes,
			'c':c,
			'r':r,
			'n':n,
		}
	return render(request, 'n_1.html',context)

def n_2(request):
	context = {
		'c':'',
		'r':'',
		'n':'',#A
		'k':'',
	}

	if request.method=='POST':
		c = request.POST.get('c')
		r = request.POST.get('b')
		n = request.POST.get('d')# A
		k = request.POST.get('e')
		mes = log((float(n)/float(c)),pow((1+(float(r)/(100*float(k)))),float(k)))
		context = {
			'mes':mes,
			'c':c,
			'r':r,
			'n':n,
			'k':k,
		}
	return render(request, 'n_2.html',context)

def k(request):
	
	context = {
		'c':'',
		'r':'',
		'n':'',
		'k':'',
	}

	if request.method=='POST':
		c = request.POST.get('b')
		r = request.POST.get('c')
		n = request.POST.get('d')
		k = request.POST.get('e') # A
		mes = 0
		context = {
			'mes':mes,
			'c':c,
			'r':r,
			'n':n,
			'k':k,
		}
	return render(request, 'k.html',context)

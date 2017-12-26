from django.shortcuts import render, HttpResponse
from django.template import loader
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

#뷰가 경로!!!!
# Create your views here.
# test 2017.12.26 2

def bootstrap_html(request):
	context = {}

	load_template = request.path.split('/')[-1]
	template = loader.get_template(load_template)
	return HttpResponse(template.render(context, request))
# def blank(request):
# 	return render(request, "blank.html",{})
#
# def buttons(request):
# 	return render(request, "buttons.html",{})
#
# def flot(request):
# 	return render(request, "flot.html",{})
#
# def forms(request):
# 	return render(request, "forms.html",{})
#
# def grid(request):
# 	return render(request, "grid.html",{})
#
# def icons(request):
# 	return render(request, "icons.html",{})
#
# def morris(request):
# 	return render(request, "morris.html",{})
#
# def notifications(request):
# 	return render(request, "notifications.html",{})
#
# def tables(request):
# 	return render(request, "tables.html",{})
#
# def typography(request):
# 	return render(request, "typography.html",{})
#
# def panels_wells(request):
# 	return render(request, "panels-wells.html",{})



class IndexView(TemplateView):
    template_name = 'index.html'

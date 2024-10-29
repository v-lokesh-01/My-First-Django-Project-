from django.views.generic import TemplateView



class homepage(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView): # new
    template_name = 'about.html'



class MenuPageView(TemplateView):
    template_name = 'menu.html'    



class ContactPageView(TemplateView):
    template_name = 'contact.html'
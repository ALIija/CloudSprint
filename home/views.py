from django.shortcuts import render
from django.views.generic import TemplateView

class KittyLandingView(TemplateView):
    template_name = "home/kitty_landing_page.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Kitty Corner - Your Purr-fect Cat Blog'
        return context

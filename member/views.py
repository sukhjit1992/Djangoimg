from django.views.generic import TemplateView, DetailView
from .models import member


# Create your views here.
class Homepage(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        members = member.objects.all()
        context= super().get_context_data(**kwargs)
        context = {'members': members}
        return context
class PostDetailView(DetailView):
    template_name = "detail.html"
    model = member


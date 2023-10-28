from django.views.generic import TemplateView, DetailView, FormView
from .models import member
from .forms import PostForm


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
class AddPostView(FormView):
    template_name= "form.html"
    form_class = PostForm
    success_url = "/"
    def form_valid(self, form):
        new_object = member.objects.create(
            name= form.cleaned_data['name'],
            img = form.cleaned_data['img']
        )
        return super().form_valid(form)

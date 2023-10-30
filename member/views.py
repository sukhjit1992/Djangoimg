from django.contrib import messages
from django.views.generic import TemplateView, DetailView, FormView
from .models import member
from .forms import PostForm


# Create your views here.
class Homepage(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        members = member.objects.all().order_by('-id')
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
    def dispatch(self, request, *args, **kwargs):
        self.request=request
        return super().dispatch(request, *args, **kwargs)
        
    def form_valid(self, form):
        new_object = member.objects.create(
            name= form.cleaned_data['name'],
            img = form.cleaned_data['img']
        )
        
        messages.add_message(self.request,messages.SUCCESS,"uploading is successful")
        return super().form_valid(form)

from django.views import generic
from .models import Quote, DailyMotivationalQuote
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.forms import UserCreationForm



class IndexView(generic.TemplateView):
    template_name = 'myApp/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        quote = DailyMotivationalQuote.objects.order_by('-created_at').first()
        context['quote'] = quote.get_quote()
        return context


class QuoteListView(LoginRequiredMixin, generic.ListView):
    model = Quote
    template_name = 'myApp/quote_list.html'
    context_object_name = 'quotes'


class QuoteDetailView(LoginRequiredMixin, generic.DetailView):
    model = Quote
    template_name = 'myApp/quote_detail.html'


class QuoteUpdateView(LoginRequiredMixin,
                      UserPassesTestMixin,
                      generic.UpdateView):
    model = Quote
    template_name = 'myApp/quote_edit.html'
    fields = ['body', 'author']

    def test_func(self):
        obj = self.get_object()
        return obj.publisher == self.request.user


class QuoteDeleteView(LoginRequiredMixin,
                      UserPassesTestMixin,
                      generic.DeleteView):
    model = Quote
    template_name = 'myApp/quote_delete.html'
    success_url = reverse_lazy('quote_list')

    def test_func(self):
        obj = self.get_object()
        return obj.publisher == self.request.user


class QuoteCreateView(LoginRequiredMixin, generic.CreateView):
    model = Quote
    template_name = "myApp/quote_new.html"
    fields = ['body', 'author']

    def form_valid(self, form):
        form.instance.publisher = self.request.user
        return super().form_valid(form)


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/sign_up.html'


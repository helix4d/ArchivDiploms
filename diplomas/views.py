from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Diploma
from .forms import DiplomaForm


class DiplomaListView(LoginRequiredMixin, ListView):
    model = Diploma
    paginate_by = 10
    template_name = "diplomas/diploma_list.html"

    def get_queryset(self):
        qs = Diploma.objects.all()
        name = self.request.GET.get("q")
        number = self.request.GET.get("number")
        if name:
            qs = qs.filter(full_name__icontains=name)
        if number:
            qs = qs.filter(diploma_number=number)
        return qs


class DiplomaDetailView(LoginRequiredMixin, DetailView):
    model = Diploma
    template_name = "diplomas/diploma_detail.html"


class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


class DiplomaCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = Diploma
    form_class = DiplomaForm
    template_name = "diplomas/diploma_form.html"
    success_url = reverse_lazy("diploma_list")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class DiplomaUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = Diploma
    form_class = DiplomaForm
    template_name = "diplomas/diploma_form.html"
    success_url = reverse_lazy("diploma_list")


class DiplomaDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = Diploma
    template_name = "diplomas/diploma_confirm_delete.html"
    success_url = reverse_lazy("diploma_list")


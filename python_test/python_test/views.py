from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import View, ListView, CreateView, UpdateView, TemplateView

from .models import Client
from .forms import ClientAddForm


class ClientDetails(ListView):
    """ view to list client details using get_context_data
    method to get the complete client list and display them"""

    model = Client
    template_name = 'client_list.html'
    context_object_name = "complete_client_list"


class AddClientDetails(CreateView):
    """ view to accept client details via a form and save
    to client model  """

    model = Client
    form_class = ClientAddForm
    template_name = 'client_add.html'
    success_url = reverse_lazy('add_client')

    def post(self, request, *args, **kwargs):
        form = ClientAddForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Client Details Added Successfully')
            return redirect('add_client')
        return render(request, 'client_add.html', {'form': form})


class EditClientDetails(AddClientDetails):
    """ view to edit client details via a form using
    the above AddClientDetails view as base """
    template_name = 'client_edit.html'
    success_url = reverse_lazy('edit_client')
    form_class = ClientAddForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['client_list'] = Client.objects.all().values('id', 'client_contact_name')
        return context

    def post(self, request, *args, **kwargs):
        instance = get_object_or_404(Client, id=request.POST.get('select_id'))
        form = ClientAddForm(request.POST or None, instance=instance)
        client_list = Client.objects.all().values('id', 'client_contact_name')
        if form.is_valid():
            form.save()
            messages.success(request, 'Client Details Updated Successfully')
            return redirect('edit_client')
        return render(request, 'client_edit.html', {'form': form, 'client_list':client_list})


class GetEditClientDetails(View):
    """ ajax view to fetch client record and display the details
    on the dropdown box onchange event"""
    model = Client
    template_name = 'client_edit.html'

    def get(self, *args, **kwargs):
        client_id = self.request.GET.get('client_id', None)
        client_dict = Client.objects.filter(id=client_id).values()[0]
        return JsonResponse(client_dict)


class SearchClients(View):
    """ search functionality to search for clients """

    def get(self, *args, **kwargs):
        selected_item = self.request.GET.get('selected_item', None)
        search_text_value = self.request.GET.get('search_text_value', None)

        if selected_item == "ClientName":
            search_objs = Client.objects.filter(client_name__icontains=search_text_value).values()
        elif selected_item == "Email":
            search_objs = Client.objects.filter(email__icontains=search_text_value).values()
        elif selected_item == "Phone":
            search_objs = Client.objects.filter(phone_number__icontains=search_text_value).values()
        else:
            search_objs = Client.objects.filter(suburb__icontains=search_text_value).values()
        return JsonResponse(list(search_objs), safe=False)


class ClientDetailsEdit(UpdateView):
    """ edit client details from the details page """
    template_name = 'client_edit.html'
    success_url = reverse_lazy('edit_client')
    form_class = ClientAddForm


class ClientHome(TemplateView):
    template_name = 'base.html'


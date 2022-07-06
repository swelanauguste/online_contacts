from django.views.generic import ListView
from django.db.models import Q
from .models import Contact, Role, Agency


class ContactListView(ListView):
    model = Contact
    paginate_by = 10
    
    def get_context_data(self, *args, **kwargs):
        context = super(ContactListView, self).get_context_data(*args, **kwargs)
        context["role_list"] = Role.objects.all()
        return context
    
    def get_queryset(self):
        queryset = Contact.objects.all()
        q = self.request.GET.get("q")
        if q:
            queryset = queryset.filter(
                Q(contact__icontains=q)
                | Q(role__role__icontains=q)
                | Q(agency__agency__icontains=q)
                | Q(tel__icontains=q)
            ).distinct()
        return queryset

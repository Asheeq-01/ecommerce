from .models import Category_model

def link(request):
    c=Category_model.objects.all()
    return {'link':c}


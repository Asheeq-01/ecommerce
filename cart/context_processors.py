from .models import Cart_model

def count(request):
    total=0
    u=request.user
    
    try:
        c=Cart_model.objects.filter(user=u)
        for i in c:
            total=total+i.quantity
    except:
        pass
    
    return {'count':total}

from registration.models import *
from taxfiling.models import *
from othernavs.models import Registration as othernavreg
from chat.models import conversation
from Home.models import BlogNews
from dashboard.views import editname

def regfunc(request):
   Registrations = Registration.objects.all()
   othernavregob = othernavreg.objects.all()
   tfiling = TaxFiling.objects.all()
   messages =  conversation.objects.filter(msgby=request.user.id).order_by('time') if request.user.is_authenticated else []
   res= {
      'Registrations':Registrations,
      'othernavreg':othernavregob,
      'tfiling':tfiling,
      'msg':messages,
      'editnames':editname,
      'choices' : BlogNews().Getchoices
   }
   return res
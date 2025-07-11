from citate.models import Citata

c = Citata()
c.content = "test citata"
c.save()
print(Citata.objects.all())
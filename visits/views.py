from django.db import connection
from django.http import HttpResponse

from .models import Visit


def index(request):
    Visit.objects.create()
    total = Visit.objects.count()
    return HttpResponse(
        f"<h1>example-django na UQBITZ</h1><p>segundo deploy</p>"
        f"<p>visitas: {total}</p>"
        f"<p>banco: {connection.vendor}</p>"
    )

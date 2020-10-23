from django.shortcuts import render

# Create your views here.
def quote_list(request):
    return render(request, 'quote/quote_list.html', {})
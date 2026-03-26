from django.shortcuts import render, redirect
from .models import Feedback

# Create your views here.
def home(request):
    return render(request, 'testApp/home.html')

def about(request):
    return render(request, 'testApp/about.html')

def feedback_view(request):
    if request.method == 'POST':
        # Mengambil data dari form
        nama = request.POST.get('nama')
        email = request.POST.get('email')
        pesan = request.POST.get('pesan')
        
        # Simpan ke Database
        Feedback.objects.create(nama=nama, email=email, pesan=pesan)
        
        # Redirect atau beri tanda sukses
        return render(request, 'testApp/form.html', {'status': 'success'})
    
    return render(request, 'testApp/form.html')
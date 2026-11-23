from django.shortcuts import render,redirect,get_object_or_404
from .models import Autor,Libro,Prestamo
from .forms import AutorForm,LibroForm,PrestamoForm

# ---------- AUTOR ----------
def autor_list(request):
    autores = Autor.objects.all()
    return render(request,'autor_list.html',{'autores':autores})

def autor_create(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('autor_list')
    else:
        form = AutorForm()
    return render(request,'form.html',{'form':form,'titulo':'Agregar autor'})

def autor_update(request,pk):
    autor = get_object_or_404(Autor,pk=pk)
    if request.method == 'POST':
        form = AutorForm(request.POST,instance=autor)
        if form.is_valid():
            form.save()
            return redirect('autor_list')
    else:
        form = AutorForm(instance=autor)
    return render(request,'form.html',{'form':form,'titulo':'Editar autor'})

def autor_delete(request,pk):
    autor = get_object_or_404(Autor,pk=pk)
    if request.method == 'POST':
        autor.delete()
        return redirect('autor_list')
    return render(request,'confirmar_borrar.html',{'objeto':autor,'volver':'autor_list'})

# ---------- LIBRO ----------
def libro_list(request):
    libros = Libro.objects.all()
    return render(request,'libro_list.html',{'libros':libros})

def libro_create(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('libro_list')
    else:
        form = LibroForm()
    return render(request,'form.html',{'form':form,'titulo':'Agregar libro'})

def libro_update(request,pk):
    libro = get_object_or_404(Libro,pk=pk)
    if request.method == 'POST':
        form = LibroForm(request.POST,instance=libro)
        if form.is_valid():
            form.save()
            return redirect('libro_list')
    else:
        form = LibroForm(instance=libro)
    return render(request,'form.html',{'form':form,'titulo':'Editar libro'})

def libro_delete(request,pk):
    libro = get_object_or_404(Libro,pk=pk)
    if request.method == 'POST':
        libro.delete()
        return redirect('libro_list')
    return render(request,'confirmar_borrar.html',{'objeto':libro,'volver':'libro_list'})

# ---------- PRESTAMO ----------
def prestamo_list(request):
    prestamos = Prestamo.objects.all()
    return render(request,'prestamo_list.html',{'prestamos':prestamos})

def prestamo_create(request):
    if request.method == 'POST':
        form = PrestamoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('prestamo_list')
    else:
        form = PrestamoForm()
    return render(request,'form.html',{'form':form,'titulo':'Agregar préstamo'})

def prestamo_update(request,pk):
    prestamo = get_object_or_404(Prestamo,pk=pk)
    if request.method == 'POST':
        form = PrestamoForm(request.POST,instance=prestamo)
        if form.is_valid():
            form.save()
            return redirect('prestamo_list')
    else:
        form = PrestamoForm(instance=prestamo)
    return render(request,'form.html',{'form':form,'titulo':'Editar préstamo'})

def prestamo_delete(request,pk):
    prestamo = get_object_or_404(Prestamo,pk=pk)
    if request.method == 'POST':
        prestamo.delete()
        return redirect('prestamo_list')
    return render(request,'confirmar_borrar.html',{'objeto':prestamo,'volver':'prestamo_list'})
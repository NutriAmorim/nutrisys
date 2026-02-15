from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import FileResponse, Http404
from .models import FichaAnamnese
from .forms import FichaAnamneseForm
from .utils import gerar_pdf, gerar_word
import os


def home(request):
    """Página inicial com o formulário"""
    if request.method == 'POST':
        form = FichaAnamneseForm(request.POST)
        if form.is_valid():
            # Salvar ficha
            ficha = form.save()
            
            try:
                # Gerar Word
                word_path = gerar_word(ficha)
                ficha.arquivo_docx = word_path.replace(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'media/'), '')
                
                # Gerar PDF
                pdf_path = gerar_pdf(ficha)
                ficha.arquivo_pdf = pdf_path.replace(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'media/'), '')
                
                ficha.save()
                
                messages.success(request, f'Prontuário criado com sucesso! ID: {ficha.id}')
                return redirect('visualizar_ficha', ficha_id=ficha.id)
            
            except Exception as e:
                messages.error(request, f'Erro ao gerar documentos: {str(e)}')
                return redirect('home')
        else:
            messages.error(request, 'Por favor, corrija os erros no formulário.')
    else:
        form = FichaAnamneseForm()
    
    return render(request, 'anamnese/home.html', {'form': form})


def lista_fichas(request):
    """Lista todas as fichas criadas"""
    fichas = FichaAnamnese.objects.all().order_by('-data_criacao')
    return render(request, 'anamnese/lista_fichas.html', {'fichas': fichas})


def visualizar_ficha(request, ficha_id):
    """Visualiza uma ficha específica"""
    ficha = get_object_or_404(FichaAnamnese, id=ficha_id)
    return render(request, 'anamnese/visualizar_ficha.html', {'ficha': ficha})


def download_pdf(request, ficha_id):
    """Download do PDF da ficha"""
    ficha = get_object_or_404(FichaAnamnese, id=ficha_id)
    
    if not ficha.arquivo_pdf:
        # Se não existe PDF, gera agora
        try:
            pdf_path = gerar_pdf(ficha)
            ficha.arquivo_pdf = pdf_path.replace(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'media/'), '')
            ficha.save()
        except Exception as e:
            raise Http404(f"Erro ao gerar PDF: {str(e)}")
    
    # Caminho completo do arquivo
    filepath = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'media', str(ficha.arquivo_pdf))
    
    if os.path.exists(filepath):
        return FileResponse(open(filepath, 'rb'), as_attachment=True, filename=f'prontuario_{ficha.nome}.pdf')
    else:
        raise Http404("PDF não encontrado")


def download_word(request, ficha_id):
    """Download do Word da ficha"""
    ficha = get_object_or_404(FichaAnamnese, id=ficha_id)
    
    if not ficha.arquivo_docx:
        # Se não existe Word, gera agora
        try:
            word_path = gerar_word(ficha)
            ficha.arquivo_docx = word_path.replace(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'media/'), '')
            ficha.save()
        except Exception as e:
            raise Http404(f"Erro ao gerar Word: {str(e)}")
    
    # Caminho completo do arquivo
    filepath = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'media', str(ficha.arquivo_docx))
    
    if os.path.exists(filepath):
        return FileResponse(open(filepath, 'rb'), as_attachment=True, filename=f'prontuario_{ficha.nome}.docx')
    else:
        raise Http404("Word não encontrado")


def editar_ficha(request, ficha_id):
    """Edita uma ficha existente"""
    ficha = get_object_or_404(FichaAnamnese, id=ficha_id)
    
    if request.method == 'POST':
        form = FichaAnamneseForm(request.POST, instance=ficha)
        if form.is_valid():
            ficha = form.save()
            
            # Regenerar documentos
            try:
                word_path = gerar_word(ficha)
                ficha.arquivo_docx = word_path.replace(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'media/'), '')
                
                pdf_path = gerar_pdf(ficha)
                ficha.arquivo_pdf = pdf_path.replace(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'media/'), '')
                
                ficha.save()
                
                messages.success(request, 'Prontuário atualizado com sucesso!')
                return redirect('visualizar_ficha', ficha_id=ficha.id)
            except Exception as e:
                messages.error(request, f'Erro ao gerar documentos: {str(e)}')
        else:
            messages.error(request, 'Por favor, corrija os erros no formulário.')
    else:
        form = FichaAnamneseForm(instance=ficha)
    
    return render(request, 'anamnese/editar_ficha.html', {'form': form, 'ficha': ficha})


def deletar_ficha(request, ficha_id):
    """Deleta uma ficha"""
    ficha = get_object_or_404(FichaAnamnese, id=ficha_id)
    
    if request.method == 'POST':
        # Deletar arquivos se existirem
        if ficha.arquivo_pdf:
            filepath = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'media', str(ficha.arquivo_pdf))
            if os.path.exists(filepath):
                os.remove(filepath)
        
        if ficha.arquivo_docx:
            filepath = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'media', str(ficha.arquivo_docx))
            if os.path.exists(filepath):
                os.remove(filepath)
        
        ficha.delete()
        messages.success(request, 'Prontuário deletado com sucesso!')
        return redirect('lista_fichas')
    
    return render(request, 'anamnese/deletar_ficha.html', {'ficha': ficha})

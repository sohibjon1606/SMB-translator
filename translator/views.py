from django.shortcuts import render
from googletrans import Translator

def home(request):
    translated_text = ""
    original_text = ""
    
    if request.method == "POST":
        original_text = request.POST.get('text', '')
        target_lang = request.POST.get('language', 'en')
        
        try:
            translator = Translator()
            translation = translator.translate(original_text, dest=target_lang)
            translated_text = translation.text
        except Exception as e:
            translated_text = "Xatolik: Tarjima xizmati ulanmadi."

    return render(request, 'index.html', {
        'translated_text': translated_text, 
        'original_text': original_text
    })
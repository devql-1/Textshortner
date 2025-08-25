
from django.shortcuts import render
from transformers import pipeline

# Load model once
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def model(request):
    summary = None
    if request.method == "POST":
        input_text = request.POST.get("input_text")
        if input_text:
            summary = summarizer(
                input_text,
                min_length=100,
                do_sample=False
            )[0]['summary_text']

    return render(request, 'index.html', {'summary': summary})
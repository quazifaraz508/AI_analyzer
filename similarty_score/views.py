import os
from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from django.conf import settings
from sentence_transformers import SentenceTransformer, util
from pdfminer.high_level import extract_text
from docx import Document

# ✅ Load or Download the Model
MODEL_PATH = os.path.join(settings.BASE_DIR, "all-mpnet-base-v2-model")

if not os.path.exists(MODEL_PATH):
    print("⏳ Downloading the model for the first time... Please wait.")
    model = SentenceTransformer("all-mpnet-base-v2")
    model.save(MODEL_PATH)
    print("✅ Model downloaded and saved locally.")
else:
    print("✅ Loading model from local storage...")
    model = SentenceTransformer(MODEL_PATH)


# ✅ Function to extract text from a PDF
def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)


# ✅ Function to extract text from a DOCX
def extract_text_from_docx(docx_path):
    doc = Document(docx_path)
    return "\n".join([para.text for para in doc.paragraphs])


# ✅ Function to calculate similarity
def calculate_similarity(resume_text, job_description):
    embedding_resume = model.encode(resume_text, convert_to_tensor=True)
    embedding_job = model.encode(job_description, convert_to_tensor=True)
    
    similarity = util.pytorch_cos_sim(embedding_resume, embedding_job)
    return similarity.item()


# ✅ Django View to Handle File Upload
def upload_resume(request):
    if request.method == "POST" and request.FILES.get("resume"):
        resume_file = request.FILES["resume"]
        file_extension = resume_file.name.split(".")[-1].lower()

        # Save file temporarily
        file_path = default_storage.save(os.path.join("uploads", resume_file.name), resume_file)
        file_full_path = os.path.join(settings.MEDIA_ROOT, file_path)

        # Extract text based on file type
        if file_extension == "pdf":
            extracted_text = extract_text_from_pdf(file_full_path)
        elif file_extension == "docx":
            extracted_text = extract_text_from_docx(file_full_path)
        else:
            extracted_text = "Unsupported file format"

        # Delete the file after extraction
        default_storage.delete(file_path)

        # Sample job description (You can replace this with actual job descriptions from a database)
        job_description = "We are looking for a Python developer with experience in Django, NLP, and AI."

        # ✅ Calculate Similarity
        similarity_score = calculate_similarity(extracted_text, job_description)
        
        return render(
            request,
            "resume_page.html",
            {"extracted_text": extracted_text, "similarity_score": round(similarity_score * 100, 2)},
        )

    return render(request, "resume_page.html")

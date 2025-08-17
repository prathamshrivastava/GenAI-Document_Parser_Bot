# Document Parser App – LangChain + Google Gemini

A Streamlit application that allows users to upload resumes or any document (PDF, DOCX, TXT) and extract structured information using Google Gemini and LangChain.

---

## App Concept

Users upload a resume and the app performs the following steps:

1. Extracts raw text from the uploaded file.
2. Previews the extracted text.
3. Sends the text to a Large Language Model (Google Gemini) for parsing.
4. Returns structured information in JSON format, including:
   - Name
   - Age
   - Experience
   - Education
   - Projects
   - Languages

---

## App Objective

The app is designed to:

- Automatically parse resumes for recruiters or HR professionals.
- Extract relevant details in a structured format.
- Reduce manual data entry and improve efficiency.

---

## Interface Flow

- Users upload a resume in PDF, DOCX, or TXT format.
- Extracted text is displayed in a preview area.
- Click "Ask LLM" to parse the resume.
- Structured JSON results are displayed.

---

## Project Structure

| File / Directory     | Description                                        |
|----------------------|----------------------------------------------------|
| `app.py`             | Main Streamlit app                                 |
| `.env`               | Contains Google API Key                             |
| `requirements.txt`   | Python dependencies                                 |
| `README.md`          | Documentation file                                  |

---

## Getting Started

### 🔧 Prerequisites

- Python 3.10+
- Streamlit
- Internet connection
- Google API Key

cd ResumeParserApp

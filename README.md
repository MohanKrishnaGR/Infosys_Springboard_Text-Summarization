<div align='center'>
    <a><img src="https://i.ibb.co/P4B4LrL/springboard-logo-removebg-preview.png" alt="springboard-logo-removebg-preview" border="0"></a>
</div>

[![Deploy to Azure Container Instance](https://github.com/MohanKrishnaGR/Infosys_Springboard_Text-Summarization/actions/workflows/azure.yml/badge.svg?event=push)](https://github.com/MohanKrishnaGR/Infosys_Springboard_Text-Summarization/actions/workflows/azure.yml)

![Docker Image Version](https://img.shields.io/docker/v/mohankrishnagr/infosys_text-summarization/group)
![Docker Image Size](https://img.shields.io/docker/image-size/mohankrishnagr/infosys_text-summarization/group)
![Docker Pulls](https://img.shields.io/docker/pulls/mohankrishnagr/infosys_text-summarization)
<i>
# Text Summarization

A project by AI/ML Interns (Group 4) @ Infosys Springboard, Summer 2024.
## Mentor
Mr. Narendra Kumar

## Contents
- [Problem Statement](#problem-statement)
- [Project Statement](#project-statement)
- [Approach to Solution](#approach-to-solution)
- [Background Research](#background-research)
- [Solution](#solution)
- [Workflow](#workflow)
- [Data Collection](#data-collection)
- [Abstractive Text Summarization](#abstractive-text-summarization)
- [Extractive Text Summarization](#extractive-text-summarization)
- [Testing](#testing)
- [Deployment](#deployment)
- [Containerization](#containerization)
- [CI/CD Pipeline](#cicd-pipeline)

## Problem Statement
- Developing an automated text summarization system that can accurately and efficiently condense large bodies of text into concise summaries is essential for enhancing business operations.
- This project aims to deploy NLP techniques to create a robust text summarization tool capable of handling various types of documents across different domains.
- The system should deliver high-quality summaries that retain the core information and contextual meaning of the original text.

## Project Statement
- Text Summarization focuses on converting large bodies of text into a few sentences summing up the gist of the larger text.
- There is a wide variety of applications for text summarization including News Summary, Customer Reviews, Research Papers, etc.
- This project aims to understand the importance of text summarization and apply different techniques to fulfill the purpose.

## Approach to Solution
- **Figure:** Intended Plan
<div align="center">
    <a><img src="https://drive.usercontent.google.com/u/0/uc?id=1cn429WFQzvF1eDwEFiLsIk87M8KBELt8&export=download" border="0"></a>
</div>


## Background Research
- **Literature Review**
<div align="center">
    <a><img src="https://drive.usercontent.google.com/u/0/uc?id=1201kWfyGURgsA32u6Xe_WPSrO0izo8Fg&export=download" border="0"></a>
</div>

## Solution
- **Selected Deep Learning Architecture**

## Workflow
- Workflow for Abstractive Text Summarizer:
<div align="center">
    <a><img src="https://drive.usercontent.google.com/u/0/uc?id=1-smea28F10cOnmXXUj24QkzEZL-ffhWt&export=download" width="640" height="640"  border="0"></a>
</div><br>

- Workflow for Extractive Text Summarizer:
<div align="center">
    <a><img src="https://drive.usercontent.google.com/u/0/uc?id=1vS2Gm5ccJvjxH7fsnyOf3ARk2pNTR75p&export=download" width="640" height="640"  border="0"></a>
</div>


## Data Collection
- Data Preprocessing & Pre-processing Implemented in `src/data_preprocessing`.
- Data collection from different sources:
  - CNN, Daily Mail: News
  - BillSum: Legal
  - ArXiv: Scientific
  - Dialoguesum: Conversations
- Data integration ensures robust and multi-objective data, including News articles, Legal Documents – Acts, Judgements, Scientific papers, and Conversations.
- Validated the data through Data Statistics and Exploratory Data Analysis (EDA) using Frequency Plotting for every data source.
- Data cleansing optimized for NLP tasks: removed null records, lowercasing, punctuation removal, stop words removal, and lemmatization.
- Data splitting using sci-kit learn for training, testing, and validating the model, saved in CSV format.

## Abstractive Text Summarization
### Model Training & Evaluation
- **Training:**
  - Selected transformer architecture for ABSTRACTIVE SUMMARIZATION: fine-tuning a pre-trained model.
  - Chosen Facebook’s Bart Large model for its performance metrics and efficient trainable parameters.
      -  406,291,456 training parameters.
    
<div align="center">
    <a><img src="https://drive.usercontent.google.com/u/0/uc?id=1fe7MMx_-kEAN9c0QVJbsMj9dBUNgEZX8&export=download" border="0"></a>
</div><br>

- **Methods:**
  - Native PyTorch Implementation
  - Trainer API Implementation

### Method 1 - Native PyTorch
- Trained the model using manual training loop and evaluation loop in PyTorch. Implemented in: `src/model.ipynb`
- **Model Evaluation:** Source code:`src/evaluation.ipynb`
    - Obtained inconsistent results in inferencing.
    - There's a suspected tensor error while training using method 1, which could be attributed to the inconsistency of the model's output.
    -  Dire need to implement alternative approach   

### Method 2 – Trainer Class Implementation
- Utilized Trainer API from Hugging Face for optimized transformer model training. Implemented in: `src/bart.ipynb`
    - The model was trained with whole dataset for 10 epochs for 26:24:22 (HH:MM:SS) in 125420 steps.
     
- **Evaluation:** Performance metrics using ROUGE scores. Source code: `src/rouge.ipynb`
    - Model 2 - results outperformed that of method 1.
    - ROUGE1 (F-Measure) = 61.32 -> Benchmark grade
    - GPT4 performance for text summarization - ROUGE1 (F-Measure) is 63.22
 
- Comparative analysis showed significant improvement in performance after fine-tuning. Source code: `src/compare.ipynb`
<div align="center">
    <a><img src="https://drive.usercontent.google.com/u/0/uc?id=1V4u8ohFNFcceidx3l43LNjxTbtLZ233g&export=download" border="0"></a>
</div><br>

## Extractive Text Summarization
- Rather than choosing computationally intensive deep-learning models, utilizing a rule based approach will result in optimal solution. Utilized a new-and-novel approach of combining the matrix obtained from TF-IDF and KMeans Clustering methodology.
- It is the expanded topic modeling specifically to be applied to multiple lower-level specialized entities (i.e., groups) embedded in a single document. It operates at the individual document and cluster level.
- The sentence closest to the centroid (based on Euclidean distance) is selected as the representative sentence for that cluster.
- **Implementation:** Preprocess text, extract features using TF-IDF, and summarize by selecting representative sentences.
    - Source code: `src/Extractive_Summarization.ipynb`     

## Testing
- Implemented text summarization application using Gradio library for a web-based interface.
- **Source Code:** `src/interface.ipynb`

## Deployment
<div align="center">
    <a><img src="https://drive.usercontent.google.com/u/0/uc?id=1mvbC3IZzRxS0Hx0DoO6EvrQyKqgD--Gw&export=download" border="0"></a>
</div><br>

### Application
- **File Structure:** `summarize/`
<div align="center">
    <a><img src="https://drive.usercontent.google.com/u/0/uc?id=1OnHuW8YMPQYT88pqPbWAZCpgEFlic0kw&export=download" width="320" height="320" border="0"></a>
</div><br>

### API Endpoints
- Developed using FastAPI framework for handling URLs, files, and direct text input.
- **Endpoints:**
  - Root Endpoint
  - Summarize URL
  - Summarize File
  - Summarize Text

### Extractor Modules
- Extract text from various sources (URLs, PDF, DOCX) using BeautifulSoup and fitz.
- **Source Code:** `summarizer/extractors.py`

### Extractive Summary Script
- Implemented extractive summarizer module. Same as implemented in: src/bart.ipynb
- **Source Code:** `summarizer/extractive_summary.py`

### User Interface
- Developed a user-friendly interface using HTML, CSS, and JavaScript.
- **Source Code:** `summarizer/templates/index.html`

## Containerization
- Developed a Dockerfile to build a Docker image for the FastAPI application.
- **Source Code:** `summarizer/Dockerfile`
- **Image:** [Docker Image](https://hub.docker.com/layers/mohankrishnagr/infosys_text-summarization/group/images/sha256-28802ba2a3b30d36b94fbd878c97585c02c813534fc80fdca5e81494b96bfd08?context=explore)

## CI/CD Pipeline
- Developed a CI/CD pipeline using Docker, Azure and GitHub Actions.
- Utilized Azure Container Instance (ACI) for deploying the image, triggers for every push to the main branch.
- **Source Code:** `.github/workflows/azure.yml`
- **IPv4 Address:** [Text Summarizer](http://20.235.235.107:8000/) ( http://20.235.235.107:8000/ )
- **FQDN:** [Text Summarizer](http://text-summarizer.bqegenbyedfzhpa3.centralindia.azurecontainer.io:8000/) ( http://text-summarizer.bqegenbyedfzhpa3.centralindia.azurecontainer.io:8000/ )

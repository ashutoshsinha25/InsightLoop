1. Goal:

Build an AI-powered conversatinal insights engine that:
* Ingests raw chat/meeting trasncripts 
* Extract sentiments, emotions, entities, action items and topics 
* Generate summarizes and root-cause analysis 
* Enable users to ask natural questions and get evidence-backed, explainable answers:
    - "Why are customers unhappy this week?"


2. System Overview:

Top level architecture:
```mermaid
flowchart TD
    subgraph UI["Frontend UI"]
        A1["React / Streamlit"]
    end

    subgraph API["FastAPI Backend"]
        B1["Auth & API Gateway"]
        B2["Task Scheduler (Celery)"]
    end

    subgraph PIPELINE["Processing Pipeline"]
        C1["Data Ingestion<br/>(CSV, APIs)"]
        C2["NLP Processing<br/>(Sentiment, NER, Topics)"]
        C3["Insight Engine<br/>(Topics, Root-cause, Summary)"]
    end

    subgraph STORAGE["Embedding Store"]
        D1["FAISS / Weaviate"]
    end

    subgraph REASONING["LLM Reasoning"]
        E1["RAG / GPT / LLaMA"]
    end

    subgraph DASH["Insight Dashboards"]
        F1["Dashboards & Reports"]
    end

    %% Connections
    UI --> API
    API --> PIPELINE
    PIPELINE --> STORAGE
    STORAGE --> REASONING
    REASONING --> DASH
```
3. Core backend stack:

* Components: 
    - Framwwork: FastAPI
    - ASGI Server: Uvicorn 
    - Task Queue: Celery + Redis 
    - Serializartion/Validation: Pydantic v2
    - Authentication: FastAPI Users (JWT) or Firebase JWT Verify
    - API docs: Swagger / Redoc 

* Data & Storage: 

// TODO 

* Machine Learning / NLP: 
    - Embeddings: OpenAI / HuggingFace
    - Senmantic Analysis: HuggingFace Transformers
    - Topic Modeling: BERTopic / LDA 
    - Summarization: OpenAI (gpt) / Meta (bart-large-cnn) / Google (t5)
    - NER/Entity Extraction: SpaCy / HuggingFace
    - Keyword Extraction: YAKE / KeyBERT/ HuggingFace
    - Root Cause Analysis: Custom LLM Prompts / GPT-4/ Scikit-learn
    - RAG: LangGraph / LangChain
    - Evaluation: Promptfoo / nltk / rouge-score / bert-score


* Job Orchestration & Processing:
    - Asyn Queue: Celery + Redis
    - Monitoring: Celery Flower
    - Batch Processing: Corn (via Celery Beat)


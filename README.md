# **Agents Intensive Capstone Project**

### Multi-Agent System using **Google ADK**, **Gemini**, **FAISS**, and **Google APIs**

***

## ✅ Overview

This project is part of the **Kaggle Agents Intensive Capstone**. It demonstrates a **production-ready multi-agent system** designed to optimize workflows by:

*   Extracting tasks from unstructured data (PDFs, text, images).
*   Prioritizing tasks using AI reasoning.
*   Scheduling tasks and syncing with Google Calendar.
*   Providing iterative improvements through reflection agents.

***

## ✅ Tech Stack

*   **Python 3.11**
*   **Google Agent Development Kit (ADK)** – Hierarchical agent orchestration.
*   **Gemini Model** – Advanced reasoning and planning.
*   **FAISS** – Vector memory for semantic search.
*   **Google APIs** – Calendar & Gmail integration.
*   **Optional:** LangChain / CrewAI for additional orchestration patterns.

***

## ✅ Architecture

!Architecture Diagram Placeholder  
*(Replace with actual diagram later)*

**Core Components:**

*   **Orchestrator**: ADK-based hierarchical agent tree.
*   **Agents**:
    *   Extractor Agent
    *   Priority Agent
    *   Scheduler Agent
    *   Reflection Agent
    *   Communication Agent
*   **Memory Layer**: FAISS for long-term context.
*   **Reasoning Layer**: Gemini for prioritization and planning.

***

## ✅ Folder Structure

    project-root/
    ├── notebooks/
    │    └── kaggle_capstone.ipynb
    ├── src/
    │    ├── agents/
    │    │    ├── extractor.py
    │    │    ├── priority.py
    │    │    ├── scheduler.py
    │    │    ├── reflection.py
    │    │    └── communication.py
    │    ├── orchestrator.py
    │    ├── memory.py
    │    ├── utils.py
    ├── config/
    │    ├── agents.yaml
    │    └── settings.yaml
    ├── requirements.txt
    ├── Dockerfile
    ├── README.md
    └── LICENSE

***

## ✅ Setup Instructions

### **1. Clone the Repository**

```bash
git clone https://github.com/theshikhardwivedi/agents-intensive-capstone.git
cd agents-intensive-capstone
```

### **2. Install Dependencies**

```bash
pip install -r requirements.txt
```

### **3. Configure Google APIs**

*   Enable **Google Calendar API** and **Gmail API**.
*   Download OAuth credentials and store in `.env` or `credentials.json`.

### **4. Run the Notebook**

Open `notebooks/kaggle_capstone.ipynb` in Kaggle or Jupyter.

### **5. (Optional) Run with Docker**

```bash
docker build -t capstone-agent .
docker run -p 8501:8501 capstone-agent
```

***

## ✅ Features

*   Task extraction from PDFs, text, and images.
*   AI-based prioritization using Gemini.
*   Automated scheduling and calendar sync.
*   Iterative refinement through reflection agents.
*   Modular and scalable architecture.

***

## ✅ Evaluation Metrics

*   Accuracy of task extraction.
*   Latency for end-to-end workflow.
*   Scalability for multiple tasks.

***

## ✅ Future Enhancements

*   Add Slack/Teams integration.
*   Implement CI/CD with GitHub Actions.
*   Expand to voice-based task input.

***

## ✅ License

MIT License – Free to use and modify.

# Multi-Agent Research Assistant

A monolithic AI-powered application that autonomously researches a complex topic, analyzes sources, and generates a summarized report. Built with Flask, HTML/JS, BeautifulSoup, and NLTK. Entire system is containerized using Docker.

---

## Features

- Submit any technical/business research topic
- Agents coordinate to:
  - Search the web
  - Evaluate content
  - Analyze and summarize findings
- Download final report
- Monitor job progress live via UI

---

## Architecture

### Agents:
- **Research Agent**: Gathers web results using DuckDuckGo & BeautifulSoup
- **Analysis Agent**: Summarizes content using NLTK
- **Job Manager**: Manages job queue, tracks status
- **Writer Agent**: Format results into final reports

All logic is embedded into a single Python Flask application for simplicity and portability.

**NOTE:** Please refer to Future Scalability Section at the end for better architecture

### Diagram:
![image](https://github.com/user-attachments/assets/4b42123e-a5b5-491a-a77e-b5a384979842)



### APIs:

| Method | Endpoint            | Description                             | Request Body (if any)                     | Response Example                         |
|--------|---------------------|-----------------------------------------|-------------------------------------------|----------------------------------------  |
| POST   | `/query`            | Submit a new research job               | `{ "query": "Implications of AI" }`       | `{ "job_id": "abc123" }`                 |
| GET    | `/status/<job_id>`  | Get status of a specific job            | —                                         | `{ "status": "inprogress","report":null }`          |
| GET    | `/report/<job_id>`  | Download the generated report (if done) | —                                         | Returns `.txt` file                      |

---

##  UI

- View live job queue
- Auto-refreshing job status table
- View/download report after completion

---

##  Setup Instructions

### 1. Clone the Repo
```bash
git clone https://github.com/kartik3219/shyftlabs-multi-agent-assignment.git
cd shyftlabs-multi-agent-assignment
```

### 2. Run the docker command to build the image
```bash
docker build -t shyftlabs-multi-agent-assignment .
```

### 3. Run the docker command to run the image
```bash
docker run -p 5000:5000 shyftlabs-multi-agent-assignment
```

### 4. Go to localhost:5000 to access the UI

 
##  Future Scalability
This system has been designed to scale horizontally with minimal architectural changes. 
Key points:
- **Distributed Architecture**: Instead of having monolithic architecture all the services will be deployed separately using kubernetes or container apps. 
- **Worker Expansion**: More worker agents (e.g., research, analysis, writing) can be added to process jobs in parallel.
- **Queue-based Decoupling**: RabbitMQ ensures agents are decoupled and scalable. Additional workers can subscribe to the same queue. This will also allow to have retry capability.
- **Load Balancing**: Frontend and backend can be containerized and balanced using NGINX or Kubernetes.
- **Monitoring Ready**: System structure allows integration of Prometheus/Grafana for real-time monitoring.
- **Pluggable Agents**: Each agent can be enhanced or replaced without affecting the core pipeline.

### Architecture
![image](https://github.com/user-attachments/assets/f522e3d4-340c-4d3b-99ed-1c2750899804)





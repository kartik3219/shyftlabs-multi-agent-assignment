# job_manager.py

import threading
import uuid
import time
from agents.research_agent import ResearchAgent
from agents.analysis_agent import AnalysisAgent
from agents.writer_agent import WriterAgent

class JobManager:
    def __init__(self):
        self.jobs = {}

    def create_job(self, query):
        job_id = str(uuid.uuid4())
        self.jobs[job_id] = {"status": "queued", "report": None}
        thread = threading.Thread(target=self.process_job, args=(job_id, query))
        thread.start()
        return job_id

    def process_job(self, job_id, query):
        try:
            self.jobs[job_id]["status"] = "researching"
            research_agent = ResearchAgent()
            sources = research_agent.run(query)
            time.sleep(4)
            self.jobs[job_id]["status"] = "analyzing"
            analysis_agent = AnalysisAgent()
            analyzed = analysis_agent.run(sources)
            time.sleep(4)
            self.jobs[job_id]["status"] = "writing"
            writer_agent = WriterAgent()
            report = writer_agent.run(analyzed)
            time.sleep(4)
            self.jobs[job_id]["status"] = "complete"
            self.jobs[job_id]["report"] = report
        except Exception as e:
            self.jobs[job_id]["status"] = "error"
            self.jobs[job_id]["report"] = str(e)

    def get_status(self, job_id):
        return self.jobs.get(job_id, {"status": "not_found"})

    def get_report(self, job_id):
        job = self.jobs.get(job_id)
        if job and job["status"] == "complete":
            return job["report"]
        return None
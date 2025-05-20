from flask import Flask, request, jsonify, render_template
from job_manager import JobManager

app = Flask(__name__)
job_manager = JobManager()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/query", methods=["POST"])
def submit_query():
    data = request.json
    query = data.get("query", "")
    job_id = job_manager.create_job(query)
    return jsonify({"job_id": job_id})

@app.route("/api/status/<job_id>", methods=["GET"])
def get_status(job_id):
    return jsonify(job_manager.get_status(job_id))

@app.route("/api/report/<job_id>", methods=["GET"])
def get_report(job_id):
    report = job_manager.get_report(job_id)
    if report:
        return jsonify({"report": report})
    else:
        return jsonify({"message": "Report not ready or job not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

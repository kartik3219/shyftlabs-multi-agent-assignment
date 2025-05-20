class WriterAgent:
    def __init__(self):
        self.status = "idle"
        self.report = ""

    def run(self, analyzed_data):
        self.status = "writing"
        self.report = "# AI Research Report\n\n"
        self.report += f"{analyzed_data['summary']}\n\n"
        self.report += f"Citation: \n"
        for index, url in enumerate(analyzed_data["citations"]):
            self.report += f"{index+1}. "
            self.report += f"{url}\n"
        self.status = "complete"
        return self.report

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

class AnalysisAgent:
    def __init__(self):
        pass

    def merge_sources(self, sources):
        return "\n".join(source["text"] for source in sources)

    def summarize(self, sources, sentence_count=5):
        combined_text = self.merge_sources(sources)
        parser = PlaintextParser.from_string(combined_text, Tokenizer("english"))
        summarizer = TextRankSummarizer()
        summary = summarizer(parser.document, sentence_count)
        return " ".join(str(sentence) for sentence in summary)

    def run(self,sources):
        summary = self.summarize(sources)
        return {
            "summary": summary,
            "citations":(source["url"] for source in sources)
        }

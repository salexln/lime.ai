
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from enum import Enum


class AnalysisResponce(Enum):
    POSITIVE = 0
    NEGATIVE = 1
    NEUTRAL = 2

class SentimentAnalysis(object):
    def __init__(self):
        self._sentiment_analyzer = SentimentIntensityAnalyzer()

    def predict(self, text, debug=False):
        ss = self._sentiment_analyzer.polarity_scores(text)

        if debug:
            print(ss)
        if ss['compound'] > 0.00:
            return AnalysisResponce.POSITIVE
        elif ss['compound'] < 0.00:
            return AnalysisResponce.NEGATIVE
        else:
            return AnalysisResponce.NEUTRAL



if __name__ == "__main__":
    sentiment_analysis = SentimentAnalysis()
    print(sentiment_analysis.predict('worst product ever'))

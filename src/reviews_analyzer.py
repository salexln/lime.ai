from sentiment_analysis import SentimentAnalysis
from sentiment_analysis import AnalysisResponce

from collections import defaultdict

class ReviewAnalyzerResult(object):
    def __init__(self):
        self._pos = []
        self._neg = []

    def negative_results(self):
        return self._neg

    def negative_relust_count(self):
        return len(self._pos)

    def positive_results(self):
        return self._pos

    def positive_relust_count(self):
        return len(self._pos)

    def add_result(self, sentince, result):
        if result == AnalysisResponce.POSITIVE:
            self._pos.append(sentince)
        elif result == AnalysisResponce.NEGATIVE:
            self._neg.append(sentince)

    def print_result(self):
        print('Positive {}'.format(len(self._pos)))
        print('Nagative {}'.format(len(self._neg)))

    def print_with_value(self, number_of_values=3):
        print('Positive {}'.format(len(self._pos)))
        for i in range(number_of_values):
            print(self._pos[i])

        print('Nagative {}'.format(len(self._neg)))
        for i in range(number_of_values):
            print(self._neg[i])

class ReviewAnalyzer(object):
    def __init__(self, data_path):
        self._data_path = data_path
        self._result = {}
        self._sentiment_analysis = SentimentAnalysis()
        self._prepare_result()


    def _prepare_result(self):
        self._result['location'] = ReviewAnalyzerResult()
        self._result['price'] = ReviewAnalyzerResult()
        self._result['parking'] = ReviewAnalyzerResult()
        self._result['clean'] = ReviewAnalyzerResult()

    def analyze(self):
        with open(self._data_path, 'r') as input_file:
            lines = input_file.readlines()
            for sentince in line.split('.'):
                res = sentiment_analysis.predict(text=sentince)
                self._add_result(sentince=sentince,
                                 result=res)

    def _add_result(self, sentince, result):
        if HotelAttributes.location(sentince):
            self._result['location'].add_result(sentince=sentince,
                                                result=res)
        if HotelAttributes.price(sentince):
            self._result['price'].add_result(sentince=sentince,
                                             result=res)
        if HotelAttributes.parking(sentince):
            self._result['parking'].add_result(sentince=sentince,
                                             result=res)
        if HotelAttributes.location(sentince):
            self._result['clean'].add_result(sentince=sentince,
                                             result=res)

    def print_results(self):
        for k, v in self._result.iteritems():
            print(k + ':')
            v.print_result()

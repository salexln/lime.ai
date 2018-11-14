from sentiment_analysis import SentimentAnalysis
from sentiment_analysis import AnalysisResponce
from collections import defaultdict


class HotelAttributes(object):
    @staticmethod
    def location(str):
        locations = ['in', 'around','location']
        if any(x in locations for x in str.split(' ')):
            return True
        return False

    @staticmethod
    def price(str):
        prices = ['price', 'cheap','expensive']
        if any(x in prices for x in str.split(' ')):
            return True
        return False

    @staticmethod
    def parking(str):
        parking = ['parking', 'car']
        if any(x in parking for x in str.split(' ')):
            return True
        return False

    @staticmethod
    def cleanliness(str):
        clean = ['clean', 'neat','dirty']
        if any(x in clean for x in str.split(' ')):
            return True
        return False



def run():
    with open('../data/hotel.tsv', 'r') as input_file:
        lines = input_file.readlines()

        sentiment_analysis = SentimentAnalysis()
        result = {}
        result['location'] = {'pos':0, 'neg':0}
        result['price'] = {'pos':0, 'neg':0}
        result['parking'] = {'pos':0, 'neg':0}
        result['clean'] = {'pos':0, 'neg':0}

        for line in lines:
            res = sentiment_analysis.predict(line)

            if HotelAttributes.location(line):
                if res == AnalysisResponce.POSITIVE:
                    result['location']['pos'] +=1
                elif res == AnalysisResponce.NEGATIVE:
                    result['location']['neg'] +=1

            if HotelAttributes.price(line):
                if res == AnalysisResponce.POSITIVE:
                    result['price']['pos'] +=1
                elif res == AnalysisResponce.NEGATIVE:
                    result['price']['neg'] +=1

            if HotelAttributes.parking(line):
                if res == AnalysisResponce.POSITIVE:
                    result['parking']['pos'] +=1
                elif res == AnalysisResponce.NEGATIVE:
                    result['parking']['neg'] +=1

            if HotelAttributes.location(line):
                if res == AnalysisResponce.POSITIVE:
                    result['clean']['pos'] +=1
                elif res == AnalysisResponce.NEGATIVE:
                    result['clean']['neg'] +=1

        # import pdb; pdb.set_trace()
        for x, y in result.iteritems():
            print(x, y)








if __name__ == "__main__":
    run()

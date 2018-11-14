
from hotel_attributes import HotelAttributes
from reviews_analyzer import ReviewsAnalyzer





def run():
    reviews_analyzer = ReviewsAnalyzer(data_path='../data/hotel.tsv')
    reviews_analyzer.analyze()
    reviews_analyzer.print_results()


if __name__ == "__main__":
    run()

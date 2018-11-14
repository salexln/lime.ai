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

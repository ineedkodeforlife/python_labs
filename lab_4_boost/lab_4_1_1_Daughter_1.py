from lab_4_1_1_Parent import Car


class Tractor(Car):
    def __init__(self, tractor_name: str, oil_volume: int):
        Car.__init__(self, tractor_name, oil_volume)

    @staticmethod
    def mean_consumption(kilometer: (int, float)):
        if isinstance(kilometer, (int, float)):
            return f'Примерная трата бензина {kilometer * 40}'





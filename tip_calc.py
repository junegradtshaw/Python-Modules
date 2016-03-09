class TipOutCalc():
    def __init__(self, tip=0.18):
        self.tip = tip
        self.tip_array = []

    def add_to_total(self, bill):
        self.tip_array.append(self.tip * bill)

    def total_tips(self):
        return reduce(lambda x, y : x+y, self.tip_array)

if __name__ == '__main__':
    test_tc = TipOutCalc()
    test_tc.add_to_total(60.32)
    test_tc.add_to_total(51.28)
    print test_tc.total_tips()

def cal_F1(precision, recall):
    return 2 * ((precision * recall) / (precision + recall))

if __name__ == '__main__':
    print(cal_F1(86.4706, 99.2519))
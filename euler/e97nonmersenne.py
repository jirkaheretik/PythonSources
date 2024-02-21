import datetime
import sys

if __name__ == '__main__':
    print(f"Start: {datetime.datetime.now()}")
    sys.set_int_max_str_digits(3000000)
    hodnota = 28433 * 2**7830457 + 1
    print(f"After computing the value: {datetime.datetime.now()}")
    text = str(hodnota)
    print(f"Converted value to string: {datetime.datetime.now()}")  # +2 minutes(!!)
    print("Last 10 digits: " + text[-10:])
    # print(len(text))  # 2357207
    print(f"Finish: {datetime.datetime.now()}")
    sys.set_int_max_str_digits(4300)   # back to normal value

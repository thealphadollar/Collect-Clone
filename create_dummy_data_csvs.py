"""
methods to generate random data for testing
"""
import os
import csv
import string
import random
import datetime

import julian

WRITE_TO = "./collect-demo/dummy-input/"


class DummyGenerator:
    """
    class to encapsulate all random data generation methods
    """

    def __init__(self):
        """
        driver method to call all others
        """
        os.makedirs(WRITE_TO, exist_ok=True)
        self.for_ex_1()
        self.for_ex_2()
        self.for_ex_3()

    def for_ex_1(self):
        """
        generate csv file with random data (data1, data2, data3) for first example 1
        """

        csvData = [['data1', 'data2', 'data3']]
        for _ in range(100000):
            csvData.append([self.random_text_generator() for x in range(3)])
        self.writeCSV("exam1.csv", csvData)

    def for_ex_2(self):
        """
        generate csv file with random data (date, data) for second example 2

        NOTE: The dates are saved in Julian format to facilitate easy sorting
        """

        csvData = [['date', 'data']]
        date_1 = datetime.datetime(2015, 8, 1)
        date_2 = datetime.datetime(2017, 8, 1)
        date_1 = julian.to_jd(date_1, fmt='jd')
        date_2 = julian.to_jd(date_2, fmt='jd')

        for _ in range(18000000):
            csvData.append([date_1, self.random_text_generator()])
        for _ in range(18000000, 20000000):
            csvData.append([date_2, self.random_text_generator()])
        self.writeCSV("exam2.csv", csvData)

    def for_ex_3(self):
        """
        generate csv file with random data (name, phone) for example 3
        """

        csvData = [['name', 'phone']]

        for _ in range(10000):
            csvData.append([self.random_text_generator(), self.random_ph_nos()])
        self.writeCSV("exam3.csv", csvData)

    @staticmethod
    def random_text_generator(str_len=8):
        """
        generates random text (including upper case, lower case and digits) of 
        specified length

        :param str_len: length of random string, defaults to 8
        :param str_len: int, optional
        :return: random string
        :rtype: string
        """

        chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
        random_str_list = [random.choice(chars) for _ in range(str_len)]
        return "".join(random_str_list)

    @staticmethod
    def random_ph_nos(str_len=10):
        """
        generate random number with specified number of digits
        
        :param str_len: number of digits in the number, defaults to 10
        :param str_len: int, optional
        :return: random number
        :rtype: int
        """

        chars = string.digits
        random_num_list = [random.choice(chars) for _ in range(str_len)]
        return int("".join(random_num_list))

    @staticmethod
    def writeCSV(name, csvData):
        """
        write csv data to the file
        
        :param name: name of the file
        :type name: string
        :param csvData: data to be written
        :type csvData: list
        """

        with open(os.path.join(WRITE_TO, name), 'w+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(csvData)


if __name__ == "__main__":
    DummyGenerator()

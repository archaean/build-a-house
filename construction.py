import csv
import sys
from collections import defaultdict


class Construction():
    @staticmethod
    def read_data(file):
        '''
        @abstract method meant to be implemented by a sub-class

        :param file: a file object
        :return a list of tuples:
        '''
        raise NotImplementedError

    def __init__(self, file):
        self._data = self.__class__.read_data(file)

    def get_steps(self):
        '''
        Get the unique set steps need to complete the construction

        :return: list of strings
        '''
        _, c2 = zip(*self._data)
        return list(set(c2))

    def get_dependency_list(self):
        '''
        Get the list of construction dependencies

        :return: list of tuples
        '''
        return self._data

    def get_graph(self):
        '''
        Gets the graph representation (dictionary of nodes -> edges) of the construction as a dictionary

        :return: a dict of string -> set of string
        '''
        d = defaultdict(set)
        for x, y in self.get_dependency_list():
            d[y].add(x)
        return dict(d)


    def build(self):
        '''
        Constructs a linear order of build steps needed to construct a house

        :return: list of strings
        '''
        #TODO IMPLEMENT THIS METHOD
        return ['']

class CSV_Construction(Construction):
    '''
    >>> construction = CSV_Construction(open('data/house_steps.csv', 'rb'))
    >>> construction.get_steps()
    ['finishings', 'foundation', 'windows', 'roof', 'walls', 'electrical', 'plumbing', 'fixtures']
    '''
    @staticmethod
    def read_data(file):
        csvreader = csv.reader(file, skipinitialspace=True, delimiter=',', quoting=csv.QUOTE_NONE)
        next(csvreader, None) #Skip header
        return [(row[0], row[1]) for row in csvreader]

#TODO optionally create Construction object using data/house_step.txt file

def main():
    file = open(sys.argv[1], 'rb')
    construction = CSV_Construction(file)
    print 'Steps:', construction.get_steps()
    print 'Dependencies:', construction.get_dependency_list()
    print 'Graph:', construction.get_graph()
    print 'Build', construction.build()

if __name__ == '__main__':
    main()
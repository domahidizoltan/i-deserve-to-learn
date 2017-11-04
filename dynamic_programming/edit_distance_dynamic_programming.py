# http://www.ideserve.co.in/learn/edit-distance-dynamic-programming

from common.algorithm import levenshtein_distance

if __name__ == "__main__":
    source = 'INTENTION'
    destination = 'EXECUTION'
    distance = levenshtein_distance(source, destination)

    print("The minimum edit distance between the words {} and {} is: {}".format(source, destination, distance))

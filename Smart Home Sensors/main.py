import pickle
import sys

Threshold = 2


def main():
    argument1 = sys.argv[1]
    argument2 = sys.argv[2]
    try:
        open(argument1, 'rb')
        open(argument2, 'rb')

    except FileNotFoundError:
        print('Error: The files given as arguments are not valid.')
        return

    measurements_1 = read_file(argument1)
    measurements_2 = read_file(argument2)
    measurements_int1 = map_to_int(measurements_1)
    measurements_int2 = map_to_int(measurements_2)
    data_diff = find_faulty(measurements_int1, measurements_int2, Threshold)
    display_warnings(data_diff)


def read_file(filename):
    input_file1 = open(filename, 'rb')
    end_of_file = False
    data_measurements = {}
    while not end_of_file:
        try:
            data_measurements = pickle.load(input_file1)
        except EOFError:
            end_of_file = True
    return data_measurements


def map_to_int(measurements):
    for key in measurements:
        string_value = (measurements[key])
        integer_value = int(string_value[:-1])
        measurements[key] = integer_value
    return measurements


def find_faulty(primary, secondary, threshold):
    data_set = set()
    for key_primary, key_secondary in zip(primary, secondary):
        difference = abs(primary.get(key_primary) - secondary.get(key_secondary))
        if difference > threshold:
            data_set.add(key_primary)
    return data_set


def display_warnings(faulty_sensors):
    print('Analyzis of the provided files is complete.')
    print('-------------------------------------------')
    print()
    print('The following sensors differ more than 2°:')
    for room in faulty_sensors:
        print(room)


if __name__ == '__main__':
    main()
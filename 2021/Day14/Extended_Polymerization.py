from collections import defaultdict

def make_pairs(p):
    """
    Creates a dictionary to count the occurrences of adjacent character pairs in a given string.

    Args:
        p (str): The input string (polymer).

    Returns:
        defaultdict: A dictionary where the keys are pairs of adjacent characters 
                     and the values are their counts in the string.
    """
    pairs = defaultdict(int)
    for i in range(1, len(p)):
        pairs[p[i - 1] + p[i]] += 1
    return pairs


def parse_input(file):
    """
    Parses the input file to extract the polymer template and pair insertion rules.

    Args:
        file (str): The path to the input file.

    Returns:
        tuple: A dictionary of pair insertion rules, a dictionary of initial pairs with their counts, 
               and the first character of the polymer.
    """
    dic = {}
    try:
        with open(file, "r") as file1:
            polymer = file1.readline().strip()
            rules = file1.readlines()

        for line in rules[1:]:
            tmp = line.split(' -> ')
            insertion_char = tmp[1].strip()

            dic[tmp[0]] = [tmp[0][0] + insertion_char, insertion_char + tmp[0][1]]

    except :
        print("f"Error: The file '{file}' was not found."")
        raise
    except IndexError:
        print("Error: The file structure is incorrect, missing or incomplete rules.")
        raise
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise

    return dic, make_pairs(polymer), polymer[0]


def extended_poly(file, steps):
    """
    Simulates polymer growth over a specified number of steps based on pair insertion rules.

    Args:
        file (str): The path to the input file containing the polymer template and rules.
        steps (int): The number of steps to simulate the polymer growth.

    Returns:
        int: The difference between the most common and least common elements in the final polymer.
    """
    try:
        dic, pairs, first_char = parse_input(file)

        for _ in range(steps):
            tmp = pairs.copy()
            for val in tmp.keys():
                if val not in dic or tmp[val] == 0:
                    continue
                k = tmp[val]
                pairs[val] -= k
                np = dic[val]
                pairs[np[0]] += k
                pairs[np[1]] += k

        c = defaultdict(int)
        for key, value in pairs.items():
            c[key[-1]] += value

        return max(c.values()) - min(c.values())
    except ValueError:
        print("Error: The number of steps should be a valid integer.")
        raise
    except Exception as e:
        print(f"An unexpected error occurred during polymer simulation: {e}")
        raise


# User input for the file and number of steps with error handling
try:
    file = input()
    steps = int(input())
    print(extended_poly(file, steps))
except ValueError:
    print("Invalid input: Please enter a valid integer for the number of steps.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

import math

def trialdivision(n): # returns True if n is prime
    if n == 1:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def get_combinations(l, n): # returns the possible combinations of size n from a list l (l choose n)

    solutions = []

    if n == 1:
        solutions = [[i] for i in l]

    for i in range(len(l) - 1):

        sub_solutions = get_combinations(l[i + 1:], n - 1)

        for j in range(len(sub_solutions)):
            solutions.append([l[i]] + sub_solutions[j])

    return solutions

def get_permutations(l): #returns the possible permutations of a list l (l Permute l)

    if len(l) == 1:
        return [l]

    solutions = []

    for i in range(len(l)):

        sub_solutions = get_permutations(l[:i] + l[i + 1:])

        for j in range(len(sub_solutions)):
            solutions.append([l[i]] + sub_solutions[j])

    return solutions

def concatenate_to_int(l): #concatenates a list of integers l into a single integer, returns integer
    answer = 0

    for i in range(len(l)):
        answer += (l[i] * (10 ** (len(l) - i - 1)))

    return answer

def concatenate_to_str(l): #concatenates a list of integers into a string, returns string
    answer = ''

    for i in range(len(l)):
        answer = answer + str(l[i])

    return answer

def initialize_prime_permutations_dictionary(l, n): #returns a dictionary which stores the number of prime permutations of a freely concatenated set of n digits chosen from list l
    prime_permutations = dict()
    combinations = get_combinations(l, n)

    for i in range(len(combinations)):
        permutations = get_permutations(combinations[i])
        primes_count = 0

        for j in range(len(permutations)):
            if trialdivision(concatenate_to_int(permutations[j])):
                primes_count += 1

        prime_permutations[concatenate_to_str(combinations[i])] = primes_count

    return prime_permutations

def initialize_prime_permutations_list(ref): #what is this base business
    prime_permutations_list = []

    for i in range(1, len(ref) + 1):
        prime_permutations_list.append(initialize_prime_permutations_dictionary(ref, i))

    return prime_permutations_list

def get_partitions(n): #returns a list containing the partitions of a number
    solutions = []

    if n == 0:
        return []

    if n == 1:
        return [[1]]

    for i in range(n):
        sub_partitions = get_partitions(i)

        if len(sub_partitions) == 0:
            solutions.append([n - i])

        for j in range(len(sub_partitions)):
            if n - i >= sub_partitions[j][0]:
                solutions.append([n - i] + sub_partitions[j])

    return solutions

def update_reference(combo, cat): #removes already-used digits from the reference list when recursively generating one possible freely concatenated set of digits using get_spec_part()

    for i in range(len(combo)):
        cat.remove(combo[i])

    return cat

def get_spec_part(partition, ref): #given a partition of the reference, returns a list of the possible unique ways of dividing the digits between partitions
    ans = []

    if partition[0] == 1:
        return [ref]

    elif len(partition) == 1:
        return [[concatenate_to_int(ref)]]

    combinations = get_combinations(ref, partition[0])

    for i in range(len(combinations)):
        dummy_ref = ref.copy()

        r = get_spec_part(partition[1:], update_reference(combinations[i], dummy_ref))

        for j in range(len(r)):

            if partition[0] != partition[1] or concatenate_to_int(combinations[i]) < r[j][0]:
                ans.append([concatenate_to_int(combinations[i])] + r[j])

    return ans

def get_all_spec_parts(partitions, ref): #given all possible partitions of the reference, runs get_spec_part for each one of them and combines it all into a big list
    ans = []

    for i in range(len(partitions)):
        ans.append(get_spec_part(partitions[i], ref))

    return ans

def count_prime_configs(prime_permutations_list, spec_parts_list): #counts how many free concatenations of the digits there are using the reference dictionary
    count = 0

    for i in range(len(spec_parts_list)):
        for j in range(len(spec_parts_list[i])):
            current_count = 1

            for k in range(len(spec_parts_list[i][j])):
                current_count *= prime_permutations_list[len(str(spec_parts_list[i][j][k])) - 1][str(spec_parts_list[i][j][k])]

            count += current_count

    return count


reference = [1, 2, 3, 4, 5, 6, 7, 8, 9]

partitions = get_partitions(len(reference))
prime_permutations_list = initialize_prime_permutations_list(reference)
spec_parts_list = get_all_spec_parts(partitions, reference)
answer = count_prime_configs(prime_permutations_list, spec_parts_list)
print(answer)

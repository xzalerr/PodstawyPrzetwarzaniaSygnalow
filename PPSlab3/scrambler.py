import random


class LFSR:
    def __init__(self, seed):
        self.seed = seed
        self.state = seed.copy()

    def shift(self):
        feedback = self.state[-1] ^ self.state[-2]
        self.state = [feedback] + self.state[:-1]

    def generate(self):
        self.state = self.seed.copy()
        while True:
            self.shift()
            yield self.state[-1]


class Scrambler:
    def __init__(self, lfsr):
        self.lfsr = lfsr

    def scramble(self, data):
        scrambled_data = []
        for bit in data:
            random_bit = next(self.lfsr.generate())
            scrambled_bit = (bit + random_bit) % 2
            scrambled_data.append(scrambled_bit)
        return scrambled_data

    def descramble(self, data):
        descrambled_data = []
        for bit in data:
            random_bit = next(self.lfsr.generate())
            descrambled_bit = (bit - random_bit) % 2
            descrambled_data.append(descrambled_bit)
        return descrambled_data


class Transmission:
    def generate_data(length):
        return [random.randint(0, 1) for _ in range(length)]

    def introduce_noise(data, max_same_len, probability):
        noise_data = []
        same_len = 0
        last_bit = None
        for bit in data:
            if bit == last_bit:
                same_len += 1
                if same_len >= max_same_len or random.random() < probability:
                    last_bit = bit
                    bit = 1 - bit
                    same_len = 0
            else:
                last_bit = bit
                same_len = 0
            noise_data.append(bit)
        return noise_data

    def find_num_errors(original, received):
        return sum(bit1 != bit2 for bit1, bit2 in zip(original, received))


lfsr = LFSR([1, 0, 0, 1])
generator = lfsr.generate()
for _ in range(16):
    print(next(generator), end=' ')
print()
scrambler = Scrambler(lfsr)
data = [1, 0, 1, 0, 1, 0, 1, 0]#Transmission.generate_data(20)

print("Original data: ", data)

scrambled = scrambler.scramble(data)
print("Scrambled data: ", scrambled)

noise_no_scrambled = Transmission.introduce_noise(data, 3, 0.05)
noise_scrambled = Transmission.introduce_noise(scrambled, 3, 0.05)

print("Received data with no scrumble: ", noise_no_scrambled)
print("Number of errors: ", Transmission.find_num_errors(data, noise_no_scrambled))

descrambled = scrambler.descramble(noise_scrambled)
print("Received data with scrumble: ", descrambled)
print("Number of errors: ", Transmission.find_num_errors(data, descrambled))
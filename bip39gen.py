#!/usr/bin/env python3

import numpy as np
import argparse
import sys
import subprocess

# Function to convert a bit_string to a numpy list array
# (one dimensional vector)
def stringToNumpy(binary):
    lennum = len(binary)
    ns = np.zeros((1,lennum), dtype=int)
    
    for i,bit in enumerate(binary):
        ns[0,i] = int(bit)

    return ns

def numpyToString(binary):
    res = ""

    for b in binary[0]:
        res += "1" if b else "0"

    return res

# Function to convert hexadecimal number to binary with trailing zeros
# if necessary
def hexToBin(hex_data, num_of_bits):
    scale = 16 # equals to hexadecimal

    return bin(int(hex_data, scale))[2:].zfill(num_of_bits)



parser = argparse.ArgumentParser(prog='bip39gen', description="""Generate a Bitcoin mnemonic seed phrase 
                                 from a random binary string according to bip39""")
parser.add_argument("-b", "--binary", help="A BIG binary number that will be converted to a mnemonic seed phrase.\
                                    Default length=256(264-8) for a 24 word bip39 seed", type=str)
parser.add_argument("-s","--short", help="convert to 12 word seed",action="store_true")
parser.add_argument("-l", "--lang", help="specify the language of the seed phrase (Default=en)",
                    type=str, choices=["en","fr","jp","kr","it"], default="en")
parser.add_argument("-g", "--random", help="""use a pseudo-random binary number (not recommended,
                                            use only for testing)""", action="store_true")
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
parser.add_argument("-f", "--file"   , help="Take a file as input instead of binary", type=str, action="store",
                    default=None)
args = parser.parse_args()



lennum = 256
if args.short:
    lennum = 124

if not(args.random) and not(args.file):

    if args.verbose: print(f"length={len(args.binary)}")


elif args.random:
    rg = np.random.default_rng(1)
    bools = rg.random((1,lennum)) < 0.5

    args.binary = numpyToString(bools)

    print(args.binary)

elif args.file:
    args.binary = ""
    with open(args.file, "r") as file:
        while c := file.read(1):
            if c == "1" or c == "0":
                args.binary += c

    if args.verbose:
        print(args.binary)
        print(f"length={len(args.binary)}")

# Check the length of the input
if len(args.binary) != lennum:
    sys.exit("error: bad length for input 'binary'")



# Check if it is a binary number
for i in args.binary:
    if i != "1" and i != "0":
        print(i)
        sys.exit("error: not a binary number")
        
    # if args.verbose: print(i)

# STEP 2: Calculate the checksum
bs = subprocess.Popen(("echo",args.binary), stdout=subprocess.PIPE)
output = subprocess.check_output(('shasum', '-a','256','-0'), stdin=bs.stdout)
if args.verbose: print(output)

checksum_hex = str(output)[2:4]

checksum_bin = hexToBin(checksum_hex, 8)
if args.verbose: print(checksum_bin)

my_bits = np.hstack((stringToNumpy(args.binary), stringToNumpy(checksum_bin)) )
if args.verbose: print(my_bits)


# STEP 3: Converting binary to decimal
nwords = 24
if args.short:
    nwords = 12
my_bits = my_bits.reshape(nwords,11)
w       = np.array([1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1], dtype=int)

my_decimals = my_bits @ w
if args.verbose: print(my_decimals)

# STEP 4: convert decimal to bip39 words
file_paths = {
  "en": "english.txt",
  "fr": "french.txt",
  "jp": "japanese.txt",
  "kr": "korean.txt",
  "it": "italian.txt"
}

bwords = []

with open("./bip-0039/" + file_paths[args.lang], "r") as file:
    while line := file.readline():
        bwords.append(line.rstrip())

if args.verbose: print(my_decimals.shape)

seed_words = []

for windex in my_decimals:
    seed_words.append(bwords[windex])

if args.verbose: print(my_decimals.dtype)

print(seed_words)

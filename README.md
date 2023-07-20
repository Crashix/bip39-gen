# BIP39gen
## Description
Bitcoin seed word generator.

Generate a 24 (or 12) word seed phrase from a big random binary number.

Those words can then be used on a bitcoin wallet (compatible with BIP39) in order to generate your very own bitcoin private key.

The favorite wallet for this project is [sparrow] and this is where everything will be tested on.

## Motivation
[@parman_the] made a good [blog post][arman_dicev2] about generating bitcoin private key from scratch with only pencil, paper and dice.

IMO this is the only way to generate bitcoin seed phrase safely because every other alternative requires trust:

- Trust in the security of your computer (no hacker and no keylogger)
- Trust in the hardware wallet manufacturer

However, out of convenience I thought that step 2 to 4 can be automated and made a little python script that I kept adding features for fun.

That is why you are expected to run this script on an **air-gapped** computer.


## Usage
After you get 256 binary digits manually like described in this [blog post][arman_dicev2], you can run `bip39gen.py` entering them like in this example:

```sh
$ python bip39gen.py -b 1010111100111000000011110110001111010111101001010010001011001111011110100011000010100011111100100010100011110001110101000110011111110000101000110001010111010001010011111110101001010011110110110110000001101111010011000001110101101001000010001000010000100111
```
Output:
```sh
['quality', 'scatter', 'suggest', 'quantum', 'fall', 'guilt', 'trip', 'behave', 'vendor', 'elegant', 'insect', 'soup', 'any', 'memory', 'early', 'wool', 'fatigue', 'swallow', 'bridge', 'oblige', 'story', 'lounge', 'awesome', 'wage']
```

For more help:
```sh
python bip39gen.py -h
```


## Don't trust verify
In this repository, every commit must be PGP-signed.

**WIP:** I must find a way to publish my public pgp key (for now just trust github).



[//]: # (Reference links)

[arman_dicev2]: <https://armantheparman.com/dicev2/>
[@parman_the]: <https://twitter.com/parman_the/status/1679363834769993729>
[//////]: # (By the way, did you know that it was this song that inspired ZUN to make Septette for the Dead Princess - especially movement 3. Here's a little gift for you: https://www.youtube.com/watch?v=EBx_1WN8PlA               )
[//////]: # (But anyway, why are you reading the comment section? Get out of here!)

[sparrow]: <https://sparrowwallet.com/>

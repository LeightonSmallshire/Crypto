# Crypto
A pure-python implementation of Diffie-hellman as a proof, and my own modification using a variation on Conway's game of life as the base of the one-way function used.

This is meant as a _proof-of-concept_ and not as a practical solutions.

For any practical purpose, the automata's rules should be refined, the board's initial state should specifically not be symmetric or sparse and some check should be put in place for repeating cycles of states.

# My understanding of DH-style key exchange
My generalized understanding;

 Alice and Bob generate private keys A and B respectively.
 
 Both Alice and Bob start at the same starting state G, and 'step' a number of times -their respective private keys.
 
 When Alice and Bob exchange keys, the starting state G is substituted for the other's public key and 'stepped' their own private key's number of times.
 
 When done, the starting state G has been put through the function or 'stepped' A + B number of times in total, regardless of whether it was stepped A times or B times first.
 
They both arrive at the same, and hence shared, secret.

Therefore, as long as a function is difficult to reverse, the initial states are safe to be revealed to the public and it being run A times _then_ B times is always equivalent to B times _then_ A times, then the function can be used in this scenario.
_This does not necessarily mean that the function will provide cryptographic security.
E.g. Base + 1(n times) provides security only from those unable to subtract two numbers_

# Game of life
The cell will be alive next cycle if it has 2 or 3 neighbours, or 4 if it is alive.


# Crypto

A pure-python implementation of Diffie-hellman as a proof, and my own modification using a variation on Conway's game of
 life as the base of the one-way function used.

This is meant as a proof-of-concept and not as a practical solutions.

For any practical purpose, the autometa's rules should be refined, the board's initial state should specifically not be 
symmetric or sparse and some check should be put in place for repeating cycles of states.

# My understanding of DH key exchange;
Alice wants to establish a shared secret with Bob and decides to use DH key sharing.
Alice picks a generator G, prime P and private key A_private.
Alice uses this information to create her public key A_public using the one-way function  public = G ** private (mod P)

--Alice sends her public key to Bob, along with G and P--

Bob generates his own private keys
Bob generates his own public and private keys with the same function, G and P.

--Bob sends his public key only back to Alice--

Now both Alice and Bob have their own private keys and the agreed upon values of G and P.
--secret = G ** public (mod P)
Alice and Bob now generate their secrets, Alice substituting G for Bob's public key and vice versa.
They both arrive at the same, and hence shared, secret.


My generalized understanding;
 Alice and Bob generate private keys A and B respectively.
 Both Alice and Bob start at the same starting point G, and 'step' a number of times -their private respecting keys.
 
 When Alice and Bob exchange keys, the starting point G is substituted for the other's public key and 'stepped' their
  own private key's number of times.
 
 When done, the starting point G has been put through the function or 'stepped' A + B number of times in total,
  regardless of whether it was stepped A times first or second. 
  
 Therefore, as long as a function is difficult to reverse, the initial states are safe to be revealed to the public and
  it being run A times _then_ B times is always equivalent to B times then A times, then the function can be 
  
 

# Game of life

Custom rules;
The cell will be alive next cycle if it
  has 2 or 3 neighbours
  is alive and has 4 neighbours

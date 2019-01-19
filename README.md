In programmers life algorithms and data structures is most important subject if they want to go out in the programming world and make some bucks. 

![time](https://he-s3.s3.amazonaws.com/media/uploads/c950295.png)
![graph](https://he-s3.s3.amazonaws.com/media/uploads/317c55e.png)

## Sort Algorithms
Sorting is the most heavily studied concept in Computer Science. Idea is to arrange the items of a list in a specific order. Though every major programming language has built-in sorting libraries, it comes in handy if you know how they work. Depending upon requirement you may want to use any of these.

- [Bubble sort](https://www.hackerearth.com/practice/algorithms/sorting/bubble-sort/tutorial/)
- [Merge Sort](https://www.hackerearth.com/practice/algorithms/sorting/merge-sort/tutorial/)
- [Selection Sort](https://www.hackerearth.com/practice/algorithms/sorting/selection-sort/tutorial/)
- [Insertion Sort](https://www.hackerearth.com/practice/algorithms/sorting/insertion-sort/tutorial/)
- [Quick Sort](https://www.hackerearth.com/practice/algorithms/sorting/quick-sort/tutorial/)
- [Bucket Sort](https://www.hackerearth.com/practice/algorithms/sorting/bucket-sort/tutorial/)
- [Heap Sort](https://www.hackerearth.com/practice/algorithms/sorting/heap-sort/tutorial/)
- [Counting Sort](https://www.hackerearth.com/practice/algorithms/sorting/counting-sort/tutorial/)
- [Radix Sort](https://www.hackerearth.com/practice/algorithms/sorting/radix-sort/tutorial/)

More importantly one should know when and where to use them.

- Applications
  - Sorting by price, popularity etc in e-commerce websites

## Search Algorithms

- Binary Search (in linear data structures)

  Binary search is used to perform a very efficient search on sorted dataset. The time complexity is O(log2N). Idea is to repeatedly divide in half the portion of the list that could contain the item, until we narrow it down to one possible item. Some applications are:

  When you search for a name of song in a sorted list of songs, it performs binary search and string-matching to quickly return the results.

- Depth/Breadth First Search (in Graph data structures)

- Applications
  - Used by search engines for web-crawling
  - Used in artificial intelligence to build bots, for instance a chess bot
  - Finding shortest path between two cities in a map and many other such applications
  
## Hashing

Hash lookup is currently the most widely used technique to find appropriate data by key or ID. We access data by its index. Previously we relied on Sorting+Binary Search to look for index whereas now we use hashing.

The data structure is referred as Hash-Map or Hash-Table or Dictionary that maps keys to values, efficiently. We can perform value lookups using keys. Idea is to use an appropriate hash function which does the key -> value mapping. Choosing a good hash function depends on the scenario.

- Applications:
  - In routers, to store IP address -> Path pair for routing mechanisms
  - To perform the check if a value already exists in a list. Linear search would be expensive. We can also use Set data structure for this operation.
  
## Dynamic Programming

Dynamic programming (DP) is a method for solving a complex problem by breaking it down into simpler subproblems. We solve the subproblems, remember their results and using them we make our way to solving the complex problem, quickly.

  - writes down "1+1+1+1+1+1+1+1 =" on a sheet of paper* What's that equal to?
  - counting* Eight!
  - writes down another "1+" on the left* What about that?
  - quickly* Nine!
  - How'd you know it was nine so fast?
  - You just added one more
  - So you didn't need to recount because you remembered there were eight! Dynamic Programming is just a fancy way to say 'remembering stuff to save time later'

- Applications:
  - There are many DP algorithms and applications but I'd name one and blow you away, Duckworth-Lewis method in cricket.
  
## Exponentiation by squaring

Say you want to calculate 232. Normally we'd iterate 32 times and find the result. What if I told you it can be done in 5 iterations?

Exponentiation by squaring or [Binary exponentiation](https://www.hackerearth.com/practice/notes/mod-integer-exponentiation-useful-in-competetive-programming/) is a general method for fast computation of large positive integer powers of a number in O(log2N). Not only this, the method is also used for computation of powers of polynomials and square matrices.

- Application:
  - Calculation of large powers of a number is mostly required in RSA encryption. RSA also uses modular arithmetic along with binary exponentiation.
  
## String Matching and Parsing

Pattern matching/searching is one of the most important problems in Computer Science. There have been a lot of research on the topic but we'll enlist only two basic necessities for any programmer.

- KMP Algorithm (String Matching)
  - Knuth-Morris-Pratt algorithm is used in cases where we have to match a short pattern in a long string. For instance, when we Ctrl+F a keyword in a document, we perform pattern matching in the whole document.

- Regular Expression (String Parsing)
  - Many times we have to validate a string by parsing over a predefined restriction. It is heavily used in web development for URL parsing and matching.

## Primality Testing Algorithms

There are deterministic and probabilistic ways of determining whether a given number is prime or not. We’ll see both deterministic and probabilistic (nondeterministic) ways.

- Sieve of Eratosthenes (deterministic)
If we have a certain limit on the range of numbers, say determine all primes within range 100 to 1000 then Sieve is a way to go. The length of the range is a crucial factor because we have to allocate a certain amount of memory according to the range.

For any number n, incrementally testing up to sqrt(n) (deterministic)

In case you want to check for few numbers which are sparsely spread over a long range (say 1 to 1012), Sieve won't be able to allocate enough memory. You can check for each number n by traversing only up to sqrt(n) and perform a divisibility check on n.

- Fermat primality test and Miller–Rabin primality test (both are nondeterministic)
Both of these are compositeness tests. If a number is proved to be composite, then it sure isn’t a prime number. Miller-Rabin is a more sophisticated one than Fermat’s. In fact, Miller-Rabin also has a deterministic variant, but then it's a game of trade between time complexity and accuracy of the algorithm.

- Application:
  - The single most important use of prime numbers is in Cryptography. More precisely, they are used in encryption and decryption in RSA algorithm which was the very first implementation of Public Key Cryptosystems
Another use is in Hash functions used in Hash Tables

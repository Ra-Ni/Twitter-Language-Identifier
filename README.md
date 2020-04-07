# Twitter-Language-Identifier
A bayesian classifier for languages used in tweets


# PLEASE READ
- The algorithm automatically catches zero divisions and fixes them by using a 1e-64 modifier on the numerator/denominator.
See corpus.py and evaluator.py

- Some how the locale settings are different from each of our 
machines and so we get different isalpha() values per machine
My machine (running us_UTF-8 Arch Linux) saw isalpha as 125k characters

- Our custom model is called vocabulary 5 (we can change that in the future)
Vocabulary 5 is called AccentVocabulary

- I was told by Andres that we did not need to compute the prior
probabilities of each character. I guess it was wrong to think so,
since I received news today that it was required to have prior probabilities.
This wasn't a fun time trying to switch our architecture, so please be mindful that we tried our best

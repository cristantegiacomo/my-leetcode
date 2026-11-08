class Solution:

  def countValidSubstrings(self, s: str) -> int:
    ans = 0
    last_invalid = None  # Nessun "abc" ancora trovato

    for i in range(len(s)):
        if i >= 2 and s[i - 2 : i + 1] == "abc":
            last_invalid = i - 2

        if last_invalid is None: # attenzione if not last_invalid considera 0 come "not"
            ans += i + 1
        else:
            ans += i - last_invalid   
             #è come fare ans += i+1 e poi ans -= 1 (abc) e poi tutte le stringhe prima di a che quindi contengono quell'abc
            
    return ans

    # aabcbabc
    # a | aa, a, | aab, ab, b | aabc, abc, bc, c
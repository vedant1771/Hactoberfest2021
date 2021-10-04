"""
Vikas Ukani
- A Software Engineer
- https://github.com/vikas-ukani
- https://www.linkedin.com/in/vikas-ukani-a02499167/
"""


"""
Checking is anagram or not
return boolean
"""
def is_anagram(s: str, t: str) -> bool:
            s = sorted(s)
            t = sorted(t)
            return s == t


if __name__ == "__main__":
    print(is_anagram("tea", "eat"))

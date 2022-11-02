"""
Replace all vowel to exclamation mark in the sentence. aeiouAEIOU is vowel.

Examples
replace("Hi!") === "H!!"
replace("!Hi! Hi!") === "!H!! H!!"
replace("aeiou") === "!!!!!"
replace("ABCDE") === "!BCD!"
"""

import re


def replace_exclamation(s):
    match_obj = re.compile("[aeiou]", flags=re.IGNORECASE)
    new_s = re.sub(match_obj, '!', s)

    return new_s

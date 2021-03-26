# Whiteboard Template

## Problem Domain

- Write a function to determine if a given string is full of unique characters.
- INPUT: string
- OUTPUT: Boolean

## Edge Cases

- spaces dont count
- characters are not case sensitive
- no punctuation

## Big O

- Time: O(n) - takes as long as the string is minus any characters after the first repeated one.
- Space: O(n+m) - creating a list and taking in a string.

## Verification

- The quick brown fox jumps over the lazy dog	FALSE
- I love cats	TRUE
- Donald the duck	FALSE
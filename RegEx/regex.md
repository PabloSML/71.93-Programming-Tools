# Regular Expressions Example

## Text to recognize:
- 1234567890
- 123-456-7890
- 123 456 7890
- (123) 456-7890
- +54 123 456 7890

## Regular Expressions
- \d{10}
- \d{3}-?\d{3}-?\d{4}
- \d{3}[ -]?\d{3}[ -]?\d{4}
- (\d{3})[ -]?(\d{3})[ -]?(\d{4})
  - $1$2$3
-  \(?(\d{3})\)?[ -]?(\d{3})[ -]?(\d{4})
-  (?:(\+\d{1,2})[ -])?\(?(\d{3})\)?[ -]?(\d{3})[ -]?(\d{4})
   - $1$2$3$4
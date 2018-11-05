# Twoee
Because Thue isn't bad enough

## A note on backwards compatability
This is not 100% backwards compatible. We have "improved" it.

## Design Aims (not implemented)

```twoee
This is a comment (any text without an operator)
Yes twoee has comments

Replace a with b
a::=b

Replace a with inputed text
a::=:::

Replace a with b and output c
a::=b~~~c

Replace a with inputed text print c
a::=:::~~~c

This will define the data string
;;=a
```

## Operator list


### All possible operators 

#### Definition Operators
```
    This defines a command
    ::=

    This defines the data string
    ;;=
```
#### Control Operator
```
    This tells the interpreter to take an input from the user
    :::

    Prompted input
    ~::Prompt

    This outputs the text following it (text is treated as a literal)
    ~~~
```
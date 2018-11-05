# Twoee
Because Thue isn't bad enough

## A note on backwards compatability and testing
This is not 100% backwards compatible. We have "improved" it.
Nor have we tested this any further than the included designAimsExample.t2 file.

## Design Aims (Implemented)

```twoee
This is a comment (any text without an operator)
Yes Twoee has comments

Replace a with b
a::=b

Replace a with inputed text
a::=:::

Replace a with b and output c
a::=b~~~c

Replace a with inputed text print c
a::=:::~~~c

Replace a with prompted input
a::=~::Put your string here

This will define the data string
;;=a
```

## Design Aims (Unimplemented)

```twoee
Proper implementation of literal and non literal operators
i.e. not have such a hacky fix for making ~~~ run after :::
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

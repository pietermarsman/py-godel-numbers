# py-godel-numbers

This project is a Python implementation of Gödel numbers as explained in
the book
[Gödel's proof](https://z-library.rs/book/5250426/143f37/go-dels-proof.html)
by Hofstadter, Nagel and Newman. Gödel numbers are a cool and simple idea.
And I have used this project to deepen my understanding of the it.

## What are Gödel numbers?

Gödel numbers are a *systematic enumeration* of *statements* of the *formal
calculus* "PM". In this sentence, systematic enumeration means that it can
give a specific number to every statement. A statement is something like
"zero equals zero", "every number has a successor" or more complicated (and
useful statements). The formal calculus is a way to write down all these
statements using a limited number of distinct characters.

To do this, PM consists of constants, numerical variables, sentential
variables and predicate variables. These are the 12 constants, each of them
is linked to a unique Gödel number.

| Constant sign | Gödel number | Interpretation   |
|---------------|--------------|------------------|
| `~`           | $1$          | Not              |
| `V`           | $2$          | Or               |
| `⊃`           | $3$          | If ... then ...  |
| `∃`           | $4$          | There is a ...   |
| `=`           | $5$          | Equals           |
| `0`           | $6$          | Zero             |
| `s`           | $7$          | Successor of     |
| `(`           | $8$          | Punctuation mark |
| `)`           | $9$          | Punctuation mark |
| `,`           | $10$         | Punctuation mark |
| `+`           | $11$         | Plus             |
| `*`           | $12$         | Times            |

With the Gödel number all the constant signs are uniquely identified. The `~`
is identified by $1$. The `+` is the same as $11$.

Not only single characters can be translated into Gödel number. A multi
character statement is translated to a unique Gödel number by adding
powers of subsequent primes. The $n$'th character is represented by the
$n$th prime to the power of the Gödel number of that character. For example,
`0=0` is the same as $2^6 + 3^5 + 5^2 = 332$. This is the only number for
this statement, and this is the only statement for this number.

Besides constants, there are numerical variables. Numerical variables in a
statement can be substituted by any numeric value. That way, a numerical
variable can be used to state something about all numbers. There are three
numerical variables (in this project). Each of them is linked to a unique
subsequent prime numbers higher than 12.

| Numerical variable | Gödel number | Possible substitution |
|--------------------|--------------|-----------------------|
| `x`                | $13$         | `0`                   |
| `y`                | $17$         | `s0`                  |
| `z`                | $19$         | `y`                   |

So writing `x` is exactly the same as $13$, $19$ is exactly the same as writing
`z`. And writing `x=s0` is the same as $2^{13} + 3^5 + 5^7 + 7^6 = 204209$. Like
with constants, every statement with numerical variables is uniquely identified
by a Gödel number and every Gödel number identifies a single statement.

There are also sentential variables. These can be substituted by any statement
(or sentence) of constants and numerical variables. That way, a sentential
variable can be used to state something about all numerical statements. There
are three sentential variables (again, in this project). The sentential
variables are linked to the squares of prime numbers higher than 12.

| Sentential variable | Gödel number  | Possible substitution |
|---------------------|---------------|-----------------------|
| `p`                 | $13*13 = 169$ | `0=0`                 |
| `q`                 | $17*17 = 289$ | `(∃x)(x=sy)`          |
| `r`                 | $19*19 = 361$ | `p ⊃ q`               |

With these, writing `p` is exactly the same as $169$. And `(∃x)(x=sy)` is
identified by
$2^8 + 3^{13} + 5^{13} + 7^9 + 11^8 + 13^{13} + 17^5 + 19^7 + 23^{17} + 29^9 = 141050039878047593796013$.
A very big, yet unique number for this statement. Like with numerical variables,
every statement with sentential variables is uniquely identified by a Gödel
number and every Gödel number identifies a single statement.

And last but not least, there are predicate variables. These can be substituted
by any statement of constants, numerical variables or sentential variables.
That way, a predicate variable can be used to state something about all
statements. There are three predicate variables (again, in this project).
The predicate variables are linked to cubes of the prime numbers higher
than 12.

| Sentential variable | Gödel number  | Possible substitution |
|---------------------|---------------|-----------------------|
| P                   | $13^3 = 2197$ | `x=sy`                |
| Q                   | $17^3 = 4913$ | `~(x=ss0xy)`          |
| R                   | $19^3 = 6859$ | `(∃z)(x=y+sz)         |

With these, writing `P` is exactly the same as $2197$. And writing `P⊃PVQ` is
identified by $2^{2197} + 3^3 + 5^{2197} + 7^2 + 11^{4913} = $
[a number with 5117 decimal digits]

Writing these statements is interesting, but writing a sequence of statements
allows to write proofs. Suppose there is a sequence of two statements, the
first one with Gödel number $m$ and the second one with Gödel number $n$. The
Gödel number for the sequence is than $2^m + 3^n$. Hence, again the Gödel
numbers of the parts are the powers of subsequent primes.

## So why would do this?

To proof a point. Gödel used this enumeration to proof that no formal logic
can proof everything that is true, and be consistent.

## And what does this project do?

This project just *Gödelizes* statements of the formal calculus "PM".

```python
>>> from py_godel_numbers import godelize
>>> godelize("~")
1
>>> godelize("0=0")
243000000
```

And it *de-Gödelizes* these numbers into statements of PM.

```python
>>> from py_godel_numbers import degodelize
>>> degodelize(1)
"1"
>>> degodelize(243000000)
"0=0"
```

And ofcourse you can check that both functions are unique for every input.

```python
>>> from py_godel_numbers import godelize, degodelize
>>> degodelize(godelize("P⊃PVQ"))
"P⊃PVQ"
```

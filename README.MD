# Regular Expression Calculator

One day, a fellow student of mine came to me with an assignment:
make a calcator in the console that would solve equations.
Possible inputs include `5 * (6 + 7)` and `3 * (1 + 2 * 3)`
and `4 * (3 * (2 + 1))`. The first thing that came to my mind:
the use of regular expressions.

## How it works

The calculator starts by defining the three types of things that can happen:
the remaining equation has priority brackets (`bracket_regex`),
has a priority operator like multiplication and devision
(`operator_high_regex`), or has a normal operation like addition
and subtraction (`operator_low_regex`).
These are checked in order through the `expressions` list.

The function that is called by the program is `evaluate()`.
This function keeps checking the regular expressions until
a single number remains. It uses the `eval()` function to do this.

The `calculate` function is used whenever a calculation is found
with two basic operators, these being natural numbers, not other equations.
Eventually, a single number remains which is matched with `number_regex`.
This is returned to the program.

| Function      | Description                                               |
|---------------|-----------------------------------------------------------|
| `evaluate()`  | Loop that keeps evaluating until a single number remains  |
| `eval()`      | Determining what to do during this step of the evaluation |
| `calculate()` | Calculate a basic expression like `4 * 3`                 |
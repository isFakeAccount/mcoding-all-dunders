# [mCoding] All Dunders Video

## Contributing

If you'd like to add a code example, make sure it has not already been done or
is in progress (see the [spreadsheet] or the [Issues tab] for reference). Once
you have confirmed that, open an issue for the dunder(s) you'd like to add
examples for. When you're done, simply make a PR!

### Submission guidelines
* The code has to be [PEP8]-compliant and lines must be at most 80 chars long
* Typehints are not necessary (unless needed for the example)
* Examples can include multiple dunders if they go together
* The code should be a minimal working example that uses the dunder(s)

When submitting code for the `__cool_dunder__` dunder, name the file
`cool_dunder.py` (basically strip the underlines). When submitting multiple
dunders in one example, you can:
* use the dunder name that's the most important/popular, e.g. `name.py` when
  adding `__name__` and `__qualname__`
* use a name that easily describes all of them, e.g. `comparisons.py` when
  adding `__gt__`, `__le__`, etc.

The file should be put in the corresponding folder inside `src`, e.g. a
`__post_init__` example should be located in `src/library-lagoon/post_init.py`
(see categories in the [spreadsheet]).


[Issues tab]: https://github.com/trag1c/mcoding-all-dunders/issues
[mCoding]: https://www.youtube.com/@mCoding
[PEP8]: https://peps.python.org/pep-0008/
[spreadsheet]: https://docs.google.com/spreadsheets/d/1-45UeKKMCePmTDLptT2zpI4L-jikmsCnve_lwOMyeuY/edit?usp=sharing
Theatrical Players Refactoring Kata - Python version
========================================================

See the [top level readme](https://github.com/emilybache/Theatrical-Players-Refactoring-Kata) for general information about this exercise.

This project uses [pytest](https://docs.pytest.org/en/latest/) and [approvaltests](https://github.com/approvals/ApprovalTests.Python). Pytest is configured in the file 'pytest.ini'. See also [documentation for pytest-approvaltests](https://pypi.org/project/pytest-approvaltests/).

After analysing the code, I diagnosed several issues:
- the `statement()` function has too many responsibilities: read the data, calculations, generate text...
- the "kinds of play" parameters are hard coded in if/else statements so it makes it difficult to add new ones
- high indentation levels
- invoice calculation is repeated two times
  
My goal with the refactoring was:
   * split the `statement()` function: first aggregate the data into one data structure (`construct_play()` function) and then to structure it with a dataclass ready to be used by the `statement()` function
   * to separate the different kind of plays from the code to make it easier to add new ones later
   * to make a unique calculation function that can handle the different cases without if statements


The difficulties I encountered:
   * I did only 3 commits for all the refactoring (prior to some minor tweaks). I have some trouble working on small incremental steps and have a tendency to "destoy all" and then reconstruct
   * the goal of the kata is clear but the boundaries are not. Where to stop? What is prohibited?
   * Using the approvaltests library was a first for me. For example, I didn't find how to generate my approved files automatically even by reading the docs

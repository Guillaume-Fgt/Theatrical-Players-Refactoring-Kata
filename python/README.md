Theatrical Players Refactoring Kata - Python version
========================================================

See the [top level readme](https://github.com/emilybache/Theatrical-Players-Refactoring-Kata) for general information about this exercise.

This project uses [pytest](https://docs.pytest.org/en/latest/) and [approvaltests](https://github.com/approvals/ApprovalTests.Python). Pytest is configured in the file 'pytest.ini'. See also [documentation for pytest-approvaltests](https://pypi.org/project/pytest-approvaltests/).

My goal with the refactoring was 
    * to first aggregate the data into one data structure (`construct_play()` function) and then to structure it with a dataclass ready to be used by the `statement()` function
    * to separate the different kind of plays from the code to make it easier to add new ones later


The difficulties I encountered:
    * I did only 3 commits for all the refactoring. I have some trouble working on small incremental steps
    * the goal of the kata is clear but the boundaries are not. Where to stop?
    * Using the approvaltests library was a first for me. Didn't find how to generate my approved files automatically.
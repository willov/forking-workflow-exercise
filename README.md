# Exercise to practice collaborative forking workflow

We will run this exercise in groups and we number the groups
1, 2, ..., etc.


## Goals of this exercise

- Learn how to fork, and file a pull request.
- Learn how to update your fork with upstream changes.


## First part: Fork, clone, and modify

First fork this repository and then clone the fork.

Then add a file `groupN.py` where N is your group number, e.g. `group17.py`.

This file should contain a function called `tweet()` which returns
a string of maximum 140 characters, for instance:
```python
def tweet():
    return "please replace this boring sentence with something more fun"
```

The file `main.py` automatically calls all `tweet()` functions defined in files
`groupN.py` (1 <= N <= 50). You do not need to edit `main.py`.

You can test it:
```
$ python main.py

group 17 says: please replace this boring sentence with something more fun
```

Once you see your sentence correctly printed, commit and push.


## Second part: File a pull request

Then file a pull request towards the repository where you forked from.

Wait until we integrate all pull requests into the central repo
together.


## Third part: Update your fork

We do this part after the contributions from all groups have been integrated.

Once this is done, practice to update your forked repo with the upstream
changes and verify that you got the files created by other groups:
```
$ python main.py
```

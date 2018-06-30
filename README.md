This is a coding challenge for students in Lambda School's Machine Learning course. It covers some of the basic mathematical functions that appear in reinforcement learning.

# Instructions for students

Visit the article

`https://medium.freecodecamp.org/an-introduction-to-reinforcement-learning-4339519de419`

and read up to the line  "To be simple, each reward will be discounted by gamma to the exponent of the time step." Today we'll be implementing the equation immediately above that. For simplicity, we'll assume that R_1, R_2, R_3, ... are all the same value (call it R). At this point, if you're confused by the notation you should consult this helpful tutorial

`http://www.columbia.edu/itc/sipa/math/summation.html`

or ask around on the Slack channel. Once you understand what's going on in that equation you should clone this repository, open it up locally, and check out the file `Exercise.py`. You'll see an empty function called `reward(gamma, R)`. Right now it's set to return -1.0. Change it so that it returns the correct answer. THIS IS THE ONLY FILE YOU SHOULD EDIT.

## Testing your solution

Today is probably your first exposure to pytest, a popular testing framework for Python. To install pytest, run

`sudo pip install -U pytest`

If you run into any problems, consult the official documentation at

`https://docs.pytest.org/en/3.0.6/index.html`

Once you have pytest set up, simply run the command

`pytest`

and you should be told that each `test_exercise` has failed due to an `AssertionError`. When all four tests pass, you've finished the assignment.

Note that, with a few exceptions if you know enough mathematics, there is no good way for a program to calculate the exact value of an infinite sum. Besides the inherent trickiness of infinite sums, this is true because of the unavoidable approximateness of floating point arithmetic. But don't worry about that. The tests here only check that you have the right answer to about 1 part in 1000.
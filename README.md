This is a coding challenge for students in Lambda School's Machine Learning course. It covers some of the basic mathematical functions that appear in reinforcement learning.

# Instructions for students

Visit the article

`https://medium.freecodecamp.org/an-introduction-to-reinforcement-learning-4339519de419`

and read up to the line  "To be simple, each reward will be discounted by gamma to the exponent of the time step." Today we'll be implementing the equation immediately above that. For simplicity, we'll assume that R_1, R_2, R_3, ... are all the same value (call it R). At this point, if you're confused by the notation you should consult this helpful tutorial

`http://www.columbia.edu/itc/sipa/math/summation.html`

or ask around on the Slack channel. Once you understand what's going on in that equation you should clone this repository, open it up locally, and check out the file `Exercise.py`. You'll see an empty function called `reward(gamma, R)`.

## Testing your solution

Today is probably your first exposure to pytest, a popular testing framework for Python. To install pytest, run

`sudo pip install -U pytest`

If you run into any problems, consult the official documentation at

`https://docs.pytest.org/en/3.0.6/index.html`

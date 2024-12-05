## What does the Program do?


For each page to be printed:
Create a directed graph of requirements.
Page A must Print before B => A points to B.
Delete all unrelated nodes.
a) If an arrow points to X, printing is prohibited => Fail.
b) Otherwise, delete X and all associated arrows.


Why is it so slow?
The program is creating the requirement graph every time again for each update line (from the input).
Creating the graph once and then just working with a copy of it is way faster, but also harder to implement.
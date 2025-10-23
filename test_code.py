from dummy_data_v1 import Course


math3a = Course(id="MATH 3A", full_title="Calculus with Applications, First Course")

math3b = Course(id="MATH 3B", full_title="Calculus with Applications, Second Course")

math4a = Course(id="MATH 4A", full_title="Linear Algebra with Applications")
math4a.prerequisite.append(math3a)
math4a.prerequisite.append(math3b)

math4b = Course(id="MATH 4B", full_title="Differential Equations")
math4b.prerequisite.append(math4a)

math6a = Course(
    id="MATH 6A", full_title="Vector Calculus with Applications, First Course"
)
math6a.prerequisite.append(math4a)

math6b = Course(
    id="MATH 6B", full_title="Vector Calculus with Applications, Second Course"
)
math6b.prerequisite.append(math4b)
math6b.prerequisite.append(math6a)

print(math4a)

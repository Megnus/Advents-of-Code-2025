# import numpy as np
# from scipy.optimize import minimize

# # Objective: minimize sum of variables
# def objective(x):
#     return np.sum(x)

# # Equality constraints
# def constraint1(x):
#     return x[4] + x[5] - 3

# def constraint2(x):
#     return x[1] + x[5] - 5

# def constraint3(x):
#     return x[2] + x[3] + x[4] - 4

# def constraint4(x):
#     return x[0] + x[1] + x[3] - 7


# constraints = [
#     {'type': 'eq', 'fun': constraint1},
#     {'type': 'eq', 'fun': constraint2},
#     {'type': 'eq', 'fun': constraint3},
#     {'type': 'eq', 'fun': constraint4},
# ]

# # Positivity constraints (x_i > 0)
# bounds = [(1e-6, None)] * 6

# # Initial guess (must satisfy bounds)
# x0 = np.array([1, 3, 0, 3, 1, 2])

# result = minimize(
#     objective,
#     x0,
#     method='SLSQP',
#     bounds=bounds,
#     constraints=constraints
# )

# print(result.x)
# print("Sum:", np.sum(result.x))



# from ortools.sat.python import cp_model

# model = cp_model.CpModel()

# x = [model.NewIntVar(1, 100, f"x{i}") for i in range(3)]

# model.Minimize(sum(x))

# model.Add(x[0] + x[1] + x[2] == 10)
# model.Add(2*x[0] + x[1] == 6)

# solver = cp_model.CpSolver()
# solver.Solve(model)

# print([solver.Value(v) for v in x])


import pulp

# Problem
prob = pulp.LpProblem("MinSum", pulp.LpMinimize)
solver = pulp.PULP_CBC_CMD(msg=False)

# Variables (positive integers)
x = [pulp.LpVariable(f"x{i}", lowBound=0, cat="Integer") for i in range(4)]

# Objective
prob += pulp.lpSum(x)

# Constraints
# prob += x[0] + x[1] + x[2] == 10
# prob += 2*x[0] + x[1] == 6

# prob += x[4] + x[5] == 3
# prob += x[1] + x[5] == 5
# prob += x[2] + x[3] + x[4] == 4
# prob += x[0] + x[1] + x[3] == 7

# prob += x[0] + x[2] + x[3] == 7
# prob += x[3] + x[4] == 5
# prob += x[0] + x[1] + x[3] + x[4] == 12
# prob += x[0] + x[1] + x[4] == 7
# prob += x[0] + x[2] + x[4] == 2

# prob +=  x[0] + x[1] + x[2] == 10
# prob +=  x[0] + x[2] + x[3] == 11
# prob +=  x[0] + x[2] + x[3] == 11
# prob +=  x[0] + x[1] == 5
# prob +=  x[0] + x[1] + x[2] == 10
# prob +=  x[2]== 5

# Solve
prob.solve(solver)

print([v.value() for v in x])
print("Sum:", sum(v.value() for v in x))

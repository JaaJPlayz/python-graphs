import os
import math
import matplotlib.pyplot as plt


def solve_quadratic_and_plot(a, b, c, equation_index):
    discriminant = b**2 - 4 * a * c

    x_values = list(range(-10, 11))

    y_values = [a * x**2 + b * x + c for x in x_values]

    if discriminant < 0:
        print(f"No real roots for equation {equation_index}")
        return None, None

    elif discriminant == 0:
        x = -b / (2 * a)
        return x, x_values, y_values

    else:
        sqrt_discriminant = math.sqrt(discriminant)
        x1 = (-b + sqrt_discriminant) / (2 * a)
        x2 = (-b - sqrt_discriminant) / (2 * a)
        return (x1, x2), x_values, y_values


quadratic_equations = [
    (1, -4, 3),
    (2, 5, -3),
    (3, 6, 2),
    (1, 4, 4),
    (4, 0, -16),
    (1, 3, 2),
    (2, -5, 2),
    (1, -7, 10),
    (3, -2, -1),
    (4, 8, 3),
]

data_dir = "data"
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

for idx, (a, b, c) in enumerate(quadratic_equations):
    solutions, x_values, y_values = solve_quadratic_and_plot(a, b, c, idx + 1)

    if solutions is not None:
        plt.figure()
        plt.plot(x_values, y_values, label=f"{a}x^2 + {b}x + {c} = 0")
        plt.title(f"Quadratic Equation {idx+1}")
        plt.xlabel("x")
        plt.ylabel("y")

        if isinstance(solutions, tuple):
            plt.scatter(solutions[0], 0, color="red", label=f"Roots: {solutions}")
            plt.scatter(solutions[1], 0, color="red")
        else:
            plt.scatter(solutions, 0, color="red", label=f"Root: {solutions}")

        plt.legend()

        plt.savefig(os.path.join(data_dir, f"quadratic_equation_{idx+1}.png"))
        plt.close()

        print(f"Saved graph for equation {idx+1} in 'data' folder.")
    else:
        print(f"No real solutions for equation {idx+1}")

print("All graphs saved successfully.")

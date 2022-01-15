# NAA.
# - hyperparameters as globals

x_init = 151.0  # initial y guess
n_epochs = 100  # number of iterations for algorithm
alpha = 0.01  # learning rate
y_min_threshold = 0.00001  # early y_min threshold

# Given
def f(x):
    """
    - original polynomial expression:
    10 * (x-2)**2 + 7
    """
    """
    - simplify so we can derive gradient later
    10 * (x**2 - (4*x)- 4) + 7
    (10 * x**2) - (40 * x) - 40 + 7
    (10 * x**2) - (40 * x) - 47
    """
    return 10.0 * (x - 2.0) ** 2.0 + 7.0


# Solve
def find_min(f):
    """
    - find y minimum by iterating using gradient descent:
      - y function
      - hyperparamters (y_init, alpha)
      - loss
      - y gradient
    """

    def dump_epoch(y_last, y_new, x_new):
        def x_step_str(y_last, y_new):
            if y_new < y_last:
                return "left"
            elif y_new > y_last:
                return "right"

        print(
            "y_last: {0}, y_new: {1}, y_new < y_last: {2}, step_dir: {3}, x_step: {4}".format(
                y_last, y_new, (y_new < y_last), x_step_str(y_last, y_new), x_new
            )
        )

    # NA
    # - my first mistake was mixing concepts of x steps versus y_new and cost function
    def x_step(x):
        x_new = x - (alpha * gradient(x))
        return x_new

    def y_min_reached(epoch, y_last, y_new, x_new):
        if abs(y_last - y_new) <= y_min_threshold:
            print(
                "*** y_min found early epoch {0} for: y_new: {1}, x_new".format(
                    epoch, y_new, x_new
                )
            )
            return True
        else:
            return False

    # initialize to first guess
    x_last = x_init
    y_last = f(x_init)
    step_dir = 1.0

    # iterate
    print("")
    print("*** start find_min() optimization.")
    for epoch in range(1, n_epochs):
        # compute y_new after x_new step
        x_new = step_dir * x_step(x_last)
        y_new = f(x_new)

        dump_epoch(y_last, y_new, x_new)

        if y_new < y_last:
            x_last = x_new
            step_dir = 1.0  # step same direction

            y_last = y_new  # assign y_new as new minimum
        elif y_new > y_last:
            # x_last = x_new
            step_dir = -1.0  # step opposite direction, y_last
        elif y_min_reached(epoch, y_last, y_new, x_new):
            return epoch, x_new, y_new

    # y_last after all epochs
    return epoch, x_new, y_new


def gradient(x):
    """
    - original polynomial expression
    (10 * x**2) - (40 * x) - 47
    """

    """
    - find derivative or gradient 
    (20 * x) - 40 - 0
    """
    return (20.0 * x) - 40.0 - 0.0


def y_loss(f, x):
    """
    - loss function
    """
    return f + (alpha * gradient(x))


def main():
    # NA
    # - given
    my_func = f(x_init)

    print("type(x_init): {0}".format(type(x_init)))
    print("type(f): {0}".format(type(f)))
    print("type(my_func): {0}".format(type(my_func)))

    # NA.
    # - my_loss scope does not make sense here
    # my_loss = y_loss(my_func, x)

    # NA.
    # - optimize iteratively with fixed epochs, function to optimize, and loss function
    # - NOTE:hyper parameters are global as function limit to pass in 1 parameter as x.
    # NA
    # - NOTE: pass function type and not evaluated function (as float) !
    # y_min = find_min(my_func)
    epochs_actual, x_new, y_min = find_min(f)

    print("After: {0} epochs".format(epochs_actual))
    print("    x_init:  {0}".format(x_init))
    print("    y_init:  {0}".format(f(x_init)))
    print("    x_new:   {0}".format(x_new))
    print("    y_min:   {0}".format(y_min))


if __name__ == "__main__":
    main()

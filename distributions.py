import numpy as np

"""
Common Parameters:
    - P (float): The parameter defining the allocation strategy steepness (between -1 and 1).
    - total bidget (float): The total budget to be distributed.
    - n_intervals (int): The number of time intervals over which the budget is distributed.
    
"""

def _linear_weights(P, n_intervals):
    """
    Calculate linear weights for linear distribution.

    Returns:
    - list of float: A list of linear weights for linear distribution.
    """
    weights = [1 - P * i / n_intervals for i in range(n_intervals)]
    check = [w <= 0 for w in weights]
    check = np.sum(check)
    if check > 0:
        weights = _linear_weights(1, n_intervals - check)
        weights += [0] * check

    return weights


def normalized_linear_weights(P, n_intervals):
    """
    Calculate normalized linear weights for linear distribution.

    Returns:
    - list of float: A list of normalized linear weights.
    """
    weights = _linear_weights(np.tan((np.pi / 2) * np.abs(P)), n_intervals)
    weights_sum = sum(weights)
    normalized_weights = [w / weights_sum for w in weights]

    if P < 0:
        normalized_weights.reverse()

    return normalized_weights


def exponential_weights(P, n_intervals):
    """
    Calculate weights for exponential distribution

    Returns:
    - list of float: A list of exponential weights for exponential distribution.
    """

    if P == 0:
        interval_weights = [1 / n_intervals] * n_intervals
    else:
        allocation = [(1 - np.abs(P)) ** i for i in range(n_intervals)]
        total_allocation = sum(allocation)
        interval_weights = [(a / total_allocation) for a in allocation]

    if P < 0:
        interval_weights.reverse()

    return interval_weights


def correct_budget_sum(P, budget, interval_budgets):
    """
    Correct the budget distribution to match specified budget.
    """
    delta = budget - sum(interval_budgets)
    num_intervals = len(interval_budgets)

    if delta == 0:
        return interval_budgets

    adjustment = delta // num_intervals
    remainder = delta % num_intervals

    adjustment_list = [adjustment] * num_intervals

    if P < 0:
        adjustment_list[-remainder:] = [adjustment + 1] * remainder
    else:
        adjustment_list[:remainder] = [adjustment + 1] * remainder

    interval_budgets = [b + a for b, a in zip(interval_budgets, adjustment_list)]

    return interval_budgets


def distribute_budget(P, total_budget, n_intervals, weights_generator_function):
    """
    Distribute budget using weights with a specified parameter.

    Returns:
    - list of int: A list of budget allocations based on the specified parameter P.
    """
    if not -1 <= P <= 1:
        raise ValueError("Parameter P is out of bounds. It must be between -1 and 1.")

    weights = weights_generator_function(P, n_intervals)
    interval_budgets = [int(np.floor(total_budget * w)) for w in weights]
    interval_budgets = correct_budget_sum(P, total_budget, interval_budgets)

    return interval_budgets


def distribute_budget_linear(P, total_budget, n_intervals):
    return distribute_budget(P, total_budget, n_intervals, normalized_linear_weights)


def distribute_budget_exponential(P, total_budget, n_intervals):
    return distribute_budget(P, total_budget, n_intervals, exponential_weights)


if __name__ == "__main__":
    total_budget = 700
    n_intervals = 30
    p_values = [round(x * 0.1, 1) for x in range(-10, 11)]

    for P in p_values:
        interval_budgets = distribute_budget_linear(P, total_budget, n_intervals)
        print(f'{P}: {interval_budgets}, sum={sum(interval_budgets)}')
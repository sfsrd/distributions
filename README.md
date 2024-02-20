# Budget Distribution Library

Welcome to the Budget Distribution Library! This repository provides a Python module designed to address the problem of distributing a budget over multiple time intervals using two different allocation strategies: linear and exponential.

## Introduction

One of the fundamental challenges in financial planning and resource allocation is how to distribute a limited budget effectively across various time intervals. This library offers solutions to this problem by implementing two distinct distribution methods:

- **Linear Distribution**: This method allocates the budget evenly across all time intervals, with no preference for any specific period.
- **Exponential Distribution**: In contrast, exponential distribution allocates the budget in a non-linear fashion, favoring either early or later time intervals based on a specified parameter.

## Usage

The `distributions.py` module provides functions to calculate budget allocations using both linear and exponential distribution methods. Users can specify the total budget, the number of time intervals, and the allocation parameter (`P`) to customize the distribution according to their needs.

### Common Parameters

- **`P` (float)**: The parameter defining the allocation strategy steepness (between -1 and 1).
- **`total_budget` (float)**: The total budget to be distributed.
- **`n_intervals` (int)**: The number of time intervals over which the budget is distributed.

In addition, the `distributions_visualization.ipynb` Jupyter notebook offers visualizations to help users understand how changing the parameter `P` affects the distribution of the budget over time intervals.

## Example

```python
import distributions

# Example usage
total_budget = 2400
n_intervals = 12
P = 0.5

# Distribute budget using linear weights
interval_budgets = distributions.distribute_budget_linear(P, total_budget, n_intervals)
print("Linear distribution:", interval_budgets)
# output:  [370, 339, 308, 277, 247, 216, 184, 153, 123, 92, 61, 30]

# Distribute budget using exponential weights
interval_budgets = distributions.distribute_budget_exponential(P, total_budget, n_intervals)
print("Exponential distribution:", interval_budgets)
# output:  [1201, 601, 301, 151, 75, 37, 18, 9, 4, 2, 1, 0]

```
## Visualization

The visualization notebook `distributions_visualization.ipynb` provides an environment to explore budget distributions using both linear and exponential allocation strategies. Users can adjust the parameter `P` and visualize the resulting budget allocations over time intervals.

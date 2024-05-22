def find_dishes_greedy(dishes, budget):
    # Sort dishes by calories to cost ratio in descending order
    dishes.sort(key=lambda x: x["calories"] / x["cost"], reverse=True)
    result = []
    total_cost = 0
    total_calories = 0

    for dish in dishes:
        if total_cost + dish["cost"] <= budget:
            result.append(dish["name"])
            total_cost += dish["cost"]
            total_calories += dish["calories"]

    return result, total_calories, total_cost


def find_dishes_dp(dishes, budget):
    dp = [0] * (budget + 1)
    choice = [None] * (budget + 1)

    for dish in dishes:
        for current_budget in range(budget, dish["cost"] - 1, -1):
            if (
                dp[current_budget - dish["cost"]] + dish["calories"]
                > dp[current_budget]
            ):
                dp[current_budget] = (
                    dp[current_budget - dish["cost"]] + dish["calories"]
                )
                choice[current_budget] = dish

    result = []
    current_budget = budget
    total_calories = dp[budget]
    total_cost = 0

    while current_budget > 0 and choice[current_budget] is not None:
        dish = choice[current_budget]
        result.append(dish["name"])
        current_budget -= dish["cost"]
        total_cost += dish["cost"]

    return result, total_calories, total_cost


# Testing
dishes = [
    {"name": "Dish1", "calories": 500, "cost": 5},
    {"name": "Dish2", "calories": 300, "cost": 3},
    {"name": "Dish3", "calories": 400, "cost": 4},
    {"name": "Dish4", "calories": 600, "cost": 6},
]

budget = 10

# Greedy algorithm
greedy_result, total_calories, total_cost = find_dishes_greedy(dishes, budget)
print(
    "Жадібний алгоритм:",
    greedy_result,
    "Загальні калорії:",
    total_calories,
    "Загальна вартість:",
    total_cost,
)

# Dynamic Programming
dp_result, total_calories_dp, total_cost_dp = find_dishes_dp(dishes, budget)
print(
    "Динамічне програмування:",
    dp_result,
    "Загальні калорії:",
    total_calories_dp,
    "Загальна вартість:",
    total_cost_dp,
)

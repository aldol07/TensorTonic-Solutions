def value_iteration_step(values: list, transitions: list, rewards: list, gamma: float) -> list[float]:
    """
    Returns one updated floating-point value for every state.
    """
    updated_values = []

    for s in range(len(values)):
        best_value = float("-inf")

        for a in range(len(rewards[s])):
            expected_value = sum(
                transitions[s][a][next_s] * values[next_s]
                for next_s in range(len(values))
            )

            q_value = rewards[s][a] + gamma * expected_value
            best_value = max(best_value, q_value)

        updated_values.append(float(best_value))

    return updated_values
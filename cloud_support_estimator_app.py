def calculate_support_cost(support_type: str, monthly_spend: float) -> float:
    support_type = support_type.lower()

    if support_type == "standard":
        cost = max(29.0, 0.03 * monthly_spend)

    elif support_type == "enhanced":
        if monthly_spend <= 10000:
            cost = 0.10 * monthly_spend
        elif monthly_spend <= 80000:
            cost = (0.10 * 10000) + (0.07 * (monthly_spend - 10000))
        elif monthly_spend <= 250000:
            cost = (0.10 * 10000) + (0.07 * 70000) + (0.05 * (monthly_spend - 80000))
        else:
            cost = (0.10 * 10000) + (0.07 * 70000) + (0.05 * 170000) + (0.03 * (monthly_spend - 250000))
        cost = max(100.0, cost)

    elif support_type == "premium":
        if monthly_spend <= 150000:
            cost = 0.10 * monthly_spend
        elif monthly_spend <= 500000:
            cost = (0.10 * 150000) + (0.07 * (monthly_spend - 150000))
        elif monthly_spend <= 1000000:
            cost = (0.10 * 150000) + (0.07 * 350000) + (0.05 * (monthly_spend - 500000))
        else:
            cost = (0.10 * 150000) + (0.07 * 350000) + (0.05 * 500000) + (0.03 * (monthly_spend - 1000000))
        cost = max(15000.0, cost)

    else:
        raise ValueError("Invalid support type. Choose from 'Standard', 'Enhanced', or 'Premium'.")

    return round(cost, 2)

def main():
    print("Cloud Support Cost Estimator")
    print("Support levels: Standard, Enhanced, Premium")
    support_type = input("Enter support type: ").strip()

    try:
        monthly_spend = float(input("Enter monthly cloud spend in USD: "))
        cost = calculate_support_cost(support_type, monthly_spend)
        print(f"\nEstimated Monthly Support Cost: ${cost:,.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

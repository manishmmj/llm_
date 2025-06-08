def calculate_financial_plan(age, income, expenses, savings_goal):
    years_to_goal = max((savings_goal - (income - expenses) * 12) // ((income - expenses) * 12), 0)
    annual_saving = income - expenses
    if annual_saving <= 0:
        return "Increase your income or reduce expenses to achieve financial goals."

    return {
        "Annual Saving": annual_saving,
        "Years to Reach Goal": years_to_goal,
        "Recommendation": "Maintain current savings rate" if years_to_goal <= 10 else "Consider investing to grow savings"
    }
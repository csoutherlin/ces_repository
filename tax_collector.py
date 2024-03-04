# Constants (accurate as of 2023)
FEDERAL_STANDARD_DEDUCTION = 13200
STATE_STANDARD_DEDUCTION = {
    'California': 4609,
    'New York': 8000
}
FEDERAL_TAX_BRACKETS = [
    (10400, 0.10),
    (41225, 0.12),
    (89400, 0.22),
    (174050, 0.24),
    (215400, 0.32),
    (549900, 0.35),
    (1000000, 0.37)
]
STATE_TAX_BRACKETS = {
    'California': [
        (9076, 0.01),
        (22771, 0.02),
        # ... (other brackets for California)
    ],
    'New York': [
        (8500, 0.04),
        (11700, 0.045),
        # ... (other brackets for New York)
    ]
}

def calculate_federal_tax(gross_salary):
    taxable_income = gross_salary - FEDERAL_STANDARD_DEDUCTION
    federal_tax = 0

    for bracket, rate in FEDERAL_TAX_BRACKETS:
        if taxable_income <= bracket:
            federal_tax += taxable_income * rate
            break
        else:
            federal_tax += bracket * rate
            taxable_income -= bracket

    return federal_tax

def calculate_state_tax(gross_salary, state):
    taxable_income = gross_salary - STATE_STANDARD_DEDUCTION.get(state, 0)
    state_tax = 0

    for bracket, rate in STATE_TAX_BRACKETS.get(state, []):
        if taxable_income <= bracket:
            state_tax += taxable_income * rate
            break
        else:
            state_tax += bracket * rate
            taxable_income -= bracket

    return state_tax

def calculate_fica(gross_salary):
    # Assuming FICA is 7.65% up to $147,000
    return min(gross_salary * 0.0765, 147000 * 0.0765)

if __name__ == '__main__':
    GROSS_SALARY = float(input("What's your annual income? >>> "))
    STATE = input("Which state do you reside in? (California or New York) >>> ")

    federal_tax = calculate_federal_tax(GROSS_SALARY)
    state_tax = calculate_state_tax(GROSS_SALARY, STATE)
    fica = calculate_fica(GROSS_SALARY)

    net_salary = GROSS_SALARY - federal_tax - state_tax - fica

    print(f"Your Gross Salary: ${GROSS_SALARY:.2f}")
    print(f"Federal Tax: ${federal_tax:.2f}")
    print(f"State Tax ({STATE}): ${state_tax:.2f}")
    print(f"FICA: ${fica:.2f}")
    print(f"Net Salary: ${net_salary:.2f}")

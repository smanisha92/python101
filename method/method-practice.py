def calculateNetIncome(gross, state):
    state_tax = {'NY': 10, 'LA': 12, 'CA': 2, 'SF': 0, 'HI': 15}
    net = gross - (gross * 0.10)
    if state in state_tax:
        net = net - (gross * state_tax[state]/100)
        print("The calculated Net income after deduction is: " + str(net))
        return net
    else:
        print("State is not in the list")
        return None


calculateNetIncome(100200, 'A')

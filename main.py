# Import library PuLP as p
import pulp as p

# Set up a maximization problem and its variable
# (I) Name the problem as "IceCream_maxProfit_Analysis" using objective of minimizing cost :
profit = p.LpProblem('IceCream_maxProfit_Analysis', p.LpMinimize)

# (II) Set up problem variables :
# Box of vanilla ice-cream
vanilla = p.LpVariable('v', lowBound=0)
# Box of strawberry ice-cream
strawberry = p.LpVariable('s', lowBound=0)








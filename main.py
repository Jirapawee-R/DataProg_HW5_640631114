# Import library PuLP as p
import pulp as p

# Set up a maximization problem and its variable
# (I) Name the problem as "IceCream_maxProfit_Analysis" using objective of minimizing cost :
profit = p.LpProblem('IceCream_maxProfit_Analysis', p.LpMinimize)

# (II) Set up problem variables :
# Box of vanilla ice-cream
vanilla = p.LpVariable('vanilla', lowBound=0)
# Box of strawberry ice-cream
strawberry = p.LpVariable('strawberry', lowBound=0)

# Create objective function :
profit += (2*vanilla) + (3*strawberry)

# Create constraints :
# (I) Amount of daily fresh milk order
profit += (0.5*vanilla) + (0.2*strawberry) <= 10
# (II) Number of doll for promoting in a day
profit += vanilla + strawberry <= 30





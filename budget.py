class Category:
  name = " "
  withdrawals = 0

  def __init__(self, n):
    self.name = n
    self.ledger = list()

  def deposit(self, amount, *args):
    if (args):
      self.ledger.append({'amount': amount, 'description': str(args[0]) })
    else:
      self.ledger.append({'amount': amount, 'description': "" })
  
  def withdraw(self, amount, *args):
    if (self.check_funds(amount) == True):
      if (args):
        self.ledger.append({'amount': -abs(amount), 'description': str(args[0]) })
      else:
        self.ledger.append({'amount': -abs(amount), 'description': "" })
      self.withdrawals += abs(amount)
      return True
    else:
      return False

  def get_balance(self):
    balance = 0
    for i in range(len(self.ledger)):
      balance = balance + self.ledger[i]['amount']
    return balance

  def transfer(self, amount, cat):
    if (self.check_funds(amount) == True):
      ch = "Transfer to " + cat.name
      self.withdraw(amount, ch)
      ch1 = "Transfer from " + self.name
      cat.deposit(amount, ch1)
      return True
    else:
      return False

  
  def check_funds(self, amount):
    funds = self.get_balance()
    if (funds < amount):
      return False
    else:
      return True


  def __str__(self):
    ln = len(self.name)
    lo = 30 - ln

    line = f"{'*' * round(lo/2)}{self.name}{'*' * round(lo/2)}"

    for i in range(len(self.ledger)):
      desc = self.ledger[i]['description'][0:23]
      ch = str("%.2f" % self.ledger[i]['amount'])[0:7].rjust(29-len(desc))

      line += f"\n{desc} {ch}"
    b = self.get_balance()
    line += f"\nTotal: {b}"
    return line
     
    

def create_spend_chart(categories):
  cat = Category
  expenses = dict()
  exp_cat = dict()
  total = 0
  
  for cat in categories:
      expenses[cat.name] = abs(cat.withdrawals)
      total += abs(cat.withdrawals)

  for cat, amount in expenses.items():
    exp_cat[cat] = round((amount)/total*100)
  
    line = "Percentage spent by category"
  for i in range(100,-1,-10):
    line += f"\n{str(i).rjust(3)}| " 
    for j in exp_cat.values():
      if (j>=i):
        line += "o  "
      else:
        line += "   "
  
  p = len(categories)
  line += f"\n    -{('---'*(p))}\n"

  maxlen = max(map(len, expenses))
  for c in range (maxlen):
    line += "     "
    for cat in expenses.keys():
      if (len(cat) <= maxlen):
        cat= cat + (" ")*(maxlen-len(cat))
        line += f"{cat[c]}  "
    line += "\n"
  
  

  line = line.rstrip()
  line += "  "
 

    
  return(line)

  
class wallet:
    def __init__(self, btc=0, eth=0, solana=0):
        self.btc = btc
        self.eth = eth
        self.solana = solana

    def __str__(self):
        return f"btc: {self.btc}, eth: {self.eth}, solana: {self.solana}"

    def __add__(self, other):
        btc = self.btc + other.btc
        eth = self.eth + other.eth
        solana = self.solana + other.solana
        return wallet(btc, eth, matic)

Wynder = wallet(1,2,3)
print(f"Wynder tem em sua carteira {Wynder}")
Wilson = wallet(3,2,1)
print(f"Wilson tem em sua carteira {Wilson}")
Bruno = wallet(2,1,3)
print(f"Bruno tem em sua carteira {Bruno}")

import pandas as pd 

class LogAnalyser:
    def __init__(self):
        self.data = []
        self.player_names = []
        self.df = pd.DataFrame()
    
    def retrive_info(self, filename):
        with open(filename, "r") as f:
                lines = f.readlines()
           
        for line in lines:
            # Example line: "Round 1: a rolled 1, b rolled 2, c rolled 3"
            try:
                round_part, rolls_part = line.strip().split(":", 1)
            except ValueError:
                continue  # skip malformed lines

            rolls_dict = {}
            for part in rolls_part.split(","):
                part = part.strip()  # remove spaces
                if " rolled " in part:
                    name, _, roll = part.partition(" rolled ")
                    rolls_dict[name] = int(roll)
                    if name not in self.player_names:
                        self.player_names.append(name)
            self.data.append(rolls_dict)
           
        # Convert list of dicts to DataFrame
        self.df = pd.DataFrame(self.data, columns=self.player_names)
        self.df.index += 1  # rounds starting from 1
        self.df.index.name = "Round"


L1 = LogAnalyser()
L1.retrive_info("results.txt")  

# print(L1.df)
# print(L1.df.head(2))
# print(L1.df.info())
# print(L1.df.describe())
print(L1.df.shape)
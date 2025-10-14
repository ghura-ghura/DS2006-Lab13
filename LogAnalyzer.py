import pandas as pd 

class LogAnalyser:
    def __init__(self):
        self.data = []
        self.player_names = []
        self.df = pd.DataFrame()
    
    def retrive_info(self, filename):
        with open(filename, "r") as f:
                lines = f.readlines()
        # Control variable for us going forward
        in_game_section = False
        current_round_data = {}
        # Loop through all of or lines 
        for i, line in enumerate(lines):
            line = line.strip() # remove any excess whitespace/newline charatcers 
            if not line: # Skip empty lines
                continue
            # Finds the actual round data beginning
            if not in_game_section:
                if line.lower().startswith("game rounds"):
                    in_game_section = True # Flags this line and goes until next line where this happens
                continue
            

            #  Find the rounds X and read the comming row with round info 
            if line.lower().startswith("round"):
                if i + 1 < len(lines):
                    rolls_line = lines[i + 1].strip() # Grabs the coming line 
                    rolls_dict = {}
                    # Parse each players roll
                    for part in rolls_line.split(","):
                        part = part.strip()
                        #Split at the phrase rolled. 
                        if " rolled " in part: 
                            name, _, roll = part.partition(" rolled ")
                            roll = roll.strip()
                            # Only process numeric rolls -- Might be bad if we want this to be more flexible 
                            if roll.isdigit():    
                                rolls_dict[name] = int(roll)
                                # Add tplayer name to the player list if it's not already addded
                                if name not in self.player_names:
                                    self.player_names.append(name)
                    # adds the rounds result to the data list                
                    if rolls_dict:
                        self.data.append(rolls_dict)
           
        # Convert list of dicts to DataFrame
        self.df = pd.DataFrame(self.data, columns=self.player_names)
        self.df.index += 1  # rounds starting from 1
        self.df.index.name = "Round"


L1 = LogAnalyser()
L1.retrive_info("Testfil.txt")  

#print(L1.df)
#print(L1.df.head(2))
#print(L1.df.info())
#print(L1.df.describe())
print(L1.df.shape)
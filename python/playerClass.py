class Player:
    def __init__(self, name, team, threeM, threeA, threePct) -> None:
        self.name = name
        self.team = team
        self.threesMade = threeM
        self.threesAtt = threeA
        self.threePct = threePct

    def getName(self):
        return self.name
    
    def getTeam(self):
        return self.team

    def getThrees_Made(self):
        return self.threesMade

    def getThrees_Att(self):
        return self.threesAtt

    def getThree_Pct(self):
        return self.threePct
    
    def getPlayer(self):
        return [self.name, self.team, self.threesMade, self.threesAtt, self.threePct]

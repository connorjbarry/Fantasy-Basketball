class Player:
    last_id = 0
    def __init__(self, id, name, team, threeM, threeA, threePct) -> None:
        self.id = Player.last_id + 1
        Player.last_id = self.id
        self.name = name
        self.team = team
        self.threesMade = threeM
        self.threesAtt = threeA
        self.threePct = threePct

    def getId(self):
        return self.id

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
        return [self.id, self.name, self.team, self.threesMade, self.threesAtt, self.threePct]

import sys #importing sys
class Team:
    def __init__(self,T="",P=0,W = 0,D = 0,L = 0,F = 0,A = 0,diff = 0,pts = 0): 
        """This function is created to called every times an object is created from a class. This method initialize the objects attributes and serves the value.""" 
        self.played = P
        self.win = W
        self.draw = D
        self.loss = L
        self.front = F
        self.against = A
        self.difference = diff
        self.points = pts
        self.team = T

    #getter function to get the values
    def get_team(self): 
        return self.team
    def get_played(self): 
        return self.played
    def get_win(self): 
        return self.win
    def get_loss(self): 
        return self.loss
    def get_draw(self): 
        return self.draw
    def get_front(self): 
        return self.front
    def get_against(self): 
        return self.against
    def get_diff(self): 
        return self.difference
    def get_points(self):
        return self.points
        
    # setter function to set the values
    def set_team(self,T): 
        self.team = T 
    def set_played(self,P): 
        self.played = P
    def set_win(self,W):  
        self.win = W
    def set_loss(self,L): 
        self.loss = L
    def set_draw(self,D): 
        self.draw = D
    def set_front(self,F): 
        self.front = F
    def set_aganst(self,A): 
        self.against = A
    def set_diff(self,diff): 
        self.difference = diff
    def set_points(self,pts):
        self.points = pts

    def set_score(self,frnt,agnst): 
        """This function receive the value of Front and Against and calculate the value. Then it is passed to set and get function."""
        self.set_front(self.get_front()+frnt)
        self.set_aganst(self.get_against()+agnst)
        self.set_played(self.get_played()+1)
        self.set_diff(self.get_diff()+(frnt-agnst))

        if frnt > agnst:
            self.set_win(self.get_win()+1)
            self.set_points(self.get_points()+3)
        elif frnt < agnst:
            self.set_loss(self.get_loss()+1)
        else:
            self.set_draw(self.get_draw()+1)
            self.set_points(self.get_points()+1)
def key(ab):
    """This function return the value that is sorted in arranging order"""
    return (ab.get_points(),ab.get_diff())

team = []
country = []
file = open("team.csv","r")
for i in file.readlines():  # it is used to read the data  inside the files
    tem = i.replace("\n","")
    team.append(tem)
file.close()

fle = open("result.csv","r")
for x in fle.readlines():   # it is used to read the data  inside the files
    ctry = x.replace("\n","").split(",")
    country.append(ctry)
fle.close()

objs = []
for a in team: #it loops the team list
    t = Team()
    objs.append(t)
    t.set_team(a)
    for b in country:  # it loops the country list
        if t.get_team() == b[0]:
            t.set_score(int(b[1]),int(b[3]))
        elif t.get_team() == b[2]:
            t.set_score(int(b[3]),int(b[1]))

objs.sort(key=lambda ab : (ab.get_points(),ab.get_diff()),reverse=True)

def output(objs): 
    """This function receives the objects from the passing function and then print the output as the table."""
    print(f"\n\t {'P':^11}{'W':<10}{'D':<10}{'L':<10}{'F':<10}{'A':<10}{'Diff':<10}{'Pts':<10}")   
    for gm in objs:  # it loops the object
        print(f"{gm.get_team():<10}{gm.get_played():^10}{gm.get_win():<10}{gm.get_draw():<10}{gm.get_loss():<10}{gm.get_front():<10}{gm.get_against():<10}{gm.get_diff():<10}{gm.get_points():<10}")

if len(sys.argv) == 1: # it checks the sys.argv is one or not
    output(objs)
else: 
    print("\n",sys.argv[1])
    for i in range(0,len(sys.argv[1])):
        print("=",end="")
    output(objs)
    

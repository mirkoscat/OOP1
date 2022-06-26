#OOP
class PlayerCharacter:

  def __init__(self,name,age):
      self.name=name
      self.age=age
   
     
  def run(self):
    print("Run")
    return "Done"
player1name=input("What is your name?")
player1age= input("What is your age?")
player1=PlayerCharacter(player1name,player1age)
print(player1.name)
player2=PlayerCharacter("Tom",18)
print(player2.age)

#OOP
class PlayerCharacter:
  #Class Object Attribute
  membership = True
  def __init__(self,name,age):
    if(age > 18):
      self.name=name
      self.age=age
    else:
      print("Too young, can't play")
    
     
  def run(self):
    print("Run")
    return "Done"
player1=PlayerCharacter("Mirko",30)
player2=PlayerCharacter("Tom",20)
player1.attack=50
print(f"name character is : {player1.name}")
print(player1.attack)

print(player2.age)
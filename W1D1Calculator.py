#repeat Code
while True:
# Equation template 
  def Addition(v1 ,v2):
      return v1 + v2

  def Subtraction(v1 ,v2):
      return v1 - v2

  def Division(v1 ,v2):
      return v1 / v2

  def Multiplication (v1 ,v2):
      return v1 * v2

# Instractions 
  print(
      "\n"
      "+. Addition\n"\
      "-. Subtraction\n"\
      "*. Multiplication\n"\
      "/. Division\n") 

# Valuse
  v1 =  float(input ("1st Number "))
  MathSymobles = input ("MathSymobles ")
  v2 = float(input ("2nd Number "))

# Generates outcome
  if MathSymobles == "+":
      (
  print(Addition(v1,v2))
      )
  elif MathSymobles == "-":
      (
  print(Subtraction(v1,v2))
      )
  elif MathSymobles == "*":
      (
  print(Multiplication(v1,v2))
      ) 
  elif MathSymobles == "/":
      (
  print(Division(v1,v2))
      )
  else :
      (
         print ("error")
      ) 
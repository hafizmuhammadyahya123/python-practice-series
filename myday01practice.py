#topic1
# print() using str----------  this is comment

print('I am a python programmer') #string 

print("I am a python programmer")

print('''surrogate end points basically 
      aik example k thhrough samajhtay hain  
      suppose aik Heart Patient ha 
      ab agr wo doctor k pss jata ha 
      or is ka test kr k medicine recommanded
      kr di jae or kaha jae daily ye use krty
      rahy tou ye absolutely wrong ha..
      Treatment tou ye ha k kuch surrogate
      end poijnts build kre means actual 
      end point jesy Heart Attack ye actual
      end point tha ab is sy pehly end point jesy 
      CHOLESTROL, BLOOD PRESSURE ye two surrogate 
      end points build kiyay takay jo medicine refer 
      ki thi kiya wo effected ha bhi ya nahi agr ha 
      NOW MEDICINE CONTINUE RKHNA HA AGR NAHI TOU KOE OR TREATMENT
      YA MEDICINE CHANGE KRNAY KI NEED HA AGR HUM THIS PARTICULAR CASE 
      MAIN YE 2 SURROGATE END POINTS NAHI BNAE TOU TO WO ACTUAL END POINT MEANS
      HEART ATTACK IS K REHAM O KARAM PR CHOR DIYA JAE SIRF MEDICINE REFER KR K TOU WO 
      PATIENT JALD HI MOUT K MOUN MAIN JA SKTA HA THIS IS ABSOLUTELY WRONGE...''')  
 
# print stat using int  
print(2)
print(25)

# Topic 2:  VARIABLES
name = 'ALI'  #var name using str
print(name)

age = 22  #store var name using int
print(age)

str = "this is str"
print(str)  

# data type as a vari name allowed
# but  keyword not allowed as a var name

# illegal var name:
# first name  = "ALI"  Reason space dy diya var name main
# 1name = "ali" 
 
# legal var name :
first_name = "Muhammad"  #snake_case_var
last_name = "Ali"
print(first_name , last_name)

FirstName = "ALI"
LastName = "MUHAMMAD"
print("MY FIRST NAME IS: ",FirstName)
print("MY LAST NAME IS:",LastName)

_gender = "MALE"
print(_gender)

number1 = 20 
number_2 = 20
sum  = number_2 + 50
print(sum)
print(type(sum))

number1 = number_2
print(number1)

# a = p = p = l = e = "apple"
# print(e)

#TOPIC 4: Math expressions: Familiar operators
print(2 + 2)

x = 2
y = 2
print(x + y)

sum = x + y
print("TWO+TWO = ",sum)
print('2 + 2 = ', sum)
print(type(sum))

print(2 - 2)

x = 2
y = 2
print(x - y)

difference = x - y
print("TWO - TWO = ",difference)
print('2 - 2 = ', difference)
print(type(difference))

print(2 * 2)

x = 2
y = 2
print(x * y)

product = x * y
print("TWO * TWO = ", product)
print('2 * 2 = ', product)
print(type(product))

print(2 + 2)

x = 2
y = 2
print(x / y)

quotient = x / y
print("TWO / TWO = ",quotient)
print('2 / 2 = ', quotient)
print(type(quotient))

print(2 // 2)

x = 2
y = 2
print(x // y)

floor_division = x // y
print("TWO // TWO = ",floor_division)
print('2 // 2 = ', floor_division)
print(type(floor_division))

print(2 ** 5)
# or 
x = 2
y = 5
print(x ** y)
# or 
exp = x ** y
print("TWO ** FIVE = ", exp)
print('2 ** 5 = ', exp)
print(type(exp))

# ----------------------------------------------------
# comparision operator
a = 11
b = 22
print(a != b)
print(a == b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# logical operators 
a = 20
b = 50

print("F and T = ",a >= b and a <= b)  # 0 and 1 = 0
print("F and T = ",a > b and a < b) 
print(a == b and a != b)
print(a != b and b != a)
print(a < b and a != b)
print(b > a and b == b)
print(a == a and b == b)
print(a > b or a < b)  # 0 or 1 = T
print(a != b or a == b)
print(a == b or a >= b) 

# CONCATENATE FOR STRING
# there are 3 methods

# 1 method using  + operator
FirstName = "ali"
LastName = "muhammad"
print(FirstName + LastName)
# or 
print(FirstName +' '+ LastName)
# or
print("muhamd" +' '+ "yahya")

# 2. f string
print(f'MY_NAME_IS: {FirstName} {LastName}')

# "{index1} {index2}...{index_n} ".format("str1","str2","str_n")
print("{1}{0}{2}{3}".format("python","is","heart of", "AI"))

# TOPIC: AUGMENT STATEMENT
a = 12
b = 20

a += 20 
print(a)

x = 50
x -= 10
print(x)

y = 40
y /= 40
print(y)

z = 90
z //= 90
print(z)

my_var = 20
my_var %= 3
print(my_var)

var = 3
var %= 2
print(var)

pro = 10
pro *= 2
print(pro)

exp = 2
exp **= 3
print(exp)

# PEMDAS RULE
print((2*3)+5)


print((2*4))
print((4*2))
print(8 * 5)
print(4 * 8)
print(40+32)
print((4*2)*5+4*(2*4))

print((4*2)*5+4/(2*4))

print((2+2)**2/2+2*(2*2))

x1, x2 = 3, 5 
m1, m2 = 3, 6
b = 0.01

y = m1*x1 + (m2*x2 + b)
print(y)

# input from user
first_name = input("Enter your first name...")
print(first_name)

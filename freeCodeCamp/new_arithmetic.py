
def aritmetic_arranger(problems,is_ok):
    num1=[]
    operans=[]
    num2=[]
    max=[]
    space=[]
    splited_list=[]
    more_right=[]
    dash_num=[]

    if len(problems)>5:
        return "Error:Too many problems."
    for problem in range(len(problems)):
        if "+" in problems[problem] or "-" in problems[problem]:
            if "+" in problems[problem]:
              splited_list.append(problems[problem].split("+",2))
              operans.append("+")
            elif "-" in problems[problem]:
                splited_list.append(problems[problem].split("-",2))
                operans.append("-")
            else:      
                return "Error:Operator must be '+' or  '-'"
    for number in range(len(splited_list)):
        if splited_list[number][0].isdigit()!=True:
            return "Error:Numbers must only contain digits."
        elif splited_list[number][1].isdigit()==False:
            return "Error:Numbers must only contain digits."
        
    for number in range(len(splited_list)):
        if len(splited_list[number][0])>4:
            return "Error:Numbers cannot be more than four digits."
        elif len(splited_list[number][1])>4:
            return "Error:Numbers cannot be more than four digits."
    #Find the bigger one
    for number in range(len(splited_list)):
        if int(splited_list[number][0])<int(splited_list[number][1]):
            max.append("1")
        elif int(splited_list[number][1])<int(splited_list[number][0]):
            max.append("0")
        elif int(splited_list[number][1])==int(splited_list[number][0]):
            max.append("-1")
    #Find the difference index between small one and big one
    for number in range(len(splited_list)):
        if max[number]=="0":
            bindex=len(splited_list[number][0])
            dash_num.append(bindex+2)
            
            differ_index=bindex-(len(splited_list[number][1]))
            more_right.append(differ_index)
            space.append(bindex+1)
        elif max[number]=="1":
            bindex=len(splited_list[number][1])
            dash_num.append(bindex+2)

            differ_index=bindex-len(splited_list[number][0])
            more_right.append(differ_index)
            space.append(bindex+1)
        elif max[number]=="-1":
            differ_index=0
            more_right.append(differ_index)
            dash_num.append(differ_index+1)
    #Add the first numbers to num1 and second numbers to num2        
    for number in range(len(splited_list)):
        f=splited_list[number][0]
        num1.append(f)
        s=splited_list[number][1]
        num2.append(s)
    #First Line Printing
    for num in range(len(num1)):
        if max[num]=="0":
            tot=dash_num[num]-len(max[num])
            right_aligned_num=num1[num].rjust(tot," ")
            print(right_aligned_num)
        elif max[num]=="1":
            tot=dash_num[num]-len(num1[num])
            right_aligned_num=num1[num].rjust(tot," ")
            print(right_aligned_num)
        elif max[num]=="-1":
            tot=dash_num[num]-len(num1[num])
            right_aligned_num=num1[num].rjust(tot," ")
            print(right_aligned_num)    
        print("    ",end="")
    #Second line Printing
    for num in range(len(num2)):
        if max[num]=="0":
            tot=dash_num[num]-len(max[num])
            right_aligned_num=num2[num].rjust(tot," ")
            print(right_aligned_num)
        elif max[num]=="1":
            tot=dash_num[num]-len(num2[num])
            right_aligned_num=num2[num].rjust(tot," ")
            print(right_aligned_num)
        elif max[num]=="-1":
            tot=dash_num[num]-len(num2[num])
            right_aligned_num=num2[num].rjust(tot," ")
            print(right_aligned_num)    
        print("    ",end="")

   




print(aritmetic_arranger(["32+8","1-3801","9999+9999","523-49"],True))

#--TO DO ----#
#1)Arithmetic problems vertically to make easies to solve.
#2)Create a function that receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side by side.

#3)The function should optionally take a second argment.When second argument is set to True,the answer should be displayed.
#*)The function will return the correct conversion if supplied problems are properly formatted
#*Otherwise,it will return a string that describes an error that is meaningful to the user.
#aritmetic_arranger(["32+8","1-3801","9999+9999","523-49"],True)
##OUTPUT:
#     32         1      9999      523
#   +  8    - 3801    + 9999    -  49
#   ----    ------    ------    -----
#     40     -3800     19998      474



########CONVERSIONS###########
#If the user supplied the correct format of problems,the conversion you return will folloow these rules:
#There should be a single space between the operator and the longest of the two operands
#The operator  will be on the same line as the second operand,both operands will be in the same order as provided(the first will be the top one and the second will be the bottom).
#Numbers should be right-aligned.
#There should be four spaces between each problem.
#There should be dashes at the bottom of each problem.The dashes should run along the entire lenght of each problem individuall.

#####DEVELOPMENT##########
#Write your code in arithmetic_arranger.py.
#For development you can use main.py to test your arithmetic_arranger() function.
#Click the run botton and main.py will run.

#########TESTING##########


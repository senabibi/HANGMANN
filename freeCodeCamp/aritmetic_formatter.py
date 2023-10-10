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
            ####################################
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
            space.append(differ_index+1)
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

   
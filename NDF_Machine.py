import json
"""Function that accepts one character at the time as an input and then checks for each character the transition from state to state according to the transition function""" 
def CheckCharByChar(dictionary):
     continueInput = True
     transitions = dictionary["transitions"]
     numberOfStates = dictionary["noStates"]
     finalStates = dictionary["finalStates"]
     state = dictionary["originalState"]
     numberOfTransitions = dictionary["noTransitions"]
     actualList = [False for i in range(numberOfStates)]
     actualList[state-1] = True
     helperList = [False for i in range(numberOfStates)]
    
     while(True):
         input_char = input("Please enter one character. Press Enter if you want to stop giving input.")
         
         if input_char == "":
             break
        

         for i in range(numberOfStates):
             if actualList[i]== True:
                 tmp =  str(i+1) +input_char 
                 for j in range(numberOfTransitions):
                      t = transitions[j][:2]
                      if  tmp == t:
                         k = int(transitions[j][2])
                         helperList[k-1] = True                     
         actualList = helperList.copy()
         helperList = [False for i in range(numberOfStates)]
         if  not any(actualList):
              break
     CheckingTheFinalStates(finalStates,actualList) 
     
       
             
                 
"""Function that accepts the whole word as an input and then checks for each letter the transition from state to state according to the transition function"""      
def CheckTheWord(dictionary):
     continueInput = True
     transitions = dictionary["transitions"]
     numberOfStates = dictionary["noStates"]
     finalStates = dictionary["finalStates"]
     state = dictionary["originalState"]
     numberOfTransitions = dictionary["noTransitions"]
     actualList = [False for i in range(numberOfStates)]
     actualList[state-1] = True
     helperList = [False for i in range(numberOfStates) ]
    

     input_word = input("Please enter the word you want to check.\n")
     listOfLetters = list(input_word.strip()) #the letters of the word
     k = 0
     while(k < len(listOfLetters)):
          for i in range(numberOfStates):
               if actualList[i]==True:
                    tmp =  str(i+1) + listOfLetters[k] 
                    for j in range(numberOfTransitions):
                         t = transitions[j][:2]
                         if  tmp == t:
                              p = int(transitions[j][2])
                              helperList[p-1] = True
          actualList = helperList.copy()
          helperList = [False for i in range(numberOfStates)]
          k = k + 1
          if  not any(actualList):
              break
     CheckingTheFinalStates(finalStates,actualList)     
          

"""Checks if at least one of the final states is True. This means that the word has been accepted."""
def CheckingTheFinalStates(finalStates,actualList):    
     accepted = False
     for i in range (len(finalStates)):
         if actualList[finalStates[i]-1] == True:
             accepted = True
     if accepted == True :
         print("The word is accepted.\n")
     else:
         print("The word is denied.\n")


"""Checking if the filename extension is .json"""               
def CheckingForValidFileName():
    while(True):
        NameOfTheFile = str(input("Please enter the title of the file (ex. input.json)\n"  ))            
        if NameOfTheFile.endswith(".json"):
            break
        print("The FileName is not valid .Try again!")
        continue
    return NameOfTheFile.strip("\n")



    
def main():
    NameOfTheFile = CheckingForValidFileName()
    with open(NameOfTheFile,'r') as outfile:
       data = json.load(outfile)
       continueInput = 1
       while(continueInput==1):
            inputt = input("Enter 1 if you want to enter the whole word for testing or 0 if you want to give character-character\n")
            if inputt.isdigit() and inputt in [0,1]:
               print("INCORRECT INPUT!!")
               continue
            if int(inputt)==1:
               CheckTheWord(data)
            else:
               CheckCharByChar(data)    
            while(True):
                continueInput = input("Press 1 if you want to check more words or 0 to stop\n")
                if len(continueInput)==1 and (int(continueInput) ==1 or int(continueInput)== 0):
                    continueInput=int(continueInput)
                    break         
                 
if __name__== "__main__":
    main()

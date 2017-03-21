name_of_mydocument = 'tuesdayafternoon.txt'                
file_input = open(name_of_mydocument, 'r')           

line = file_input.readline()                          
print(line, end = "")
line = file_input.readline()                         
print(line, end = "")
line = file_input.readline()                         
print(line, end = "")

line = file_input.readline()                          

line_counter = 1                                    
stanza_counter = 1

while line != '':                                     

    if line == '\n':                                    
      stanza_counter += 1                                      
      print ()                                              
    else:                                                
      print(line_counter, end = '') 
      print(")   ", end = "")
      print(line, end = '') 
      line_counter += 1                                    
    line = file_input.readline()                        
    
print ()                                               
print ()                         
print ("The number of stanzas is ",  stanza_counter)   

file_input.close()

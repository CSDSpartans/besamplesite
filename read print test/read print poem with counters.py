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
total_lines_in_file = 2

while line != '':                                     
  total_lines_in_file += 1
  if line == '\n':                                    
      stanza_counter += 1                                      
      print ()                                              
  else:                                                
      print(line_counter, end = '')
      if line_counter >= 10:
        print(")  ", line, end = "")
      else:
        print(")   ", line, end = "")
      line_counter += 1  
 
  line = file_input.readline()                        
    
print ()                                               
print ()                         
print ("The number of stanzas is ",  stanza_counter)   
print ("The total number of lines in this file are", total_lines_in_file)
print ("The song Tuesday Afternoon first appeared in the album Days Of Future Passed which was released in 1967.")
print ("The members of the Moody Blues are Mike Pinder, Graeme Edge, Justin Hayward, Ray Thomas and John Lodge.")
file_input.close()

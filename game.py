import pyttsx3
talk = pyttsx3.init()
count=0;
talk.say("Enter your name please")
talk.runAndWait()
name=str(input("Enter your name please:"))
print("Hello",name,"and welcome to the quiz game hope you will enjoy it, All the best!")
print("Here are some basic rules \n •Each right answer gives you 1 point \n •wrong answer gives you 0 points \n\n LET'S Start")

# 1st question
print("1) What is the most abundant gas in the Earth’s atmosphere?")
talk.say("What is the most abundant gas in the Earth’s atmosphere?")
talk.runAndWait()
q1=str(input("Enter Your Answer:"))
if(q1.upper()=="NITROGEN"):
	count+=1;
	print("Correct answer")
	talk.say("Correct answer")
	talk.runAndWait()
else:
	print("Wrong answer")
	talk.say("Wrong answer")
	talk.runAndWait()
	print("the Correct answer is NITROGEN")
	talk.say("the Correct answer is NITROGEN")
	talk.runAndWait()

# 2nd question
print("2) Roughly how long does it take for the sun’s light to reach Earth?")
talk.say("Roughly how long does it take for the sun’s light to reach Earth?")
talk.runAndWait()
q2=int(input("Enter Your Answer: "))
if(q2==8):
	count+=1;
	print("Correct answer")
	talk.say("Correct answer")
	talk.runAndWait()
else:
	print("Wrong answer")
	talk.say("Wrong answer")
	talk.runAndWait()
	print("the Correct answer is 8")
	talk.say("the Correct answer is 8")
	talk.runAndWait()

# 3rd question
print("3) At what temperature are Celsius and Fahrenheit equal?")
talk.say("At what temperature are Celsius and Fahrenheit equal?")
talk.runAndWait()
q3=int(input("Enter Your Answer: "))
if(q3==-40):
	count+=1;
	print("Correct answer")
	talk.say("Correct answer")
	talk.runAndWait()
else:
	print("Wrong answer")
	talk.say("Wrong answer")
	talk.runAndWait()
	print("the Correct answer is -40")
	talk.say("the Correct answer is -40")
	talk.runAndWait()

#4th question
print("4) What is the biggest planet in our solar system?")
talk.say("What is the biggest planet in our solar system?")
talk.runAndWait()
q4=str(input("Enter Your Answer: "))
if(q4.upper()=="JUPITER"):
	count+=1;
	print("Correct answer")
	talk.say("Correct answer")
	talk.runAndWait()
else:
	print("Wrong answer")
	talk.say("Wrong answer")
	talk.runAndWait()
	print("the Correct answer is JUPITER")
	talk.say("the Correct answer is JUPITER")
	talk.runAndWait()

#5th question
print("5) What name is given for the number of protons found in the nucleus of an atom?")
talk.say("What name is given for the number of protons found in the nucleus of an atom?")
talk.runAndWait()
q5=str(input("Enter Your Answer: "))
if(q5.upper()=="ATOMIC NUMBER"):
	count+=1;
	print("Correct answer")
	talk.say("Correct answer")
	talk.runAndWait()
else:
	print("Wrong answer")
	talk.say("Wrong answer")
	talk.runAndWait()
	print("the Correct answer is ATOMIC NUMBER")
	talk.say("the Correct answer is ATOMIC NUMBER")
	talk.runAndWait()




#END OF PROGRAM
print("congratulations you completed the quiz nicily.If you want you can collect your report from the file also. You Total points are",count)
talk.say("congratulations you completed the quiz nicily. If you want you can collect your report from the file also ")
talk.runAndWait()
f = open("result.txt","w+")
f.write("congratulations " +name+ " you completed the quiz nicily. You got total number of point %d"%count)
f.close()

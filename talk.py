import pyttsx3
engine = pyttsx3.init()
n=str(input("Enter:"));
if (n=="shruti"):
	engine.say("Shruti is very beautiful,gorgeous,loving,caring. She is the only one in my life i can fully love. She is the only one in my life i can share each and every secret. She is the only one thst totally understands me and take care of me when ever i needed. I also always take care of here big and small problems. I always try to keep here safe and happy.")
elif (n=="harsh"):
	engine.say("I am stupid laughing emoji")
elif(n=="shabd"):
	engine.say("shabd is one of my closest friends. His nature is so good. He is a very intelligent. His nataure is always to help everyone. He is very time managing")
else:
	engine.say("The persone description is not mentioned ")
engine.runAndWait()
# create aprogram of displating the questions to the user like kbc 
# Use List data type to store questions and their correct answers
# Display the final amount the person is taking home after plating the game 



questions = [
    ["Who invented the telephone?", "Thomas Edison", "Alexander Graham Bell", "Newton", "Einstein", 2,1000],

    ["Which is the largest continent?", "Africa", "Europe", "Asia", "Australia", 3,2000],

    ["How many bones are there in an adult human body?", "206", "201", "210", "196", 1,5000],

    ["Which country is known as the Land of the Rising Sun?", "China", "Thailand", "Japan", "South Korea", 3,10000],

    ["What is the chemical formula of water?", "CO2", "H2O", "O2", "NaCl", 2,20000],

    ["Who was the first man to walk on the Moon?", "Yuri Gagarin", "Neil Armstrong", "Buzz Aldrin", "Michael Collins", 2,50000],

    ["Which is the fastest land animal?", "Lion", "Horse", "Cheetah", "Tiger", 3,100000],

    ["What is the national animal of Nepal?", "Tiger", "Cow", "Rhino", "Yak", 2,200000],

    ["Which language is used to structure web pages?", "CSS", "Python", "HTML", "Java", 3,500000],

    ["How many players are there in a cricket team?", "9", "10", "11", "12", 3,1000000]
]
i=0
amt=0
length=len(questions)
while True:
    
    for j in range(0,10):
        
        if(j>length-1):
            break
        print(questions[j][0])
        print("options:",questions[j][1:5])
        inp=int(input("enter your answer:"))
        if(inp!=questions[j][5]):
            print("your answer is not correct")
            print("your total win is amt")
            
            break
        else:
            print("answer is correct ")
            amt=questions[j][6]+amt
            print("your won :\t Rs",questions[j][6])
    break
        


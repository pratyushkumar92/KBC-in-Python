question=["What is the Capital of India?","Who is the PM of India","What it the national animal of India?","Who is the finance minister of India?","What is the capital of Bihar?","Who does host KBC?","Who is the captain of Indian cricket team?","How many colors are there in rainbow?","Who built GT Road?","What is Indian currency?","Geeta Phogat belongs to which state?","Who is the cheif justice of India?","Who is the chief of Air force?","Who is the chief of Indian Army?","Who is the chief of Indian Navy?"]
f_option=["Kolkata","Atal Bihari Vajpai","Tiger","Arun Jaitely","Patna","Aamir Khan","MS DHONI",3,"Sher shah","Yen","Delhi","H.J Kania","Birender Singh Dhanoa","Bipin Rawat","Sunil Lanba"]
s_option=["Delhi","L K Advani","Cow","Sushma Swaraj","Lucknow","Shahrukh Khan","Youraj Singh",7,"Balban","Dollar","Haryan","Jagdish Singh Khehar","Arup Raha","Dalbir Singh","Robin K Dhowan"]
t_option=["Mumbai","Rajnath Singh","Dog","Mulayam Singh","Chandigarh","Amitabh Bachchan","Sachin Tendulkar",4,"Shah Jahan","Rupia","Rajasthan","Dipak Misra","Anil Kumar Browne","Bikram Singh","Devendra Kumar Joshi"]
l_option=["Ahmedabad","Narendra Modi","Ox","Nitish Kumar","Ranchi","Ajay Devgan","Virat Kohli",5,"Akbar","Euro","Bihar","Kamal Narain Singh","Pradeep Vasant Naik","V K Singh","Nirmal Kumar Verma"]
#all_option=[f_option,s_option,t_option,f_option]
index=0
prize=[1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,11000,12000,13000,14000,15000]
money=0
ans_key=[2,4,1,1,1,3,4,2,1,3,2,3,1,1,1]
totalquestion=len(question)
while index<totalquestion:
    print question[index]
    print f_option[index]
    print s_option[index]
    print t_option[index]
    print l_option[index]
    answer=int(raw_input("Enter your Option"))
    if answer==ans_key[index]:
        print "Right Answer"
        money=money+prize[index]
        print "You have won" + str(money)
        if index==4:
            print "Aapne pehla pdaw pura kr liya hai or aap jeet chuke hai Rs"+str(money)
        if index==9:
            print "Aapne Dusra pdaw pura kr liya hai or aap jeet chuke hai Rs"+str(money)
        if index==9:
            print "Aapne Tino pdaw pura kr liya hai or aap jeet chuke hai Rs"+str(money)
    else:
        print "Wrong Answer"
        print "You have won"+str(money)
        break
    index=index+1
print "Congratulations, You have completed this game and won :) Rs"+str(money)

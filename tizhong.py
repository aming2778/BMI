user_weight =float (input ("请输入你的体重(单位:kg)"))
user_height =float (input ("输入你的身高(单位:m)"))
user_BMI = user_weight / (user_height ** 2)
print(f"您的BMI为:{user_BMI:.2f}")
if user_BMI < 18.5:
    print ("💀")
elif user_BMI < 25:(
    print ("您的身体很健康"))
else:
    print ("🐖")
#BMI.py
height, weight = eval(input("请输入身高(米)和体重(公斤)[逗号隔开]: "))
bmi = weight / pow(height, 2)
print("BMI={:.2f}".format(bmi))
who,net="",""
if bmi<18.5:
    who,net="偏瘦","偏瘦"
elif 18.5<=bmi<24:
    who,net="正常","正常"
elif 24<=bmi<25:
    who,net="正常","偏胖"
elif 25<=bmi<28:
    who,net="偏胖","偏胖"
elif 28<bmi<30:
    who,net="偏胖","肥胖"
else:
    who,net="肥胖","肥胖"
print("BMI= who({}),new({})".format(who,net))

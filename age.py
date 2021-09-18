driving = input('請問你是否開過車? ')
if driving != '有' and driving != '沒有':
	print('只能輸入是或否')
	raise SystemExit

age = input('請問你的年齡? ')
age = int(age)
if driving == '是':
	if age >= 18:
		print('你通過測驗了')
	else:
		print('奇怪，你怎麼會有開過車')
elif driving == '否':
	if age >= 18:
		print('可以考駕照了')
	else:
		print('很好，再過幾年可以考')

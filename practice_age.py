driving = input('你有無開過車?')
if driving != '有' and driving != '沒有':
	print('請回答有或沒有')
	raise SystemExit


age = input('你的年齡?')
age = int(age)

if driving == '有':
	if age >= 18:
		print('合格')
	else:
		print('你怎開過車')
elif driving == '沒有':
	if age >= 18:
		print('考駕照')
	else:
		print('請再等幾年')
else:
	print('請回答有或沒有')
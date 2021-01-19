password = 'a123456'
pwd = 3
while True:
	password = input('請輸入密碼:')
	if password == 'a123456':
		print('登入成功')
		break
	else:
		pwd = pwd - 1  
		print('密碼錯誤,剩餘', pwd , '機會')
		if pwd == 0:
			break


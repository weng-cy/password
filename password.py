while True:
	password = input('請輸入密碼')
	if password == 'a123456':
		print('登入成功')
		break
	else:
		print('密碼錯誤,還有兩次機會')
		password = input('請重新輸入密碼')
		if password == 'a123456':
			print('登入成功')
			break
		else:
			print('密碼錯誤,還有一次機會')
			password = input('請重新輸入你的密碼')
			if password == 'a123456':
				print('登入成功')
				break
			else:
				print('密碼錯誤,已輸入三次密碼錯誤')
				break
				

		
			
		
		
		

		

		

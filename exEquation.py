__author__ = "Trần Văn Hạnh"
from math import * 
"""
Lập phương trình thực hiện công việc sau:
    1. Nhập ba số a, b, c bất kỳ từ bàn phím
    2. Giải và biện luận nghiệm của phương trình bậc 2: ax^2 + bx + c =0 ( kể cả trường hợp nghiệm phức)
    3. Đưa kết quả ra màn hình
"""
def solveFirstEqua():
	try: 
		a = float(input('Vui lòng nhập hệ số a: '))  
		b = float(input('Vui lòng nhập hệ số b: '))  

		if a != 0 and b != 0:
			x = round(-b/a,2)
			print("Nghiệm của phương trình là: x = %s" %x)
		elif a != 0 and b == 0:
			x = 0
			print("Nghiệm của phương trình là: x = %s" %x)
		else:
			print("Không phải là phương trình")
	except ValueError:
		print("Vui lòng nhập lại giá trị số tự nhiên: ")

def solveSecondEqua():
	try: 
		a = float(input('Vui lòng nhập hệ số a: '))  
		b = float(input('Vui lòng nhập hệ số b: '))  
		c = float(input('Vui lòng nhập hệ số c: '))  

		if(a != 0 and b != 0 and c != 0):
			# calculate the discriminant  
			d = (b**2) - (4*a*c)  
			  
			# find two solutions  
			if d < 0:
			    print("Phương trình này vô nghiệm")
			elif d == 0:
			    x = round((-b + sqrt(b**2-4*a*c))/2*a, 2)
			    print("Phương trình này có một nghiệp duy nhất: ", x)
			else:
			    x1 = round((-b + sqrt(b**2-4*a*c))/2*a, 2)
			    x2 = round((-b - sqrt(b**2-4*a*c))/2*a, 2)
			    sp = (" ")*10
			    print("Phương trình này có 2 nghiệm: \n{sp} x1 = {x1}\n{sp} x2 = {x2} ".format(x1 = x1, x2 = x2, sp = sp))
		elif a != 0 and b != 0 and c == 0:
			x1 = 0
			x2 = round(-b/a, 2)
			sp = (" ")*10
			print("Phương trình này có 2 nghiệm: \n{sp} x1 = {x1}\n{sp} x2 = {x2} ".format(x1 = x1, x2 = x2, sp = sp))
		else:
			print("Không phải là phương trình mà bạn muốn giải!")
	except ValueError:
		print("Vui lòng nhập lại giá trị số tự nhiên: ")
# ---------------------------------------------------------------
print("-------- Giải phương trình bậc nhất và bậc hai ----------")
print("Bạn muốn giải phương trình nào ?\n- Nhập 1 cho bậc phương trình bậc 1 \n- Nhập 2 cho phương trình bậc 2")
try:
	x = int(input())
	if x == 1:
	    solveFirstEqua()
	else:
	    solveSecondEqua()
except:
	print("Vui lòng nhập lại sự lựa chọn:")

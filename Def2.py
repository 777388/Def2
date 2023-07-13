def def2(**kwargs):
	globals().update(kwargs)

def2(yup=lambda:(print("hellO"), print("goodbye")), mhm=lambda:(print("mhm"), print("howdy")))

yup()
mhm()

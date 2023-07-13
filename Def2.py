def def2(**kwargs):
	globals().update(kwargs)
a, b, c = 1, 2, 3
def2(yup=lambda:(print(f"hellO{a}"), print(f"goodbye{b}")), mhm=lambda:(print(f"mhm{c}"), print("howdy")))

yup()
mhm()

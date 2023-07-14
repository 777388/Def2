#global anonymous definition of mhm.
def def2(**kwargs):
	globals().update(kwargs)
def2(mhm = lambda mhm: mhm)
mhm(mhm) 

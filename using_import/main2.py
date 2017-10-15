from mkmsg_mod.MakeMsg import MsgUser

obj = MsgUser()
obj.add_data('Leo', 696.31415)
obj.add_data('tiZZY', 13.1132, 'tt@timail.com')
obj.add_data('baNG', 0.4544, 'Nope@yahoo.com.tw')
print (obj.make_msg())

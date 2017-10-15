import datetime 
class MsgUser(): #store user`s detail and make individual msgs
    user_detail = [] #a list of dicts
    msgli = [] #a list of msgs
    base_msg = """Hello, {name}!!
    You have to pay ${amount} NTD until next class.
    SentTime: {date}
    Thanks!
    """
    def add_data(self, name, amount, email=None):
        new_name = name[0].upper() + name[1:].lower()
        new_amount = '%.3f' %(amount)
        today_data = datetime.date.today()
        date_data = '{today.month}/{today.day}/{today.year}'.format(today=today_data)
        detail = {
            'Name' : new_name,
            'Amount' : new_amount,
            'Date' : date_data
        }
        if email is not None:
            detail['Email'] = email
        self.user_detail.append(detail)
    def get_detail(self):
        return self.user_detail
    def make_msg(self):
        for detail in self.user_detail:
            new_msg = self.base_msg.format(
                name = detail['Name'],
                amount = detail['Amount'],
                date = detail['Date']
                )
            self.msgli.append(new_msg)
        return self.msgli
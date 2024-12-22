from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

urlkb = InlineKeyboardMarkup(row_width=1)
urlbutton = InlineKeyboardButton(
    text='👨‍💻 Admin', url='https://t.me/Jamshid_dusel')
urlkb.add(urlbutton)


def create_social_btn(car_id):
    social_btn = InlineKeyboardMarkup(row_width=3)
    like = InlineKeyboardButton(text='👍', callback_data=f'like_{car_id}')
    dislike = InlineKeyboardButton(text='👎', callback_data=f'dislike_{car_id}')
    remove = InlineKeyboardButton(text='❌', callback_data='remove ')
    social_btn.add(like, remove, dislike)

    return social_btn

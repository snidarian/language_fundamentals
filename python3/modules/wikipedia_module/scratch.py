#!/usr/bin/python3

import wikipedia



#print(wikipedia.languages())



wikipedia.set_lang('ru')


page = wikipedia.page(title="мужчина")


print(page.summary)


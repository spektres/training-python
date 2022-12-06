# from isOdd import isOdd

# print(isOdd(3))
# print(isOdd(4))


# from progress.bar import Bar
# from time import sleep

# bar = Bar('Processing', max=20)
# for i in range(20):
#     sleep(1)
#     bar.next()
# bar.finish()


# import emoji
# print(emoji.emojize('Python es :pulgar_hacia_arriba:', language='es'))
# print(emoji.demojize('Python es 👍', language='es'))


# import matplotlib.pyplot as plt
# import numpy as np

# list = [1, 4, 2, -3, -4, -2, 5, 9]

# plt.plot(list)

# plt.show()


from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from bot_commands import *

app = ApplicationBuilder().token("5895711909:AAG3DPUIC1mnwlcj6Y_xOvHM4XMFYZm3qMY").build()

app.add_handler(CommandHandler("hello", hello_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("summ", summ_command))

print("server start")

app.run_polling()
# Pine-X-easy-widget
this simple widget with system info, time and date

чтобы изменить цвет фона, измените строку root['bg'] = '#000000' изначально на черный цвет, также не забудьте изменить цвет в строках date_info_label = tkinter.Label(text=get_date(), font= 'helvetica 25', bg= "black", fg='white')
вот пример с белым фоном и черным текстом
root['bg'] = '#ffffff'
date_info_label = tkinter.Label(text=get_date(), font='helvetica 25', bg="white", fg='black')

виджет также можно сделать без эффекта прозрачности, измените строку root.attributes("-alpha", 0.5) на root.attributes("-alpha", 1), если вы хотите изменить размер виджета вручную, затем удалите строку root.resizable(ширина = False, высота = False)

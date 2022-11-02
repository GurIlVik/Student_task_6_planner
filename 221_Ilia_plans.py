# С помощью графического интерфейса написать программу для сохранения дел.
# Программа будет записывать в текстовый файл строки, начинающиеся с +,
# если дело сделано и -, если не сделано.
# Дела нужно вывести в окно.
# Против дел - чекбоксы (окошечки с галочками)
# Над всеми делами строка для ввода нового дела, и кнопка "сохранить"оно дописывается к списку в конец.
# При запуске программа пытается открыть файл, загрузить старый список дел для продолжения работы.

# Усложнения:
# можно указывать даты и отмечать красным просроченные дела.
# можно отмечать сделанные дела зеленым.
# Можно сделать кнопку сортировки по датам или по алфавиту.
# Можно выводить несделанные дела выше или не выводить сделанные вовсе.
# Можно сделать файл отчёта, в который записывать только выполненные дела.

import tkinter as _t
from time import strftime
from tkinter.ttk import Checkbutton
from tkinter import LEFT, SINGLE, ttk, Listbox, END, StringVar, Scrollbar, Frame, Canvas, W, Label, Button
from functools import partial 
 


# открытие файла
def open_file(file_plan):
    try:
        f = open(file_plan, 'r', encoding='utf-8')
    except:
        f = open(file_plan, 'w', encoding='utf-8')
    f.close()
    return file_plan

# чтение файла на список дел
def ride_file(file_plan):
    count_plan = 0
    planner = []
    with open(file_plan, 'r', encoding='utf-8') as file:
        try:
            for line in file:
                list1 = []
                if len(line) == '':
                    pass
                else:
                    count_plan += 1
                    list1.append(line[:1])
                    list1.append(line[2:10])
                    list1.append(line[11:])
                    planner. append(list1)
                    list1 = []
        except:
            pass
    return count_plan, planner

# запись в файл памяти всех ранее сделаных дел
def memory_file(file, lis):
    print(lis)
    print(file)
    with open(file, 'a', encoding='utf-8') as fil:
        for line in lis:
            string = f'исполнено {str(line[1][:4])} года {str(line[1][4:6])} месяца {str(line[1][6:])} дня -  {str(line[2])}'
            fil.write(string)

# функция перезаписи списка дел без выполненых     
def write_file(file, lis):
    
    with open(file, 'w', encoding='utf-8') as fil:
        for line in lis:
            string = f'{str(line[0])} {str(line[1])} {str(line[2])}'
            fil.write(string)    
     
 # функция проверки ввода данных 
def check_user_input(user_day, user_mounth, user_yers):
    y = strftime('%Y')
    m = strftime('%m')
    d = strftime('%d')
    if user_day == '' or user_mounth == '' or user_yers == '':
        return True 
    elif int(y) > int(user_yers) or int(y) == int(user_yers) and int(m) > int(user_mounth) or int(y) == int(user_yers) and int(m) == int(user_mounth) and int(d) > int(user_day):
        return False
    else:
        return True


# функция отображения первого окна обработки списка
def display_win1(win, file_plan, window1, window2):
    # функция обновления
    def update_planning():
        display_win1(win, file_plan, window1, window2)
    # функция закрытия программы
    def close_program():
        win.destroy()
        
    # получение актуального времени 
    def update_clock():
        y = strftime('%Y')
        m = strftime('%m')
        d = strftime('%d')
        h = strftime('%H') 
        mi = strftime('%M')
        s = strftime('%S')
        main_time1 = _t.Label(window1, text=f'Сегодня {d} число {m} месяца {y} года. Время - {h}:{mi}:{s}')
        main_time2 = _t.Label(window2, text=f'Сегодня {d} число {m} месяца {y} года. Время - {h}:{mi}:{s}')
        main_time1.grid(column = 0, row = 0, columnspan=7)
        main_time2.grid(column = 0, row = 0, columnspan=7)
        win.after(1000, update_clock)
    update_clock()
    
    def lbl_list_ret(count_plan):
        result = []
        result2 = []
        for i in range(count_plan):
            result.append(f'label{i+1}')
            result2.append(f'label{i+1001}')
        return result, result2  
    # список значений переменных для флажка
    def bool_list_ret(count_plan):
        result = []
        for i in range(count_plan):
            res = f'bool_simbol{i+1}'
            res = _t.IntVar()
            result.append(res)
        return result 
    
    count_plan, planner = ride_file(file_plan)
    lbl_list, ldl_list2 = lbl_list_ret(count_plan)
    bool_list = bool_list_ret(count_plan)
    
    frame_container=Frame(window1)
    canvas_container=Canvas(frame_container, height=610, width=700)
    frame2=Frame(canvas_container)
    sb=Scrollbar(frame_container,orient="vertical",command=canvas_container.yview) # will be visible if the frame2 is to to big for the canvas
    canvas_container.create_window((0,0),window=frame2,anchor='nw')
    
    class Delo:
        def __init__(self, master, varik, count): 
            
            # функция удаления элемента списка дел безвозврата 
            def dellet_element_list(win10):
                name = nume_delo_list[self.count-1]
                list_1 = []
                with open(file_plan, 'r', encoding='utf-8') as file:
                    for line in file:
                        if line[11:] == name:
                            pass
                        else:
                            list_1.append(line)
                with open(file_plan, 'w', encoding='utf-8') as file:
                    for line in list_1:
                        file.write(line)
                win10.destroy()
                display_win1(win, file_plan, window1, window2)
            
            # функция записи дела в списке как выполненого
            def execute_element_list(win10):
                y = strftime('%Y')
                m = strftime('%m')
                d = strftime('%d')
                name = nume_delo_list[self.count-1]
                list_1 = []
                with open(file_plan, 'r', encoding='utf-8') as file:
                    for line in file:
                        list_1.append(line)
                with open(file_plan, 'w', encoding='utf-8') as file:
                    for line in list_1:
                        if line[11:] == name:
                            a =f'1 {y}{m}{d} {line[11:]}'
                            line = a
                        file.write(line) 
                win10.destroy()
                display_win1(win, file_plan, window1, window2)   
            
            # перевод дела из выполненых в невыполненые с сегодняшней датой
            def non_execute_element_list(win10):
                name = nume_delo_list[self.count-1]
                list_1 = []
                with open(file_plan, 'r', encoding='utf-8') as file:
                    for line in file:
                        list_1.append(line)
                with open(file_plan, 'w', encoding='utf-8') as file:
                    for line in list_1:
                        if line[11:] == name:
                            a =f'2{line[1:]}'
                            line = a
                        file.write(line)
                win10.destroy()  
                display_win1(win, file_plan, window1, window2)
                             
            # функция отображения всплывающего окна
            def open_windows():
                win10 = _t.Tk()
                win10.title('фиксирование флажка')
                win10.geometry('300x60')  
                return win10
                         
            # функция вызова доп окна в случае нажатия на флажек                     
            def prt():
                try:
                    win10.destroy()
                except:
                    pass        
                win10 = open_windows()     
                if self.varik.get() == 1:
                    but_win10 = _t.Button(win10, text='записать как исполненое?', command=partial(execute_element_list, win10))
                    but_win10.pack()
                    but_win10_2 = _t.Button(win10, text='Удалить эту запись без возврата?', command=partial(dellet_element_list, win10))
                    but_win10_2.pack()
                else:
                    but_win10_0 = _t.Button(win10, text='Сохранение с сегодняшней датой', command=partial(non_execute_element_list, win10))
                    but_win10_0.pack()
                win10.mainloop() 
                
 
            self.varik = _t.IntVar()
            self.count = count
            self.varik = varik
            self.cb = Checkbutton(
                master, variable=self.varik,
                onvalue=1, offvalue=0, command=prt)
            self.cb.grid(column=2, row=self.count)

    class Label_User_Delo:
        def __init__(self, res2,  frame2, count, text, znak, color):
            self.count = count
            self.res2 = res2
            self.text = text
            self.znak = znak
            self.color = color
            self.frame2 = frame2
            self.text_strvar1 = StringVar()
            self.text_strvar1.set(f'{self.znak} {self.text}')
            self.lbl = _t.Label(self.frame2, textvariabl = self.text_strvar1, font=('Bradley Hand Bold', 20), bg='Light Blue', fg=self.color, justify=LEFT)
            self.lbl.grid(column=0, row=self.count, sticky=W)
            
    class Label_User_Delo_Data:  
        def __init__(self, res3, frame2, count, text2, znak2, color):
            self.count1 = count
            self.res3 = res3
            self.text2 = text2
            self.znak2 = znak2
            self.color = color
            self.frame2 = frame2
            self.text_strvar2 = StringVar()
            self.text_strvar2.set(f'{self.znak2} {self.text2}')
            self.lbl2 = _t.Label(self.frame2, textvariabl = self.text_strvar2, font=('Bradley Hand Bold', 20), bg='Light Blue', fg=self.color, justify=LEFT)
            self.lbl2.grid(column=1, row=self.count1, sticky=W)  
            

    label_1_list = []
    label_2_list = []
    buuton_1_list = []
    nume_delo_list = []
    
    # цикл разверстки списка на экран
    def cycle_show_list(planner, lbl_list, ldl_list2, bool_list):
        count = 0
        count_green = 0
        count_black = 0
        count_red = 0
        for i, elem in enumerate(planner):
            res2 = lbl_list[count]
            res3 = ldl_list2[count]
            res4 = bool_list[count]
            nume_delo_list.append(elem[2])
            count += 1
            check = True
            if elem[1][6:] == 'мя':
                pass 
            else:
                check =  check_user_input(elem[1][6:], elem[1][4:6], elem[1][:4])
            fg_black = 'black'
            znak = '-'
            text = elem[2]
            if len(elem[2]) < 40:
                text = text + ' '*(50 - len(elem[2]))
            text2 = f'{elem[1][6:]}:{elem[1][4:6]}:{elem[1][:4]}'
            znak2 = 'до '
            if elem[0] == '1':  
                znak = '+' 
                fg_black = 'green' 
                znak2 = 'исп '  
                res4.set(1)
                count_green +=1
            else:
                if check == False:
                    fg_black = 'red'
                    count_red += 1
                else:
                    count_black += 1
                res4.set(0)
                if elem[1][0] == "Н":
                    text2 = f'Без времени'
            
            res2 = Label_User_Delo(res2, frame2, count, text, znak, fg_black)    
            res3 = Label_User_Delo_Data(res3, frame2, count, text2, znak2, fg_black)  
            res = Delo(frame2, res4, count)
            label_1_list.append(res2)
            label_2_list.append(res3)
            buuton_1_list.append(res)
            
        lebl_stat = Label(window1, text=f'У Вас на сегодня {count} дел из них: {count_green} выполнено, {count_black} требую выполнения и не просрочены, {count_red} просроченных ', font=(...))
        lebl_stat.grid(column=0, row= 7)
        
        
        
            
    cycle_show_list(planner, lbl_list, ldl_list2, bool_list) 
            
    frame2.update() # update frame2 height so it's no longer 0 ( height is 0 when it has just been created )
    canvas_container.configure(yscrollcommand=sb.set, scrollregion="0 0 0 %s" % frame2.winfo_height()) # the scrollregion mustbe the size of the frame inside it,      
    canvas_container.grid(column=0, row=1)
    sb.grid(column=1, row=1)
    frame_container.grid(column=0, row=1, rowspan=6)
    
     # функция сортировки по дате
    def sort_by_date(planner=planner):
        label_1_list.clear()
        label_2_list.clear()
        buuton_1_list.clear()
        nume_delo_list.clear()
        planner = sorted(planner, key = lambda elem: elem[1])
        cycle_show_list(planner, lbl_list, ldl_list2, bool_list) 
    
    # функция сортировки по алфавиту
    def sort_by_alfabet(planner=planner):
        planner = sorted(planner, key = lambda elem: elem[2])
        cycle_show_list(planner, lbl_list, ldl_list2,  bool_list)  
    
    # Сортировка без выполненых    
    def sort_without_completed(planner=planner):
        planner = [i for i in planner if i[0] == '2'] 
        cycle_show_list(planner, lbl_list, ldl_list2,  bool_list) 
    
    def delet_completed(planner=planner):
        file_completed = open_file('Complected.txt')
        list_memory = [i for i in planner if i[0] == '1']
        planner = [i for i in planner if i[0] == '2']
        memory_file(file_completed, list_memory)
        write_file(file_plan, planner)
        count_plan, planner = ride_file(file_plan)
        lbl_list, ldl_list2 = lbl_list_ret(count_plan)
        bool_list = bool_list_ret(count_plan) 
        cycle_show_list(planner, lbl_list, ldl_list2,  bool_list) 
        
    def print_complected():
        try:
            file = open ('Complected.txt', 'r', encoding='utf-8') 
            for line in file:
                print(line) 
        except:
            print('Что - то случилось с файлом')
        finally:
            file.close()
        
        
    clic1 = Button(window1, text= "ОБНОВИТЬ", width=24, command=update_planning)
    clic1.grid(column=1, row=1)
    clic2 = Button(window1, text= "Сортировать по дате", width=24, command=sort_by_date)
    clic2.grid(column=1, row=2)
    clic3 = Button(window1, text= "Сортировать по алфавиту", width=24, command=sort_by_alfabet)
    clic3.grid(column=1, row=3)
    clic4 = Button(window1, text= "Показать список без выполненых", width=24, command=sort_without_completed)
    clic4.grid(column=1, row=4)
    clic5 = Button(window1, text= "Удалить из списка выполненые", width=24, command=delet_completed)
    clic5.grid(column=1, row=5)
    clic6 = Button(window1, text= "Распечатать все выполненые", width=24, command=print_complected)
    clic6.grid(column=1, row=6)
    clic7 = Button(window1, text= "Закрыть программу", width=24, command=close_program)
    clic7.grid(column=1, row=7)
    
    
    
# функция отображения второго окна записи данных о предстоящем деле в файл         
def display_win2(win, file_plan, window1, window2):
    user_yers = ''
    user_mounth = ''
    user_day = ''
    
    text_strv = StringVar()
    lbl_error = _t.Label(window2, textvariable = text_strv, font=('Bradley Hand Bold', 20), bg='Light Blue', fg='red')
    lbl_error.grid(column=0, columnspan=6, row=7)
    
    # функция преобразования цифры в строку
    def trasform(res):
        res = str(res)
        if len(res) == 1:
            res = '0'+ res
        return res   
    # функция подтверждения года события
    def input_yers():
        res = ''
        for i in btl1_window2.curselection():
            res = btl1_window2.get(i)
        res = str(res)
        if res != '':
            bbl11_window2.destroy()
            lbl_res_yers = _t.Label(window2, text = res, font=('Bradley Hand Bold', 18), bg='Light Blue', width=11)
            lbl_res_yers.grid(column=2, row=4)
        nonlocal user_yers
        user_yers = res
    # функция подтверждения месяца события    
    def input_mounth():
        res = ''
        for i in btl2_window2.curselection():
            res = btl2_window2.get(i)
        res = trasform(res)
        if res != '':        
            bbl21_window2.destroy()
            lbl_res_mounth = _t.Label(window2, text = res, font=('Bradley Hand Bold', 18), bg='Light Blue', width=11)
            lbl_res_mounth.grid(column=5, row=4)
        nonlocal user_mounth
        user_mounth = res
    # функция подтверждения дня события         
    def input_day (x = 0):       
        res = ''
        for i in btl3_window2.curselection():
            res = btl3_window2.get(i)
        res = trasform(res)
        if res != '':
            bbl31_window2.destroy()
            lbl_res_day = _t.Label(window2, text = res, font=('Bradley Hand Bold', 18), bg='Light Blue', width=11)
            lbl_res_day.grid(column=8, row=4) 
            if x == 1:
                return lbl_res_day
        nonlocal user_day
        user_day = res 
    
    # функция записи дела в файл без указания времени
    def write_non_time(x=0):
        res =  user_delo.get() 
        if len(res) > 40:
            text_strv.set('введенная дата не может быть записана, слишком длинная') 
        elif res == '':
            text_strv.set('Внимание ошибка ввода данных без указания даты') 
        else:
            user_delo.delete(0, END)
            string = '2 НетВремя ' + res + '\n'
            with open(file_plan, 'a', encoding='utf-8') as file:
                file.write(string)
            text_strv.set('данные без указанной даты введены верно')
               
    # функция записи дела в файл с указаной датой
    def write_time(x=0):
        nonlocal user_day
        nonlocal user_mounth
        nonlocal user_yers
        res =  user_delo.get()
        user_delo.delete(0, END)
        check = check_user_input(user_day, user_mounth, user_yers)
        if len(res) > 80:
            text_strv.set('введенная дата не может быть записана, слишком длинная') 
        elif check == False:
            text_strv.set('введенная дата меньше сегодняшнего дня')
        else:
            if user_day == '' or user_mounth == '' or user_yers == '':
                text_strv.set('возможно ошибка при загрузке данных с указанной датой')
                if res == '' and user_day == '' and user_mounth == '' and user_yers == '':
                    text_strv.set('')
            else: 
                string = '2 '+ user_yers + user_mounth + user_day + ' ' + res + '\n'  
                with open(file_plan, 'a', encoding='utf-8') as file:
                    file.write(string)
                text_strv.set('данные с указанной датой введены верно')
         
        user_yers = ''
        user_mounth = ''
        user_day = ''
        
        # display_win2(win, file_plan, window1, window2)
        bbl11_window2 = _t.Button(window2, text='подтведить', command=input_yers)
        bbl11_window2.grid(column=2, row=4) 
        if x == 'y':
            return bbl11_window2
        bbl21_window2 =_t.Button(window2, text='подтведить', command=input_mounth)
        bbl21_window2.grid(column=5, row=4)
        if x == 'm':
            return bbl21_window2
        bbl31_window2 = _t.Button(window2, text='подтведить', command=input_day)
        bbl31_window2.grid(column=8, row = 4)
        if x == 'd':
            return bbl31_window2
        davi = input_day(x = 1)
        davi.destroy()
        print(davi)
        print(type(davi))
    
    # функция сброса не верно указанных дат
    def write_time_free():
        display_win2(win, file_plan, window1, window2)
    
    
    lbl_window2 = _t.Label(window2, text='напишите новое дело:', 
                            width=92, height=2, 
                            font=('Bradley Hand Bold', 18), bg='Light Blue')         
    lbl_window2.grid(column = 0, row = 1, columnspan=17, padx=10, pady=10, ) 
    user_delo = _t.Entry(window2,
                         font=('Bradley Hand Bold', 18), 
                         bg='Light Blue', width=92,)   
    user_delo.grid(column = 0, row = 2, columnspan=17, padx=10, pady=10) 
    
    btl_write_non_time = _t.Button(window2, text = 'Записать без указания даты', width=62,
                            bg='Light Blue', command= write_non_time)
    btl_write_non_time.grid(column=0, columnspan=6, row=3)
    
    btl_write_time = _t.Button(window2, text = 'Записать c указанной датой', width=62,
                            bg='Light Blue', command= write_time)
    btl_write_time.grid(column=0, columnspan=6, row=6)
    
    btl_write_time_free = _t.Button(window2, text = 'СБРОС (нажмите в случае не верно указанной даты', width=62,
                            bg='Light Blue', command= write_time_free)
    btl_write_time_free.grid(column=0, columnspan=6, row=5)
    
            
    lbl1_window2 = _t.Label(window2, text = 'введите год: ', font=('Bradley Hand Bold', 18), bg='Light Blue')
    btl1_window2 = Listbox(window2, width=5, height=12, selectmode=SINGLE)
    bbl11_window2 = write_time(x='y')
    for i in reversed(range(2022,2222)):
        btl1_window2.insert(0, i)
    lbl1_window2.grid(column=0, row=4)
    btl1_window2.grid(column=1, row=4)  
        
    lbl2_window2 = _t.Label(window2, text = 'введите месяц: ', font=('Bradley Hand Bold', 18), bg='Light Blue')
    btl2_window2 = Listbox(window2, width=5, height=12, selectmode=SINGLE)
    bbl21_window2 = write_time(x='m')
    for i in reversed(range(1,13)):
        btl2_window2.insert(0, i)
    lbl2_window2.grid(column=3, row=4)
    btl2_window2.grid(column=4, row=4)
    
    lbl3_window2 = _t.Label(window2, text = 'введите день: ', font=('Bradley Hand Bold', 18), bg='Light Blue')
    btl3_window2 = Listbox(window2, width=5, height=31, selectmode=SINGLE)
    bbl31_window2 = write_time(x='d')
    for i in reversed(range(1,32)):
        btl3_window2.insert(0, i)
    lbl3_window2.grid(column=6, row = 4)
    btl3_window2.grid(column=7, row = 3, rowspan=5)
                         
# основная функция запуска программы
def start_program():
    file_plan = open_file('plan.txt') 
    win = _t.Tk()
    win.title('СПИСОК ДЕЛ')
    win.geometry('1000x750')
    tab_control = ttk.Notebook(win)
    window1 = ttk.Frame(tab_control)
    window2 = ttk.Frame(tab_control)
    tab_control.add(window1, text='Список дел')  
    tab_control.add(window2, text='Запись дел')
    # tab_control.pack(expand=1, fill='both') 
    tab_control.grid(column=0, row=0)
    display_win1(win, file_plan, window1, window2)
    display_win2(win, file_plan, window1, window2)
    win.mainloop()
    
if __name__ == "__main__":
    start_program()
    
#   шрифты - зачеркивание  
#     font1 = font.Font(family= "Arial", size=11, weight="normal", slant="roman", underline=True, overstrike=True)
# label1 = ttk.Label(text="Hello World", font=font1)
# https://pythonru.com/uroki/rabota-s-cvetami-i-shriftami-tkinter-7
# https://younglinux.info/tkinter/widget
# https://pythonru.com/uroki/obuchenie-python-gui-uroki-po-tkinter
# https://vk.com/@codeby_net-izuchaem-python-na-praktike-pishem-analog-utilit-wc-i-split
# https://python-scripts.com/tkinter-widgets-example
# 'Bradley Hand Bold' - текстовый шрифт 
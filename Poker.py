import tkinter as tk

#継承
class Application(tk.Frame):
    def __init__(self, root=None):
        #オーバーライド
        super().__init__(root, width=380, height=540,
                         bd=1, relief='groove')
        self.root = root
        self.pack()
        self.pack_propagate(0)
        self.create_widgets()

#widgetの作成    
    def create_widgets(self):
        
        #label
        label=tk.Label(self,text='ポーカーの手札の強弱が分かります',width=200)
        label.pack(side="top")

        #radiobutton
        self.selected_radio = tk.StringVar()

        #プレイング人数が少ないほうが勝率は高い
        #UTG：かなり強いハンドでのみ参加。多人数参戦してきた時に備える。
        radio_1 =tk.Radiobutton(self,text="UTG",value="UTG",
                                variable=self.selected_radio,command=self.image_utg)

        #SB　：そこそこのハンドでも参加。状況見て参加を決める。
        radio_2 =tk.Radiobutton(self,text="MP",value="MP",
                                variable=self.selected_radio,command=self.image_mp)
        
        #BB:ポジションでは優位な反面、どんなに弱いハンドでも参加費を強制的に払うリスク
        radio_3 =tk.Radiobutton(self,text="CO",value="CO",
                                variable=self.selected_radio,command=self.image_co)
        
        #最も有利。攻めることを意識。
        radio_4 =tk.Radiobutton(self,text="BTN",value="BTN",
                                variable=self.selected_radio,command=self.image_btn)


        #有利。攻めることを意識。
        radio_5 =tk.Radiobutton(self,text="SB",value="SB",
                                variable=self.selected_radio,command=self.image_sb)
        
        radio_1.pack()
        radio_2.pack()
        radio_3.pack()
        radio_4.pack()
        radio_5.pack()

         # 決定ボタン
        decide_btn = tk.Button(self,text="選択",command=self.submit)
        decide_btn.pack()
        

        #キャンバス self忘れないように
        self.canvas = tk.Canvas(self, bg="white", width=287, height=290)
        self.canvas.pack(side='bottom')


    def submit(self):
        print("ボタンが押された") 
        print(self.selected_radio.get()) 
        #if self.selected_radio.get()=="UTG":
             #画像ファイルを指定する
             #self.img_file = tk.PhotoImage(file = "assets/utg_101.png")
             
             #画像ファイルをキャンバスの(0,0)に合わせて表示してみる
             #self.canvas.create_image(140,140,image = self.img_file)

    def image_utg(self):
        #画像ファイルを指定する
             self.img_file = tk.PhotoImage(file = "assets/utg.png")
             
             #画像ファイルをキャンバスの(0,0)に合わせて表示してみる
             self.canvas.create_image(150,145,image = self.img_file)

    def image_mp(self):
        #画像ファイルを指定する
             self.img_file = tk.PhotoImage(file = "assets/mp.png")
             
             #画像ファイルをキャンバスの(0,0)に合わせて表示してみる
             self.canvas.create_image(148,148,image = self.img_file)

    def image_co(self):
        #画像ファイルを指定する
             self.img_file = tk.PhotoImage(file = "assets/co.png")
             
             #画像ファイルをキャンバスの(0,0)に合わせて表示してみる
             self.canvas.create_image(145,150,image = self.img_file)

    def image_btn(self):
        #画像ファイルを指定する
             self.img_file = tk.PhotoImage(file = "assets/btn.png")
             
             #画像ファイルをキャンバスの(0,0)に合わせて表示してみる
             self.canvas.create_image(147,150,image = self.img_file)

    def image_sb(self):
        #画像ファイルを指定する
             self.img_file = tk.PhotoImage(file = "assets/sb.png")
             
             #画像ファイルをキャンバスの(0,0)に合わせて表示してみる
             self.canvas.create_image(148,148,image = self.img_file)
        
root = tk.Tk()
root.title("Pokerハンド強弱アプリ")
root.geometry('400x480')
app = Application(root=root)
app.mainloop()

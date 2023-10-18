import tkinter as tk

#継承
class Application(tk.Frame):
    def __init__(self, root=None):
        #オーバーライド
        super().__init__(root, width=380, height=280,
                         bd=1, relief='groove')
        self.root = root
        self.pack()
        self.pack_propagate(0)
        self.create_widgets()

#widgetの作成    
    def create_widgets(self):
        # 決定ボタン
        decide_btn = tk.Button(self,text="選択",command=self.submit)
        decide_btn.pack(side='bottom')
        
        #label
        label=tk.Label(self,text='ポーカーの手札の強弱が分かります',width=200)
        label.pack(side="top")

        #radiobutton
        self.selected_radio = tk.StringVar()

        #プレイング人数が少ないほうが勝率は高い
        #最初は一番で,その後も順番が速いので不利。UTG：かなり強いハンドで参加。多人数参戦してきた時に備える。
        radio_1 =tk.Radiobutton(self,text="UTG",value="UTG",
                                variable=self.selected_radio)
        
        #最後から二番目にアクションを選択できますが、プロップ以降は最初にアクションを決定するポジション。SB　：そこそこのハンドでも参加。状況見て参加を決める。
        radio_2 =tk.Radiobutton(self,text="SB",value="SB",
                                variable=self.selected_radio)
        
        #最初は1番最後だが、それ以降は二番手。BB:ポジションでは優位な反面、どんなに弱いハンドでも参加費を強制的に払うリスク
        radio_3 =tk.Radiobutton(self,text="BB",value="BB",
                                variable=self.selected_radio)
        
        #最も有利。最初は後ろから三番手。後は一番後ろ。攻めることを意識。
        radio_4 =tk.Radiobutton(self,text="BTN",value="BTN",
                                variable=self.selected_radio)
        
        radio_1.pack()
        radio_2.pack()
        radio_3.pack()
        radio_4.pack()


    def submit(self):
        print("ボタンが押された") 
        print(self.selected_radio.get()) 

        
root = tk.Tk()
root.title("Pokerハンド強弱アプリ")
root.geometry('400x300')
app = Application(root=root)
app.mainloop()

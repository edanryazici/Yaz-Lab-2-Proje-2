import wx
class CustomButton(wx.Button):
    def __init__(self, parent, label, background_color):
        super().__init__(parent, label=label)

        # Özelleştirilmiş stil özellikleri
        self.default_background_color = background_color
        self.default_border_style = wx.BORDER_DOUBLE
        self.default_font = wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)

        self.SetBackgroundColour(self.default_background_color)
        self.SetForegroundColour(wx.WHITE)
        self.SetWindowStyleFlag(self.default_border_style)
        self.SetOwnFont(self.default_font)

        # Event bağlantıları
        self.Bind(wx.EVT_ENTER_WINDOW, self.on_mouse_enter)
        self.Bind(wx.EVT_LEAVE_WINDOW, self.on_mouse_leave)

    def on_mouse_enter(self, event):
        self.SetWindowStyleFlag(wx.BORDER_SIMPLE)
        self.SetBackgroundColour(self.default_background_color)
        self.SetForegroundColour(wx.BLACK)
        self.Refresh()

    def on_mouse_leave(self, event):
        self.SetWindowStyleFlag(self.default_border_style)
        self.SetBackgroundColour(self.default_background_color)
        self.SetForegroundColour(wx.WHITE)
        self.Refresh()

class CustomDropdown(wx.ComboCtrl):
    def __init__(self, parent, choices):
        super().__init__(parent, style=wx.CB_READONLY)

        self.SetPopupMaxHeight(200)  # Açılır menü maksimum yüksekliğini ayarla
        self.SetTextCtrlStyle(wx.TE_PROCESS_ENTER)  # Metin kontrolü stilini ayarla

        self.choices = choices
        self.update_dropdown()

        self.Bind(wx.EVT_COMBOBOX, self.on_combobox)
        self.SetButtonBitmaps(wx.NullBitmap)  # Standart düğme görüntüsünü kaldır
        self.SetCustomPaintWidth(200)  # Özel boyama genişliğini ayarla

        self.Bind(wx.EVT_PAINT, self.on_paint)


    def update_dropdown(self):
      self.SetValue(self.choices[0])  # Varsayılan değeri ayarla
        menu = wx.Menu()
        for choice in self.choices:
            item = menu.Append(wx.ID_ANY, choice)
            self.Bind(wx.EVT_MENU, self.on_menu_item, item)

        self.SetMenu(menu)

    def on_menu_item(self, event):
        selected_item = self.choices[event.GetId()]
        self.SetValue(selected_item)
        print("Selected item:", selected_item)

    def on_combobox(self, event):
        selected_item = self.GetValue()
        print("Selected item:", selected_item)

    def on_paint(self, event):
        dc = wx.BufferedPaintDC(self)
        rect = self.GetClientRect()
        dc.SetBackground(wx.WHITE_BRUSH)
        dc.Clear()

        # Seçili öğeyi çiz
        selected_item = self.GetValue()
        dc.SetTextForeground(wx.BLACK)
        dc.SetFont(self.GetFont())
        dc.DrawText(selected_item, rect.x + 5, rect.y + 5)

        # Aşağı oku çiz
        arrow_size = 10
        arrow_pen = wx.Pen(wx.BLACK, width=1)
        arrow_start = wx.Point(rect.width - arrow_size - 5, rect.height // 2)
        arrow_end = wx.Point(rect.width - 5, rect.height // 2)
        dc.DrawLine(arrow_start, arrow_end)
        dc.DrawLine(arrow_end, arrow_end + wx.Point(-arrow_size, arrow_size // 2))
        dc.DrawLine(arrow_end, arrow_end + wx.Point(-arrow_size, -arrow_size // 2))

class MainFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, title="Sıralama Projesi", size=(800, 600))

        self.panel = wx.Panel(self)

        # Sol Panel
        self.left_panel = wx.Panel(self.panel)
        # Boyut kaydırma çubuğu
        self.size_slider = wx.Slider(self.left_panel, value=50, minValue=1, maxValue=100, style=wx.SL_HORIZONTAL)
        self.size_value_label = wx.StaticText(self.left_panel, label="Boyut: 50")

        # Hız kaydırma çubuğu
        self.speed_slider = wx.Slider(self.left_panel, value=50, minValue=1, maxValue=100, style=wx.SL_HORIZONTAL)
        self.speed_value_label = wx.StaticText(self.left_panel, label="Hız: 50")

        # Sıralama algoritmaları
        self.algorithms = ["Seçme Sıralaması", "Kabarcık Sıralaması", "Ekleme Sıralaması", "Birleştirme Sıralaması",
                           "Hızlı Sıralama"]
        self.algorithm_radios = wx.RadioBox(self.left_panel, choices=self.algorithms, style=wx.RA_VERTICAL)

        # Grafik tipleri
        self.chart_types = ["Dağılım Grafiği", "Sütun Grafiği", "Kök Grafiği"]
        self.chart_dropdown = CustomDropdown(self.left_panel, choices=self.chart_types)


        # Butonlar
        self.create_button = CustomButton(self.left_panel, label="Oluştur", background_color=(0, 180, 216))
        self.start_button = CustomButton(self.left_panel, label="Başla", background_color=(112, 224, 0))
        self.pause_button = CustomButton(self.left_panel, label="Dur", background_color=(255, 183, 3))
        self.reset_button = CustomButton(self.left_panel, label="Sıfırla", background_color=(239, 35, 60))

        # Butonları Sırala
        self.left_panel_sizer = wx.BoxSizer(wx.VERTICAL)
        self.left_panel_sizer.Add(self.create_button, flag=wx.EXPAND | wx.ALL, border=10)
        self.left_panel_sizer.Add(self.start_button, flag=wx.EXPAND | wx.ALL, border=10)
        self.left_panel_sizer.Add(self.pause_button, flag=wx.EXPAND | wx.ALL, border=10)
        self.left_panel_sizer.Add(self.reset_button, flag=wx.EXPAND | wx.ALL, border=10)

        self.left_panel.SetSizer(self.left_panel_sizer)

        # Ana Panel
        self.main_panel = wx.Panel(self.panel)
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)

        self.panel_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.panel_sizer.Add(self.left_panel, proportion=1, flag=wx.EXPAND)
        self.panel_sizer.Add(self.main_panel, proportion=3, flag=wx.EXPAND)
        self.panel.SetSizer(self.panel_sizer)

        self.left_panel_sizer = wx.BoxSizer(wx.VERTICAL)
        self.left_panel.SetSizer(self.left_panel_sizer)

        self.left_panel_sizer.Add(self.size_value_label, flag=wx.EXPAND | wx.ALL, border=10)
        self.left_panel_sizer.Add(self.size_slider, flag=wx.EXPAND | wx.ALL, border=10)

        self.left_panel_sizer.Add(self.speed_value_label, flag=wx.EXPAND | wx.ALL, border=10)
        self.left_panel_sizer.Add(self.speed_slider, flag=wx.EXPAND | wx.ALL, border=10)

        self.left_panel_sizer.Add(wx.StaticText(self.left_panel, label="Sıralama Algoritması:"), flag=wx.ALL, border=10)
        self.left_panel_sizer.Add(self.algorithm_radios, flag=wx.ALL, border=10)

        self.left_panel_sizer.Add(wx.StaticText(self.left_panel, label="Grafik Tipi:"), flag=wx.ALL, border=10)
        self.left_panel_sizer.Add(self.chart_dropdown, flag=wx.ALL, border=10)

        self.left_panel_sizer.Add(self.create_button, flag=wx.EXPAND | wx.ALL, border=10)
        self.left_panel_sizer.Add(self.start_button, flag=wx.EXPAND | wx.ALL, border=10)
        self.left_panel_sizer.Add(self.pause_button, flag=wx.EXPAND | wx.ALL, border=10)
        self.left_panel_sizer.Add(self.reset_button, flag=wx.EXPAND | wx.ALL, border=10)

        self.main_sizer.Add(self.panel, proportion=1, flag=wx.EXPAND)
        self.SetSizerAndFit(self.main_sizer)
        self.Center()

        # Event bağlantıları
        self.size_slider.Bind(wx.EVT_SCROLL, self.on_size_slider_scroll)
        self.speed_slider.Bind(wx.EVT_SCROLL, self.on_speed_slider_scroll)

    def on_size_slider_scroll(self, event):
        value = self.size_slider.GetValue()
        self.size_value_label.SetLabel("Boyut: " + str(value))

    def on_speed_slider_scroll(self, event):
        value = self.speed_slider.GetValue()
        self.speed_value_label.SetLabel("Hız: " + str(value))


if __name__ == "__main__":
    app = wx.App()
    frame = MainFrame(None)
    frame.Show()
    app.MainLoop()

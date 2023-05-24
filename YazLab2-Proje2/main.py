import wx

class CustomDropdown(wx.Choice):
    def __init__(self, parent, choices):
        super().__init__(parent, choices=choices)

        # Event bağlantısı
        self.Bind(wx.EVT_ENTER_WINDOW, self.on_mouse_enter)
        self.Bind(wx.EVT_LEAVE_WINDOW, self.on_mouse_leave)

    def on_mouse_enter(self, event):
        self.SetBackgroundColour(wx.Colour(192, 192, 192))
        self.Refresh()

    def on_mouse_leave(self, event):
        self.SetBackgroundColour(wx.WHITE)
        self.Refresh()


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

        # Sıralama türü açılır penceresi
        self.sort_type_label = wx.StaticText(self.left_panel, label="Sıralama Türü:")
        self.sort_type_choices = ["Dağılım Grafiği", "Sütun Grafiği", "Kök Grafiği"]
        self.sort_type_dropdown = CustomDropdown(self.left_panel, choices=self.sort_type_choices)

        # Butonlar
        self.create_button = CustomButton(self.left_panel, label="Oluştur", background_color=(46, 204, 113))
        self.start_button = CustomButton(self.left_panel, label="Başlat", background_color=(52, 152, 219))
        self.pause_button = CustomButton(self.left_panel, label="Durdur", background_color=(255, 183, 0))
        self.reset_button = CustomButton(self.left_panel, label="Sıfırla", background_color=(239, 35, 60))

        # Sol Panel Sıralama
        self.left_sizer = wx.BoxSizer(wx.VERTICAL)
        self.left_sizer.Add(self.size_slider, 0, wx.EXPAND | wx.ALL, 10)
        self.left_sizer.Add(self.size_value_label, 0, wx.ALIGN_CENTER_HORIZONTAL)
        self.left_sizer.Add(self.speed_slider, 0, wx.EXPAND | wx.ALL, 10)
        self.left_sizer.Add(self.speed_value_label, 0, wx.ALIGN_CENTER_HORIZONTAL)
        self.left_sizer.Add(self.sort_type_label, 0, wx.TOP | wx.LEFT, 10)
        self.left_sizer.Add(self.algorithm_radios, 0, wx.EXPAND | wx.ALL, 10)
        self.left_sizer.Add(self.sort_type_dropdown, 0, wx.EXPAND | wx.ALL, 10)
        self.left_sizer.Add(self.create_button, 0, wx.EXPAND | wx.ALL, 10)
        self.left_sizer.Add(self.start_button, 0, wx.EXPAND | wx.ALL, 10)
        self.left_sizer.Add(self.pause_button, 0, wx.EXPAND | wx.ALL, 10)
        self.left_sizer.Add(self.reset_button, 0, wx.EXPAND | wx.ALL, 10)
        self.left_panel.SetSizer(self.left_sizer)

        # Sağ Panel
        self.right_panel = wx.Panel(self.panel)
        self.right_sizer = wx.BoxSizer(wx.VERTICAL)
        self.right_panel.SetSizer(self.right_sizer)

        # Ana Panel
        self.main_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.main_sizer.Add(self.left_panel, 0, wx.EXPAND)
        self.main_sizer.Add(self.right_panel, 1, wx.EXPAND)
        self.panel.SetSizer(self.main_sizer)

        # Pencere ayarları
        self.panel.Layout()
        self.Show()

        # Event bağlantıları
        self.size_slider.Bind(wx.EVT_SCROLL, self.on_size_slider_scroll)
        self.speed_slider.Bind(wx.EVT_SCROLL, self.on_speed_slider_scroll)

    def on_size_slider_scroll(self, event):
        value = self.size_slider.GetValue()
        self.size_value_label.SetLabel("Boyut: " + str(value))

    def on_speed_slider_scroll(self, event):
        value = self.speed_slider.GetValue()
        self.speed_value_label.SetLabel("Hız: " + str(value))


app = wx.App()
frame = MainFrame(None)
frame.Show()
app.MainLoop()

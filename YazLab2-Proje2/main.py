import wx
import wx.lib.agw.flatnotebook as fnb

class CustomSlider(wx.Slider):
    def __init__(self, parent, id=wx.ID_ANY, value=0, minValue=0, maxValue=100,
                 pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.SL_HORIZONTAL,
                 validator=wx.DefaultValidator, name=wx.SliderNameStr):
        super().__init__(parent, id, value, minValue, maxValue, pos, size, style, validator, name)

        self.SetWindowStyle(wx.SL_AUTOTICKS | wx.SL_LABELS | wx.SL_TOP)
        self.SetThumbLength(20)
        self.SetPageSize(1)

        self.Bind(wx.EVT_SCROLL, self.OnScroll)
        self.Bind(wx.EVT_ENTER_WINDOW, self.OnMouseEnter)
        self.Bind(wx.EVT_LEAVE_WINDOW, self.OnMouseLeave)

    def _get_thumb_position(self):
        if self.GetWindowStyleFlag() & wx.SL_HORIZONTAL:
            slider_range = self.GetSize().GetWidth() - self.GetThumbLength()
            slider_position = (slider_range * self.GetValue()) / (self.GetMax() - self.GetMin())
        else:
            slider_range = self.GetSize().GetHeight() - self.GetThumbLength()
            slider_position = (slider_range * (self.GetMax() - self.GetValue())) / (self.GetMax() - self.GetMin())
        return slider_position

    def OnScroll(self, event):
        self.Refresh()
        event.Skip()

    def OnMouseEnter(self, event):
        self.Refresh()
        event.Skip()

    def OnMouseLeave(self, event):
        self.Refresh()
        event.Skip()

    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        thumb_pos = self._get_thumb_position()
        thumb_size = self.GetThumbLength()
        thumb_radius = thumb_size // 2

        if self.GetWindowStyleFlag() & wx.SL_HORIZONTAL:
            thumb_rect = wx.Rect(thumb_pos, (self.GetSize().GetHeight() - thumb_size) // 2, thumb_size, thumb_size)
        else:
            thumb_rect = wx.Rect((self.GetSize().GetWidth() - thumb_size) // 2, thumb_pos, thumb_size, thumb_size)

        dc.SetPen(wx.TRANSPARENT_PEN)
        dc.SetBrush(wx.Brush(wx.Colour(192, 192, 192)))
        dc.DrawEllipseRect(thumb_rect)

    def OnSize(self, event):
        self.Refresh()
        event.Skip()

class CustomDropdown(wx.Choice):
    def __init__(self, parent, choices):
        super().__init__(parent, choices=choices)

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

        self.default_background_color = background_color
        self.default_border_style = wx.BORDER_DOUBLE
        self.default_font = wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)

        self.SetBackgroundColour(self.default_background_color)
        self.SetForegroundColour(wx.WHITE)
        self.SetWindowStyleFlag(self.default_border_style)
        self.SetOwnFont(self.default_font)

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
        self.size_slider = CustomSlider(self.left_panel, value=50, minValue=1, maxValue=100, style=wx.SL_HORIZONTAL)
        self.size_value_label = wx.StaticText(self.left_panel, label="Boyut: 50")

        # Hız kaydırma çubuğu
        self.speed_slider = CustomSlider(self.left_panel, value=50, minValue=1, maxValue=100, style=wx.SL_HORIZONTAL)
        self.speed_value_label = wx.StaticText(self.left_panel, label="Hız: 50")

        # Sıralama algoritmaları
        self.algorithms = ["Seçme Sıralaması", "Kabarcık Sıralaması", "Ekleme Sıralaması", "Birleştirme Sıralaması",
                           "Hızlı Sıralama"]
        self.algorithm_radios = wx.RadioBox(self.left_panel, choices=self.algorithms, style=wx.RA_VERTICAL)

        # Sıralama türü açılır menüsü
        self.sort_type_label = wx.StaticText(self.left_panel, label="Sıralama Türü:")
        self.sort_type_choices = ["Dağılım Grafiği", "Sütun Grafiği", "Kök Grafiği"]
        self.sort_type_dropdown = CustomDropdown(self.left_panel, choices=self.sort_type_choices)

        # Butonlar
        self.create_button = CustomButton(self.left_panel, label="Oluştur", background_color=(46, 204, 113))
        self.start_button = CustomButton(self.left_panel, label="Başlat", background_color=(52, 152, 219))
        self.pause_button = CustomButton(self.left_panel, label="Durdur", background_color=(255, 170, 0))
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
        self.right_notebook = fnb.FlatNotebook(self.right_panel)

        # Sağ Panel Sıralama
        self.right_sizer = wx.BoxSizer(wx.VERTICAL)
        self.right_sizer.Add(self.right_notebook, 1, wx.EXPAND)
        self.right_panel.SetSizer(self.right_sizer)

        # Ana Sıralama Paneli
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer.Add(self.left_panel, 0, wx.EXPAND)
        self.sizer.Add(self.right_panel, 1, wx.EXPAND)
        self.panel.SetSizer(self.sizer)

        self.Layout()
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

 

if __name__ == '__main__':
    app = wx.App()
    frame = MainFrame(None)
    app.MainLoop()

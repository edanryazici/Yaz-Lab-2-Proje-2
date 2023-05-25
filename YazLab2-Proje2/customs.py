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
        self.default_font = wx.Font(10, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_MAX, wx.FONTWEIGHT_MEDIUM)

        self.SetBackgroundColour(self.default_background_color)
        self.SetForegroundColour((233, 236, 239))
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
        self.SetForegroundColour((233, 236, 239))
        self.Refresh()

import wx
import wx.lib.agw.flatnotebook as fnb
from customs import CustomSlider, CustomDropdown, CustomButton
from algorithms import selection_sort, merge_sort, quick_sort, bubble_sortt, insertion_sort


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
        self.sort_type_label = wx.StaticText(self.left_panel, label="Grafik Türü:")
        self.sort_type_choices = ["Dağılım Grafiği", "Sütun Grafiği", "Kök Grafiği"]
        self.sort_type_dropdown = CustomDropdown(self.left_panel, choices=self.sort_type_choices)

        # Butonlar
        self.create_button = CustomButton(self.left_panel, label="Oluştur", background_color=(46, 204, 113))
        self.start_button = CustomButton(self.left_panel, label="Başlat", background_color=(52, 152, 219))
        self.pause_button = CustomButton(self.left_panel, label="Durdur/ Devam Et", background_color=(255, 170, 0))
        self.reset_button = CustomButton(self.left_panel, label="Sıfırla", background_color=(239, 35, 60))

        # Karşılaştırma sayısı ve analiz sonucunu tutacak değişkenler
        self.comparison_count = 0
        self.analysis_result = ""

        # Karşılaştırma sayısını gösteren etiket
        self.comparison_label = wx.StaticText(self.left_panel, label="Karşılaştırma Sayısı: 0")

        # Analiz sonucunu gösteren etiket
        self.analysis_label = wx.StaticText(self.left_panel, label="")

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
        self.left_sizer.Add(self.comparison_label, 0, wx.ALIGN_CENTER_HORIZONTAL)
        self.left_sizer.Add(self.analysis_label, 0, wx.ALIGN_CENTER_HORIZONTAL)

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

    def update_comparison_count(self):
        self.comparison_label.SetLabel("Karşılaştırma Sayısı: " + str(self.comparison_count))

    def update_analysis_result(self):
        self.analysis_label.SetLabel(self.analysis_result)

    def show_analysis_result(self):
        # Sıralama işlemi tamamlandığında karşılaştırma sayısı ve analiz sonucunu ekrana yazdır
        self.update_comparison_count()
        self.update_analysis_result()

        # Analiz sonuçlarını güncelledikten sonra paneli yenile
        self.panel.Layout()


if __name__ == '__main__':
    app = wx.App()
    frame = MainFrame(None)
    app.MainLoop()

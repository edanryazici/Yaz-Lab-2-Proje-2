import wx
import wx.lib.agw.flatnotebook as fnb
from matplotlib.backend_bases import NavigationToolbar2
from matplotlib_inline.backend_inline import FigureCanvas
import matplotlib.pyplot as plt
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
import wx

from customs import CustomSlider, CustomDropdown, CustomButton
from algorithms import selection_sort, merge_sort, quick_sort, bubble_sortt, insertion_sort
from grafics import create_scatter_chart, create_bar_chart, create_sqrt_chart
import matplotlib.pyplot as plt
import random

class MainFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, title="Sıralama Projesi", size=(700, 700))
        self.visualization_canvas = None
        self.toolbar = None

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
        self.algorithms_options_label = wx.StaticText(self.left_panel, label="Algoritma Seçenekleri")
        self.algorithms = ["Seçme Sıralaması", "Kabarcık Sıralaması", "Ekleme Sıralaması", "Birleştirme Sıralaması",
                           "Hızlı Sıralama"]
        self.algorithm_radios = wx.RadioBox(self.left_panel, choices=self.algorithms, style=wx.RA_VERTICAL)

        # Grafik türü açılır menüsü
        self.sort_type_label = wx.StaticText(self.left_panel, label="Grafik Türü:")
        self.sort_type_choices = ["Dağılım Grafiği", "Sütun Grafiği", "Kök Grafiği"]
        self.sort_type_dropdown = CustomDropdown(self.left_panel, choices=self.sort_type_choices)

        # Butonlar
        self.create_button = CustomButton(self.left_panel, label="Oluştur", background_color=(56, 102, 65))
        self.start_button = CustomButton(self.left_panel, label="Başlat", background_color=(2, 62, 138))
        self.pause_button = CustomButton(self.left_panel, label="Durdur/ Devam Et", background_color=(255, 123, 0))
        self.reset_button = CustomButton(self.left_panel, label="Sıfırla", background_color=(157, 2, 8))


        # Karşılaştırma sayısı ve analiz sonucunu tutacak değişkenler
        self.comparison_count = 0
        self.analysis_result = ""

        # Karşılaştırma sayısını gösteren etiket
        self.comparison_label = wx.StaticText(self.left_panel, label="Karşılaştırma Sayısı: 0")

        # Analiz sonucunu gösteren etiket
        self.analysis_label = wx.StaticText(self.left_panel, label="")

        # Sol Panel Sıralama
        self.left_sizer = wx.BoxSizer(wx.VERTICAL)
        self.left_sizer.AddSpacer(20)  # 20 piksel boşluk ekle
        self.left_sizer.Add(self.size_slider, 0, wx.EXPAND | wx.ALL, 10)
        self.left_sizer.Add(self.size_value_label, 0, wx.ALIGN_CENTER_HORIZONTAL)
        self.left_sizer.Add(self.speed_slider, 0, wx.EXPAND | wx.ALL, 10)
        self.left_sizer.Add(self.speed_value_label, 0, wx.ALIGN_CENTER_HORIZONTAL)
        self.left_sizer.AddSpacer(20)  # 20 piksel boşluk ekle
        self.left_sizer.Add(self.algorithms_options_label, 0, wx.TOP | wx.LEFT, 10)
        self.left_sizer.Add(self.algorithm_radios, 0, wx.EXPAND | wx.ALL, 10)
        self.left_sizer.Add(self.sort_type_label, 0, wx.TOP | wx.LEFT, 10)
        self.left_sizer.Add(self.sort_type_dropdown, 0, wx.EXPAND | wx.ALL, 10)
        self.left_sizer.Add(self.create_button, 0, wx.EXPAND | wx.ALL, 10)
        self.left_sizer.Add(self.start_button, 0, wx.EXPAND | wx.ALL, 10)
        self.left_sizer.Add(self.pause_button, 0, wx.EXPAND | wx.ALL, 10)
        self.left_sizer.Add(self.reset_button, 0, wx.EXPAND | wx.ALL, 10)
        self.left_sizer.AddSpacer(20)  # 20 piksel boşluk ekle
        self.left_sizer.Add(self.comparison_label, 0, wx.TOP | wx.LEFT, 10)
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
        self.left_sizer.AddSpacer(20)  # 20 piksel boşluk ekle
        self.sizer.Add(self.left_panel, 0, wx.EXPAND)
        self.sizer.Add(self.right_panel, 1, wx.EXPAND)
        self.panel.SetSizer(self.sizer)

        self.Layout()
        self.Show()
        # Event bağlantıları
        self.size_slider.Bind(wx.EVT_SCROLL, self.on_size_slider_scroll)
        self.speed_slider.Bind(wx.EVT_SCROLL, self.on_speed_slider_scroll)
        self.reset_button.Bind(wx.EVT_BUTTON, self.on_reset_button_click)
        self.create_button.Bind(wx.EVT_BUTTON, self.on_create_button)
        self.start_button.Bind(wx.EVT_BUTTON, self.on_start_button)

        self.visualization_fig = None

    def on_reset_button_click(self, event):
        # Boyutu sıfırla
        self.size_slider.SetValue(50)
        self.size_value_label.SetLabel("Boyut: 50")

        # Hızı sıfırla
        self.speed_slider.SetValue(50)
        self.speed_value_label.SetLabel("Hız: 50")

        # Radyo düğmesini sıfırla
        self.algorithm_radios.SetSelection(0)

        # Açılır menüyü sıfırla
        self.sort_type_dropdown.SetSelection(-1)

        # Karşılaştırma sayısı ve analiz sonucunu sıfırla
        self.comparison_count = 0
        self.analysis_result = ""
        self.update_comparison_count()
        self.update_analysis_result()

        # Görselleştirmeyi sıfırla
        self.reset_visualization()

    def on_size_slider_scroll(self, event):
        value = self.size_slider.GetValue()
        self.size_value_label.SetLabel("Boyut: " + str(value))

    def on_speed_slider_scroll(self, event):
        value = self.speed_slider.GetValue()
        self.speed_value_label.SetLabel("Hız: " + str(value))

    def on_create_button(self, event):
        # Sıralama için veri kümesini oluştur
        size = self.size_slider.GetValue()
        data = list(range(1, size + 1))
        random.shuffle(data)

        # Görselleştirmeyi sıfırla ve yeniden oluştur
        self.reset_visualization()
        self.create_visualization(data)

    def on_start_button(self, event):
        # Sıralama işlemini başlat
        algorithm_index = self.algorithm_radios.GetSelection()
        sort_algorithm = None

        if algorithm_index == 0:
            sort_algorithm = selection_sort
        elif algorithm_index == 1:
            sort_algorithm = bubble_sortt
        elif algorithm_index == 2:
            sort_algorithm = insertion_sort
        elif algorithm_index == 3:
            sort_algorithm = merge_sort
        elif algorithm_index == 4:
            sort_algorithm = quick_sort

        if sort_algorithm is not None:
            data = self.get_visualization_data()
            self.start_sorting(sort_algorithm, data)

    def create_visualization(self, data):
        # Önceki grafik nesnesini temizle
        if self.visualization_canvas:
            self.visualization_canvas.Destroy()
        # Görselleştirme figürünü oluştur
        if self.sort_type_dropdown.GetSelection() == 0:
            fig = plt.figure()
            self.visualization_canvas = FigureCanvas(self.right_panel, -1, fig)

            self.right_sizer.Insert(0, self.visualization_canvas, 1, wx.EXPAND)

            self.visualization_canvas.figure.add_subplot(111).bar(range(len(data)), data)
            self.visualization_canvas.figure.suptitle("Dağılım Grafiği")
            self.visualization_canvas.draw()

        elif self.sort_type_dropdown.GetSelection() == 1:
            fig = plt.figure()
            self.visualization_canvas = FigureCanvas(self.right_panel, -1, fig)

            self.right_sizer.Insert(0, self.visualization_canvas, 1, wx.EXPAND)

            self.visualization_canvas.figure.add_subplot(111).bar(range(len(data)), data)
            self.visualization_canvas.figure.suptitle("Sütun Grafiği")
            self.visualization_canvas.draw()

        elif self.sort_type_dropdown.GetSelection() == 2:
            fig = plt.figure()
            self.visualization_canvas = FigureCanvas(self.right_panel, -1, fig)

            self.right_sizer.Insert(0, self.visualization_canvas, 1, wx.EXPAND)

            self.visualization_canvas.figure.add_subplot(111).plot(range(len(data)), data)
            self.visualization_canvas.figure.suptitle("Kök Grafiği")
            self.visualization_canvas.draw()

        

    def reset_visualization(self):
        # Görselleştirme figürünü sıfırla
        if self.visualization_fig is not None:
            self.visualization_fig.clear()
            self.visualization_canvas.draw()
            self.right_sizer.Remove(0)  # Toolbar'ı kaldır
            self.right_sizer.Remove(0)  # Canvas'ı kaldır
            self.visualization_fig = None
            self.visualization_canvas = None
            self.toolbar = None

    def get_visualization_data(self):
        # Görselleştirme verisini al
        if self.visualization_fig is not None:
            if self.sort_type_dropdown.GetSelection() == 0:
                # Dağılım grafiği için veriyi al
                bars = self.visualization_fig.axes[0].patches
                data = [bar.get_height() for bar in bars]
                return data
            elif self.sort_type_dropdown.GetSelection() == 1:
                # Sütun grafiği için veriyi al
                bars = self.visualization_fig.axes[0].patches
                data = [bar.get_height() for bar in bars]
                return data
            elif self.sort_type_dropdown.GetSelection() == 2:
                # Kök grafiği için veriyi al
                lines = self.visualization_fig.axes[0].lines
                data = [line.get_ydata()[0] for line in lines]
                return data

        return []

    def update_visualization(self, data):
        # Görselleştirmeyi güncelle
        if self.visualization_fig is not None:
            if self.sort_type_dropdown.GetSelection() == 0:
                # Dağılım grafiğini güncelle
                bars = self.visualization_fig.axes[0].patches
                for bar, height in zip(bars, data):
                    bar.set_height(height)
                self.visualization_fig.canvas.draw()
            elif self.sort_type_dropdown.GetSelection() == 1:
                # Sütun grafiğini güncelle
                bars = self.visualization_fig.axes[0].patches
                for bar, height in zip(bars, data):
                    bar.set_height(height)
                self.visualization_fig.canvas.draw()
            elif self.sort_type_dropdown.GetSelection() == 2:
                # Kök grafiğini güncelle
                lines = self.visualization_fig.axes[0].lines
                for line, y in zip(lines, data):
                    line.set_ydata([y, y])
                self.visualization_fig.canvas.draw()

    def update_comparison_count(self):
        # Karşılaştırma sayısını güncelle
        self.comparison_label.SetLabel("Karşılaştırma Sayısı: " + str(self.comparison_count))

    def update_analysis_result(self):
        # Analiz sonucunu güncelle
        self.analysis_label.SetLabel(self.analysis_result)

    def start_sorting(self, sort_algorithm, data):
        # Sıralama işlemini başlat ve görselleştirmeyi güncelle
        self.comparison_count = 0
        self.update_comparison_count()

        if sort_algorithm is not None:
            # Sıralama işlemini başlat
            sorted_data, comparisons = sort_algorithm(data)
            self.comparison_count = comparisons
            self.update_comparison_count()

            if sorted_data == sorted(data):
                self.analysis_result = "Sıralama başarıyla tamamlandı."
            else:
                self.analysis_result = "Sıralama işlemi başarısız."

            self.update_analysis_result()
            self.update_visualization(sorted_data)

        else:
            self.analysis_result = "Lütfen bir sıralama algoritması seçin."
            self.update_analysis_result()

app = wx.App()
frame = MainFrame(None)
app.MainLoop()

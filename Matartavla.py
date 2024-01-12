import tkinter as tk
import math
import time



class Gauge(tk.Frame):
    def __init__(self, master=None, title="", unit="", max_value=100, min_value=0):
        super().__init__(master)
        self.title = title
        self.unit = unit
        self.max_value = max_value
        self.min_value = min_value
        self.current_value = min_value
        self.direction = 1  # 1 for increasing, -1 for decreasing

        self.create_widgets()

    def create_widgets(self):
        self.label_title = tk.Label(self, text=self.title)
        self.label_title.pack()

        self.canvas = tk.Canvas(self, width=210, height=100)
        self.canvas.pack()

        self.label_unit = tk.Label(self, text=self.unit)
        self.label_unit.pack()

        self.update_gauge()

    def update_gauge(self):
        self.canvas.delete("all")

        # Draw gauge outline
        self.canvas.create_arc(15, 15, 195, 190, start=0, extent=180, style=tk.ARC, outline="grey32", width=25)

        # Draw white gauge value
        value_angle = -180 * ((self.current_value - self.min_value) / (self.max_value - self.min_value))
        self.canvas.create_arc(15, 15, 195, 190, start=180, extent=value_angle, style=tk.ARC, outline="white", width=25)
        
        # Draw red small end of gauge value
        value_angle = -180 * ((self.current_value - self.min_value) / (self.max_value - self.min_value))
        self.canvas.create_arc(15, 15, 195, 190, start=176 +value_angle, extent= 4, style=tk.ARC, outline="red", width=25)


    def set_value(self, value):
        self.current_value = value
        self.update_gauge()

    def update_value(self):
        if self.direction == 1:
            self.current_value += 1
            if self.current_value >= self.max_value:
                self.direction = -1
        else:
            self.current_value -= 1
            if self.current_value <= self.min_value:
                self.direction = 1

        self.update_gauge()


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Gauge App")

        self.temperature_gauge = Gauge(self, title="Temperature", unit="°C", max_value=100, min_value=0)
        self.temperature_gauge.pack(pady=10)

        self.rpm_gauge = Gauge(self, title="RPM", unit="RPM", max_value=8000, min_value=0)
        self.rpm_gauge.pack(pady=10)

        self.update_gauges()

    def update_gauges(self):
        while True:
            self.temperature_gauge.update_value()
            self.rpm_gauge.update_value()
            self.update()
            time.sleep(0.05)


if __name__ == "__main__":
    app = App()
    app.mainloop()

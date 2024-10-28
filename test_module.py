import unittest
import medical_data_visualizer
import matplotlib as mpl


class CatPlotTestCase(unittest.TestCase):
    def setUp(self):
        self.fig = medical_data_visualizer.draw_cat_plot()  # Assuming this returns an Axes object directly
        if isinstance(self.fig, tuple):  # Check if it returns a tuple
            self.ax = self.fig[0]  # Extract the axes from the tuple
        else:
            self.ax = self.fig  # Directly use it if it's already an Axes object

    def test_line_plot_labels(self):
        actual = self.ax.get_xlabel()  # Get x-axis label
        expected = "variable"
        self.assertEqual(actual, expected, "Expected line plot xlabel to be 'variable'")
        actual = self.ax.get_ylabel()  # Get y-axis label
        expected = "total"
        self.assertEqual(actual, expected, "Expected line plot ylabel to be 'total'")
        
        # Get x-axis tick labels
        actual = [label.get_text() for label in self.ax.get_xticklabels()]
        expected = ['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke']
        self.assertEqual(actual, expected, "Expected bar plot secondary x labels to be 'active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'")

    def test_bar_plot_number_of_bars(self):
        # Check for rectangles directly in patches
        actual = len([rect for rect in self.ax.get_children() if isinstance(rect, mpl.patches.Rectangle)])
        expected = 13
        self.assertEqual(actual, expected, "Expected a different number of bars in the chart.")


class HeatMapTestCase(unittest.TestCase):
    def setUp(self):
        self.fig = medical_data_visualizer.draw_heat_map()  # Assuming this returns an Axes object directly
        if isinstance(self.fig, tuple):  # Check if it returns a tuple
            self.ax = self.fig[0]  # Extract the axes from the tuple
        else:
            self.ax = self.fig  # Directly use it if it's already an Axes object

    def test_heat_map_labels(self):
        actual = [label.get_text() for label in self.ax.get_xticklabels()]
        expected = ['id', 'age', 'sex', 'height', 'weight', 'ap_hi', 'ap_lo', 'cholesterol', 'gluc', 'smoke', 'alco', 'active', 'cardio', 'overweight']
        self.assertEqual(actual, expected, "Expected heat map labels to be 'id', 'age', 'sex', 'height', 'weight', 'ap_hi', 'ap_lo', 'cholesterol', 'gluc', 'smoke', 'alco', 'active', 'cardio', 'overweight'.")

    def test_heat_map_values(self):
        actual = [text.get_text() for text in self.ax.texts]  # Get the text from the heatmap
        expected = ['0.0', '0.0', '-0.0', '0.0', '-0.1', '0.5', '0.0', '0.1', '0.1', '0.3', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.2', '0.1', '0.0', '0.2', '0.1', '0.0', '0.1', '-0.0', '-0.1', '0.1', '0.0', '0.2', '0.0', '0.1', '-0.0', '-0.0', '0.1', '0.0', '0.1', '0.4', '-0.0', '-0.0', '0.3', '0.2', '0.1', '-0.0', '0.0', '0.0', '-0.0', '-0.0', '-0.0', '0.2', '0.1', '0.1', '0.0', '0.0', '0.0', '0.0', '0.3', '0.0', '-0.0', '0.0', '-0.0', '-0.0', '-0.0', '0.0', '0.0', '-0.0', '0.0', '0.0', '0.0', '0.2', '0.0', '-0.0', '0.2', '0.1', '0.3', '0.2', '0.1', '-0.0', '-0.0', '-0.0', '-0.0', '0.1', '-0.1', '-0.1', '0.7', '0.0', '0.2', '0.1', '0.1', '-0.0', '0.0', '-0.0', '0.1']
        self.assertEqual(actual, expected, "Expected different values in heat map.")


if __name__ == "__main__":
    unittest.main()

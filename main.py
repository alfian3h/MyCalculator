# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import matplotlib.pyplot

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    data = (3, 6, 9, 12, 15)

    fig, simple_chart = matplotlib.pyplot.subplots()

    simple_chart.plot(data)

    matplotlib.pyplot.show()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

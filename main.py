
import epicycles
import fourier

z = epicycles.Epicycles.read_image_as_complex("Screenshot 2023-03-20 at 9.04.55 PM.png", num_indicies=4200, indices_step_size=4)
"""
        :param1 path of the image, make sure its B/W image with defined lines, see the example image 'bhenchod.png' and result ' bhenchod.gif'
        Very Important Read this, if you want to change any param
        Read image outline into complex numbers.  Uses random num_indicies locations to create outline of image
        :param num_indicies The number of random indicies to select from the image outline
        :param indicies_step_size The step size to use for excluding indicies.  Select higher value to reduce data size,
        DFT size, and computation time of epicycles, at the cost of drawing accuracy.
        :returns Image outline indices as complex numbers
"""
fourier_data = fourier.fft(z)

fourier_data.sort(key=lambda x: x.amplitude, reverse=True)
epicycles = epicycles.Epicycles(fourier_data, plot_size=[1024, 1024])
epicycles.run()
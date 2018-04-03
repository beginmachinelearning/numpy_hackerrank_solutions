import numpy as np
numpy_array = np.arange(1000000)
normal_list = list(range(1000000))

%time for looper in range(5): numpy_array = numpy_array * 2
%time for looper in range(5): normal_list = normal_list*2



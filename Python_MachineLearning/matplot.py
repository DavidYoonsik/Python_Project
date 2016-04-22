# from matplotlib.pyplot import legend, plot, title, show

from matplotlib.pyplot import plot, title, legend, show
from scipy import stats, polyval


x = [3.52, 2.58, 3.31, 4.07, 4.62, 3.98, 4.29, 4.83, 3.71, 4.61, 3.90, 3.20]
y = [2.48, 2.27, 2.47, 2.77, 2.98, 3.05, 3.18, 3.46, 3.03, 3.25, 2.67, 2.53]

slope, intercept, r_value, p_value, stderr = stats.linregress(x, y)

ry = polyval([slope, intercept], x)

print ry

plot(x, y, 'k.')

plot(x, ry, 'r.-')

title('Regression result')

legend(['original', 'regression'])

show()

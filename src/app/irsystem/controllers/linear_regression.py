import numpy as np

# get multiplier of projection to opening weekend
def get_projected_multiplier(data):
	x = np.array([22159, 14056, 1690, 1277,  198,  183, 129, 109, 73, 60, 60, 53, 18])
	y = np.array([1.097, 1.443, 1.15, 1.826, 1.068, 1-0.337, 1-0.057,1.051, 1.125,1-0.034,1.647,1.333,1.285])
	z = np.polyfit(x, y, 1)
	p = np.poly1d(z)
	return p(data)

# get multiplier of Rotten Tomatoes to full gross
def get_rt_multiplier(data):
	x = np.array([84, 96, 74, 95, 17, 23, 33, 30, 43, 51, 79, 14, 83])
	y = np.array([1-0.19, 1.736, 1.113, 2.014, 1.017, 1-0.287, 1-0.296,1 - 0.5, 1 - 0.031,1.016,2.388,1.386,1.056])
	z = np.polyfit(x, y, 1)
	p = np.poly1d(z)
	return p(data)

if __name__ == "__main__":
    print(get_projected_multiplier(1))
    print(get_rt_multiplier(10))
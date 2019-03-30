import numpy as np

# just for plotting
import matplotlib
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
import PyQt5
matplotlib.use('qt5agg')

def trans_png_eps(img_path):
	img_rgb = np.array(mpimg.imread(img_path), dtype=np.float32)
	fig = plt.figure() # figsize=(img_rgb.shape[0], img_rgb.shape[1])
	plt.imshow(img_rgb)
	plt.axis('off')
	# plt.show()
	plt.savefig(img_path.replace(".png", "_.png"), dpi=1000)


if __name__ == "__main__":
	img_path = "/home/luffyfjx/Documents/DLR/MasterThesis/Thesis_writing/LMT_Thesis_LaTeX/figures/bern_repa.png"
	trans_png_eps(img_path)
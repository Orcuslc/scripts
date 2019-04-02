import os, sys, re

path = "F:\\PG"

condition = {
	**dict.fromkeys(["Symphony", "Symphonien", "Symphonies", "Symphonie", "SYMPHONIE", "SYMPHONY"], "Sym."),
	'Concerto': "Con.",
	" by ": " - ",
	"Sonata": "Son."
}


for folder in os.listdir(path):
	local_path = os.path.join(path, folder)
	if os.path.isdir(local_path):
		for f in os.listdir(local_path):
			if os.path.isdir(os.path.join(local_path, f)):
				nf = f
				for k, v in condition.items():
					nf = nf.replace(k, v)
				os.rename(os.path.join(local_path, f), os.path.join(local_path, nf))

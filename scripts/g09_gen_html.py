import re
f = open('./doc/g09_prof_report.tex', 'r')
alltext = f.read()

fields = re.findall(r'(\\.*section{.*})|(\\par{.*})|(\\includegraphics.*{.*})', alltext)
fields = [(lambda p: p[0] if len(p[0]) else p[1] if len(p[1]) else p[2])(p) for p in fields]
for u, v in enumerate(fields):
	if re.search('Profiling', v):
		fields = fields[:u]
		break

pat_h1 = re.compile('\\\section{(.*)}')
pat_h2 = re.compile('\\\subsection{(.*)}')
pat_h3 = re.compile('\\\subsubsection{(.*)}')
pat_p = re.compile('\\\par{(.*)}')
pat_img = re.compile('\\\includegraphics\[.*\.([0-9]+)\]{g09_plot(.*)\.png}')
html = []
for s in fields:
	s = pat_h3.sub(r'<h3>\1</h3>', s)
	s = pat_h2.sub(r'<h2>\1</h2>', s)
	s = pat_h1.sub(r'<h1>\1</h1>', s)
	s = pat_p.sub(r'<p>\1</p>', s)
	s = pat_img.sub(r'<img src="../plots/g09_lab09_plot\2.png" height="\1%" />', s)
	s = re.sub(r'\\\\', '<br/>', s)
	s = re.sub('\\\\verb\+(.*)\+', r'<i>\1</i>', s)
	html.append(s)
g = open('./doc/g09_lab09_report.html', 'w+')
header = '<html><head><title>Timing report</title></head><body>'
end = '</body></html>'
print(header, file=g, end='\n')
for i in html:
	print(i, file=g, end='\n')
print(end, file=g, end='\n')

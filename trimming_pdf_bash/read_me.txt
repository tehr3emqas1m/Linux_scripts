pdftk doc.pdf cat 1-167 output doc1.pdf
qpdf --empty --pages doc1.pdf doc2.pdf -- doc.pdf
qpdf doc1.pdf --pages . 2-28 -- doc.pdf
img2pdf pic1.jpeg pic2.jpeg -o doc.pdf


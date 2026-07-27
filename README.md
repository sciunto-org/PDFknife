# PDFknife

A Swiss Army Knife sort of python scripts collection to manipulate PDFs. It relies on:

* pdfjam
* pdftk
* pdfunite (poppler)
* ghostscript
* mupdf-tools


# Install

The project is available on pypi: https://pypi.org/project/PDFknife/

    pip install PDFknife


# Tools

* `pdfknife-A5` -- Arrange two A5 pages side by side on A4 paper
* `pdfknife-clean` -- Recompress and clean a PDF with Ghostscript
* `pdfknife-cut` -- Cut margin marks and toolbox artefacts off a PDF
* `pdfknife-even` -- Extract only even pages from a PDF
* `pdfknife-extract` -- Extract embedded images and fonts from a PDF
* `pdfknife-margin` -- Add a white margin around PDF pages
* `pdfknife-merge` -- Merge several PDF files into one
* `pdfknife-recto` -- Arrange two A5 recto pages side by side on A4 (top-to-bottom)
* `pdfknife-reverse` -- Reverse page order of a PDF
* `pdfknife-rotate` -- Rotate all pages of a PDF by a given angle
* `pdfknife-shrink` -- Compress/reduce file size of PDFs with Ghostscript
* `pdfknife-split` -- Split a multi-page PDF into separate single-page PDFs
* `pdfknife-tearpages` -- Remove the first and/or last page of a PDF
* `pdfknife-trim` -- Trim (crop) edges of PDF pages

# License

BSD3, See LICENSE file.

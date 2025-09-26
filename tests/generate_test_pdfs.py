# tests/generate_test_pdfs.py

import random
from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def create_pdf(filename: Path, num_pages: int, title: str) -> None:
    """Generate a PDF with given number of pages and filler text."""
    c = canvas.Canvas(str(filename), pagesize=A4)
    _, height = A4
    for i in range(1, num_pages + 1):
        c.setFont("Helvetica", 14)
        c.drawString(100, height - 100, f"{title} - Page {i}")
        c.setFont("Helvetica", 10)
        for j in range(20):
            text = " ".join(
                random.choice(
                    [
                        "lorem",
                        "ipsum",
                        "dolor",
                        "sit",
                        "amet",
                        "consectetur",
                        "adipiscing",
                        "elit",
                        "random",
                        "text",
                        "content",
                    ]
                )
                for _ in range(10)
            )
            c.drawString(80, height - 150 - (j * 20), text)
        c.showPage()
    c.save()

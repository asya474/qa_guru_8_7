import os.path
from zipfile import ZipFile

from utils import PDF_RESOURCES_PATH, TXT_RESOURCES_PATH, XLS_RESOURCES_PATH, XLSX_RESOURCES_PATH


def test_archive_files(tmp_directory):
    pdf_size = os.path.getsize(PDF_RESOURCES_PATH)
    pdf_name = os.path.basename(PDF_RESOURCES_PATH)
    text_size = os.path.getsize(TXT_RESOURCES_PATH)
    text_name = os.path.basename(TXT_RESOURCES_PATH)
    xls_size = os.path.getsize(XLS_RESOURCES_PATH)
    xls_name = os.path.basename(XLS_RESOURCES_PATH)
    xlsx_size = os.path.getsize(XLSX_RESOURCES_PATH)
    xlsx_name = os.path.basename(XLSX_RESOURCES_PATH)

    with ZipFile(file="tmp/my_archive.zip", mode="a") as myzip:
        myzip.write(filename=PDF_RESOURCES_PATH, arcname='file_example.pdf', compress_type=None,
                    compresslevel=None)
        myzip.write(filename=TXT_RESOURCES_PATH, arcname='file_example.txt', compress_type=None,
                    compresslevel=None)
        myzip.write(filename=XLS_RESOURCES_PATH, arcname='file_example.xls', compress_type=None,
                    compresslevel=None)
        myzip.write(filename=XLSX_RESOURCES_PATH, arcname='file_example.xlsx', compress_type=None,
                    compresslevel=None)

    with ZipFile(file="tmp/my_archive.zip", mode="r") as myzip:
        pdf_archive_file = myzip.getinfo("file_example.pdf")
        pdf_archive_file_name = pdf_archive_file.filename
        pdf_archive_file_size = pdf_archive_file.file_size

        txt_archive_file = myzip.getinfo("file_example.txt")
        txt_archive_file_name = txt_archive_file.filename
        txt_archive_file_size = txt_archive_file.file_size

        xls_archive_file = myzip.getinfo("file_example.xls")
        xls_archive_file_name = xls_archive_file.filename
        xls_archive_file_size = xls_archive_file.file_size

        xlsx_archive_file = myzip.getinfo("file_example.xlsx")
        xlsx_archive_file_name = xlsx_archive_file.filename
        xlsx_archive_file_size = xlsx_archive_file.file_size

    assert pdf_name == pdf_archive_file_name, print(f"{pdf_name} не равна {pdf_archive_file_name}")
    assert pdf_size == pdf_archive_file_size, print(f"{pdf_size} не равна {pdf_archive_file_size}")
    assert text_name == txt_archive_file_name, print(f"{text_name} не равна {txt_archive_file_name}")
    assert text_size == txt_archive_file_size, print(f"{text_size} не равна {txt_archive_file_size}")
    assert xls_name == xls_archive_file_name, print(f"{xls_name} не равна {xls_archive_file_name}")
    assert xls_size == xls_archive_file_size, print(f"{xls_size} не равна {xls_archive_file_size}")
    assert xlsx_name == xlsx_archive_file_name, print(f"{xlsx_name} не равна {xlsx_archive_file_name}")
    assert xlsx_size == xlsx_archive_file_size, print(f"{xlsx_size} не равна {xlsx_archive_file_size}")

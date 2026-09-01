import qtawesome as qta
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QComboBox,
    QTextEdit,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
    QPushButton,
    QCheckBox,
    QFrame,
    QScrollArea,
    QGridLayout
)

class BillManagementPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        # Outer Scroll Area to ensure clean responsive layout on all screen sizes
        scroll = QScrollArea(self)
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("""
            QScrollArea {
                border: none;
                background-color: #F8FAFC;
            }
            QScrollBar:vertical {
                border: none;
                background: #F1F5F9;
                width: 6px;
                margin: 0px;
            }
            QScrollBar::handle:vertical {
                background: #CBD5E1;
                min-height: 20px;
                border-radius: 3px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0px;
            }
        """)

        container = QWidget()
        container.setStyleSheet("""
            QWidget {
                font-family: 'Segoe UI', 'Inter', sans-serif;
                background-color: #F8FAFC;
            }
            QLabel {
                background: transparent;
            }
            QLineEdit, QComboBox, QTextEdit {
                background-color: #FFFFFF;
                border: 1px solid #CBD5E1;
                border-radius: 6px;
                padding: 6px 10px;
                color: #0F172A;
                font-size: 13px;
                selection-background-color: #2563EB;
            }
            QLineEdit:focus, QComboBox:focus, QTextEdit:focus {
                border: 1.5px solid #2563EB;
            }
            QComboBox::drop-down {
                border: none;
                width: 22px;
            }
        """)
        
        main_layout = QVBoxLayout(container)
        main_layout.setContentsMargins(24, 20, 24, 20)
        main_layout.setSpacing(16)

        # ----------------------------------------------------
        # 1. Page Title & Subtitle
        # ----------------------------------------------------
        title_box = QVBoxLayout()
        title_box.setSpacing(3)

        lbl_title = QLabel("Create Contingent Bill")
        lbl_title.setStyleSheet("color: #0F3866; font-size: 20px; font-weight: 700;")

        lbl_sub = QLabel("Enter bill details and generate voucher")
        lbl_sub.setStyleSheet("color: #64748B; font-size: 13px;")

        title_box.addWidget(lbl_title)
        title_box.addWidget(lbl_sub)
        main_layout.addLayout(title_box)

        # ----------------------------------------------------
        # 2. Header Form Fields Card (Top Section)
        # ----------------------------------------------------
        header_card = QFrame()
        header_card.setStyleSheet("""
            QFrame {
                background-color: #FFFFFF;
                border: 1px solid #E2E8F0;
                border-radius: 10px;
            }
        """)
        header_card_layout = QVBoxLayout(header_card)
        header_card_layout.setContentsMargins(18, 16, 18, 16)
        header_card_layout.setSpacing(12)

        # Helper function to create field box
        def make_field(label_text, widget):
            box = QVBoxLayout()
            box.setSpacing(5)
            lbl = QLabel(label_text)
            lbl.setStyleSheet("color: #334155; font-size: 12px; font-weight: 600;")
            box.addWidget(lbl)
            box.addWidget(widget)
            return box

        # Row 1: 7 Fields Layout
        row1_layout = QHBoxLayout()
        row1_layout.setSpacing(12)

        # 1. DDO Code
        txt_ddo = QLineEdit("GH-0018")
        txt_ddo.setFixedHeight(36)
        txt_ddo.setReadOnly(True)
        txt_ddo.setStyleSheet("background-color: #F1F5F9; color: #0F172A; font-weight: 600;")
        row1_layout.addLayout(make_field("DDO Code", txt_ddo), 1)

        # 2. Bill No.
        txt_bill_no = QLineEdit("Auto Generated")
        txt_bill_no.setFixedHeight(36)
        txt_bill_no.setReadOnly(True)
        txt_bill_no.setStyleSheet("background-color: #F8FAFC; color: #94A3B8;")
        row1_layout.addLayout(make_field("Bill No.", txt_bill_no), 1)

        # 3. Bill Date
        date_box = QFrame()
        date_box.setFixedHeight(36)
        date_box.setStyleSheet("background-color: #FFFFFF; border: 1px solid #CBD5E1; border-radius: 6px;")
        db_layout = QHBoxLayout(date_box)
        db_layout.setContentsMargins(8, 2, 8, 2)
        txt_date = QLineEdit("02-Jun-2026")
        txt_date.setStyleSheet("border: none; color: #0F172A; font-size: 13px;")
        cal_btn = QLabel()
        cal_ic = qta.icon("fa5s.calendar-alt", color="#64748B")
        cal_btn.setPixmap(cal_ic.pixmap(14, 14))
        db_layout.addWidget(txt_date, 1)
        db_layout.addWidget(cal_btn)
        row1_layout.addLayout(make_field("Bill Date", date_box), 1)

        # 4. Financial Year
        cmb_fin_year = QComboBox()
        cmb_fin_year.setFixedHeight(36)
        cmb_fin_year.addItems(["2026 - 2027", "2025 - 2026"])
        row1_layout.addLayout(make_field("Financial Year", cmb_fin_year), 1)

        # 5. Major Function
        cmb_major = QComboBox()
        cmb_major.setFixedHeight(36)
        cmb_major.addItems(["GH-0018", "GH-0019"])
        row1_layout.addLayout(make_field("Major Function", cmb_major), 1)

        # 6. Minor Function
        cmb_minor = QComboBox()
        cmb_minor.setFixedHeight(36)
        cmb_minor.setStyleSheet("color: #64748B;")
        cmb_minor.addItem("Select Minor Function")
        row1_layout.addLayout(make_field("Minor Function", cmb_minor), 1)

        # 7. No. of Vouchers
        txt_vouchers = QLineEdit("0")
        txt_vouchers.setFixedHeight(36)
        row1_layout.addLayout(make_field("No. of Vouchers", txt_vouchers), 1)

        header_card_layout.addLayout(row1_layout)

        # Row 2: Detailed Function + Description / Contents
        row2_layout = QHBoxLayout()
        row2_layout.setSpacing(14)

        cmb_detail_func = QComboBox()
        cmb_detail_func.setFixedHeight(36)
        cmb_detail_func.addItem("A-01277 Contingent Paid Staff Payment")
        row2_layout.addLayout(make_field("Detailed Function", cmb_detail_func), 1)

        txt_desc = QLineEdit("Contingent Paid Staff Payment for the month of June 2026")
        txt_desc.setFixedHeight(36)
        row2_layout.addLayout(make_field("Description / Contents", txt_desc), 2)

        header_card_layout.addLayout(row2_layout)
        main_layout.addWidget(header_card)

        # ----------------------------------------------------
        # 3. Main 3-Column Section Layout
        # ----------------------------------------------------
        columns_layout = QHBoxLayout()
        columns_layout.setSpacing(16)

        # ====================================================
        # COLUMN 1: Budget & Expenditure (Left Card)
        # ====================================================
        col1_card = QFrame()
        col1_card.setStyleSheet("background-color: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 10px;")
        col1_layout = QVBoxLayout(col1_card)
        col1_layout.setContentsMargins(16, 16, 16, 16)
        col1_layout.setSpacing(12)

        lbl_c1_title = QLabel("Budget & Expenditure")
        lbl_c1_title.setStyleSheet("color: #0F3866; font-size: 15px; font-weight: bold;")
        col1_layout.addWidget(lbl_c1_title)

        # Budget Table
        tbl_budget = QTableWidget()
        tbl_budget.setColumnCount(4)
        tbl_budget.setHorizontalHeaderLabels([
            "Object Classification",
            "Budget Allocated\n(Up to Date)",
            "Expenditure\n(Up to Date)",
            "Balance"
        ])
        
        tbl_header = tbl_budget.horizontalHeader()
        tbl_header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        tbl_header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        tbl_header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        tbl_header.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)

        tbl_budget.verticalHeader().setVisible(False)
        tbl_budget.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        tbl_budget.setSelectionMode(QTableWidget.SelectionMode.NoSelection)
        tbl_budget.setStyleSheet("""
            QTableWidget {
                border: 1px solid #E2E8F0;
                gridline-color: #F1F5F9;
                font-size: 12px;
                background-color: #FFFFFF;
            }
            QHeaderView::section {
                background-color: #F8FAFC;
                color: #0F3866;
                font-weight: bold;
                font-size: 11.5px;
                border: 1px solid #E2E8F0;
                padding: 6px 4px;
            }
            QTableWidget::item {
                padding: 6px;
                color: #1E293B;
            }
        """)

        tbl_rows = [
            ("A-01277 Contingent Paid Staff", "Rs.444,000", "Rs.0", "Rs.444,000", False),
            ("A-03001 Conveyance Charges", "-", "-", "-", False),
            ("A-03201 Stationery", "-", "-", "-", False),
            ("A-03202 Conferences / Seminars / Workshops", "-", "-", "-", False),
            ("A-03205 Newspapers, Periodicals And Books", "-", "-", "-", False),
            ("Total", "Rs.444,000", "Rs.0", "Rs.444,000", True),
        ]

        tbl_budget.setRowCount(len(tbl_rows))
        for r_idx, (c_name, c_alloc, c_exp, c_bal, is_total) in enumerate(tbl_rows):
            i_name = QTableWidgetItem(c_name)
            i_alloc = QTableWidgetItem(c_alloc)
            i_exp = QTableWidgetItem(c_exp)
            i_bal = QTableWidgetItem(c_bal)

            if is_total:
                font_bold = i_name.font()
                font_bold.setBold(True)
                for item in [i_name, i_alloc, i_exp, i_bal]:
                    item.setFont(font_bold)
                    item.setBackground(Qt.GlobalColor.white)

            i_alloc.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
            i_exp.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
            i_bal.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

            tbl_budget.setItem(r_idx, 0, i_name)
            tbl_budget.setItem(r_idx, 1, i_alloc)
            tbl_budget.setItem(r_idx, 2, i_exp)
            tbl_budget.setItem(r_idx, 3, i_bal)

        col1_layout.addWidget(tbl_budget, 1)

        # Bottom Controls for Col 1
        col1_bottom_layout = QHBoxLayout()
        col1_bottom_layout.setSpacing(10)

        cmb_curr_obj = QComboBox()
        cmb_curr_obj.setFixedHeight(36)
        cmb_curr_obj.addItem("A-01277 Contingent Paid Staff")
        col1_bottom_layout.addLayout(make_field("Object Classification for Current Bill", cmb_curr_obj), 2)

        txt_curr_amt = QLineEdit("Rs.37,000")
        txt_curr_amt.setFixedHeight(36)
        txt_curr_amt.setStyleSheet("font-weight: bold; color: #0F172A;")
        col1_bottom_layout.addLayout(make_field("Current Bill Amount", txt_curr_amt), 1)

        col1_layout.addLayout(col1_bottom_layout)
        columns_layout.addWidget(col1_card, 4)

        # ====================================================
        # COLUMN 2: Tax & Amount Details (Middle Card)
        # ====================================================
        col2_card = QFrame()
        col2_card.setStyleSheet("background-color: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 10px;")
        col2_layout = QVBoxLayout(col2_card)
        col2_layout.setContentsMargins(16, 16, 16, 16)
        col2_layout.setSpacing(12)

        lbl_c2_title = QLabel("Tax & Amount Details")
        lbl_c2_title.setStyleSheet("color: #0F3866; font-size: 15px; font-weight: bold;")
        col2_layout.addWidget(lbl_c2_title)

        form2_grid = QGridLayout()
        form2_grid.setVerticalSpacing(10)
        form2_grid.setHorizontalSpacing(10)

        # Income Tax (5.5%)
        lbl_it = QLabel("Income Tax (5.5%)")
        lbl_it.setStyleSheet("color: #334155; font-size: 12.5px; font-weight: 500;")
        txt_it = QLineEdit("Rs.2,035")
        txt_it.setFixedHeight(36)
        txt_it.setAlignment(Qt.AlignmentFlag.AlignRight)
        form2_grid.addWidget(lbl_it, 0, 0)
        form2_grid.addWidget(txt_it, 0, 1)

        # General Sales Tax (GST)
        lbl_gst = QLabel("General Sales Tax (GST)")
        lbl_gst.setStyleSheet("color: #334155; font-size: 12.5px; font-weight: 500;")
        txt_gst = QLineEdit("Rs.5,644")
        txt_gst.setFixedHeight(36)
        txt_gst.setAlignment(Qt.AlignmentFlag.AlignRight)
        form2_grid.addWidget(lbl_gst, 1, 0)
        form2_grid.addWidget(txt_gst, 1, 1)

        # Total Tax to be Deducted
        lbl_tot_tax = QLabel("Total Tax to be Deducted")
        lbl_tot_tax.setStyleSheet("color: #0F172A; font-size: 13px; font-weight: bold;")
        txt_tot_tax = QLineEdit("Rs.7,679")
        txt_tot_tax.setFixedHeight(36)
        txt_tot_tax.setAlignment(Qt.AlignmentFlag.AlignRight)
        txt_tot_tax.setStyleSheet("font-weight: bold; color: #0F172A;")
        form2_grid.addWidget(lbl_tot_tax, 2, 0)
        form2_grid.addWidget(txt_tot_tax, 2, 1)

        col2_layout.addLayout(form2_grid)

        # Net Amount Highlight Green Box
        net_box = QFrame()
        net_box.setStyleSheet("background-color: #F0FDF4; border: 1.5px solid #86EFAC; border-radius: 8px;")
        net_layout = QHBoxLayout(net_box)
        net_layout.setContentsMargins(14, 12, 14, 12)

        lbl_net_title = QLabel("Net Amount")
        lbl_net_title.setStyleSheet("color: #166534; font-size: 16px; font-weight: bold;")

        lbl_net_val = QLabel("Rs.29,321")
        lbl_net_val.setStyleSheet("color: #166534; font-size: 18px; font-weight: bold;")

        net_layout.addWidget(lbl_net_title)
        net_layout.addStretch()
        net_layout.addWidget(lbl_net_val)

        col2_layout.addWidget(net_box)

        # In Words Rupees
        lbl_words_title = QLabel("In Words Rupees")
        lbl_words_title.setStyleSheet("color: #64748B; font-size: 12px; font-weight: 600;")
        col2_layout.addWidget(lbl_words_title)

        txt_words = QTextEdit("Twenty Nine Thousand Three Hundred Twenty One Only")
        txt_words.setFixedHeight(60)
        txt_words.setStyleSheet("color: #0F172A; font-size: 12.5px;")
        col2_layout.addWidget(txt_words)

        col2_layout.addStretch()
        columns_layout.addWidget(col2_card, 3)

        # ====================================================
        # COLUMN 3: Vendor Details & Certifications (Right Card)
        # ====================================================
        col3_card = QFrame()
        col3_card.setStyleSheet("background-color: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 10px;")
        col3_layout = QVBoxLayout(col3_card)
        col3_layout.setContentsMargins(16, 16, 16, 16)
        col3_layout.setSpacing(12)

        # Section 1: Vendor Details
        lbl_v_header = QLabel("Vendor Details")
        lbl_v_header.setStyleSheet("color: #0F3866; font-size: 15px; font-weight: bold;")
        col3_layout.addWidget(lbl_v_header)

        v_row1 = QHBoxLayout()
        v_row1.setSpacing(10)

        # Vendor No. Input + Search Icon Inside Box
        v_no_box = QFrame()
        v_no_box.setFixedHeight(36)
        v_no_box.setStyleSheet("background-color: #FFFFFF; border: 1px solid #CBD5E1; border-radius: 6px;")
        vnb_layout = QHBoxLayout(v_no_box)
        vnb_layout.setContentsMargins(6, 2, 6, 2)
        txt_v_no = QLineEdit("30276386")
        txt_v_no.setStyleSheet("border: none; color: #0F172A; font-size: 12.5px;")
        btn_search = QLabel()
        search_ic = qta.icon("fa5s.search", color="#64748B")
        btn_search.setPixmap(search_ic.pixmap(14, 14))
        vnb_layout.addWidget(txt_v_no, 1)
        vnb_layout.addWidget(btn_search)

        v_row1.addLayout(make_field("Vendor No.", v_no_box), 1)

        txt_v_name = QLineEdit("Ali Nawaz")
        txt_v_name.setFixedHeight(36)
        v_row1.addLayout(make_field("Vendor Name", txt_v_name), 2)

        col3_layout.addLayout(v_row1)

        # Address
        lbl_addr = QLabel("Address")
        lbl_addr.setStyleSheet("color: #334155; font-size: 12px; font-weight: 600;")
        txt_addr = QTextEdit()
        txt_addr.setFixedHeight(50)
        col3_layout.addWidget(lbl_addr)
        col3_layout.addWidget(txt_addr)

        # Section 2: Certifications
        lbl_cert_header = QLabel("Certifications")
        lbl_cert_header.setStyleSheet("color: #0F3866; font-size: 15px; font-weight: bold; margin-top: 4px;")
        col3_layout.addWidget(lbl_cert_header)

        cert_text1 = "1. Certified that the expenditure includes in this bill could not, with due regard to the interests of the public service, be avoided."
        cert_text2 = "2. Certified that all the articles detailed in the vouchers attached with the bill have been accounted for in the stock register."
        cert_text3 = "3. Certified that the purchase billed for have been received in good order and the quantities are correct."

        for c_txt in [cert_text1, cert_text2, cert_text3]:
            chk = QCheckBox(c_txt)
            chk.setChecked(True)
            chk.setStyleSheet("""
                QCheckBox {
                    color: #334155;
                    font-size: 11px;
                    spacing: 6px;
                }
                QCheckBox::indicator {
                    width: 16px;
                    height: 16px;
                    border: 1px solid #CBD5E1;
                    border-radius: 4px;
                    background-color: #FFFFFF;
                }
                QCheckBox::indicator:checked {
                    background-color: #2563EB;
                    border-color: #2563EB;
                }
            """)
            col3_layout.addWidget(chk)

        col3_layout.addStretch()
        columns_layout.addWidget(col3_card, 3)

        main_layout.addLayout(columns_layout, 1)

        # ----------------------------------------------------
        # 4. Bottom Action Buttons Row
        # ----------------------------------------------------
        actions_layout = QHBoxLayout()
        actions_layout.setSpacing(12)
        actions_layout.addStretch()

        # Save Bill Button
        btn_save = QPushButton(" Save Bill")
        save_icon = qta.icon("fa5s.save", color="white")
        btn_save.setIcon(save_icon)
        btn_save.setCursor(Qt.CursorShape.PointingHandCursor)
        btn_save.setStyleSheet("""
            QPushButton {
                background-color: #1E40AF;
                color: #FFFFFF;
                font-size: 13.5px;
                font-weight: 700;
                padding: 10px 22px;
                border-radius: 6px;
                border: none;
            }
            QPushButton:hover {
                background-color: #1D4ED8;
            }
        """)

        # Print Preview Button
        btn_print = QPushButton(" Print Preview")
        print_icon = qta.icon("fa5s.print", color="white")
        btn_print.setIcon(print_icon)
        btn_print.setCursor(Qt.CursorShape.PointingHandCursor)
        btn_print.setStyleSheet("""
            QPushButton {
                background-color: #15803D;
                color: #FFFFFF;
                font-size: 13.5px;
                font-weight: 700;
                padding: 10px 22px;
                border-radius: 6px;
                border: none;
            }
            QPushButton:hover {
                background-color: #16A34A;
            }
        """)

        # Generate Bill Button
        btn_gen = QPushButton(" Generate Bill")
        gen_icon = qta.icon("fa5s.file-contract", color="white")
        btn_gen.setIcon(gen_icon)
        btn_gen.setCursor(Qt.CursorShape.PointingHandCursor)
        btn_gen.setStyleSheet("""
            QPushButton {
                background-color: #0F2942;
                color: #FFFFFF;
                font-size: 13.5px;
                font-weight: 700;
                padding: 10px 22px;
                border-radius: 6px;
                border: none;
            }
            QPushButton:hover {
                background-color: #173B5E;
            }
        """)

        actions_layout.addWidget(btn_save)
        actions_layout.addWidget(btn_print)
        actions_layout.addWidget(btn_gen)

        main_layout.addLayout(actions_layout)

        scroll.setWidget(container)

        outer_layout = QVBoxLayout(self)
        outer_layout.setContentsMargins(0, 0, 0, 0)
        outer_layout.addWidget(scroll)
